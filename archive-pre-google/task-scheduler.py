class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = [-f for f in Counter(tasks).values()]
        heapq.heapify(pq)

        time = 0
        # Process tasks until the heap is empty
        '''
        a b c d . .
        a b c . . .
        a b . . . .
        a b
        pq [-4 -4 -2 -1] | n 5 | ans 20
        time,cycle 0,5
        store [3]
        task_count 1
        current_freq 4
        '''
        while pq:
            store = []
            task_count = 0
            
            # Execute tasks in each cycle
            for _ in range(n+1):
                if not pq: 
                    break
                current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
            
            for x in store:
                heapq.heappush(pq, x)

            time += task_count if not pq else n + 1
        return time