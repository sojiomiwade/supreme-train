'''
Pancake Sort
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.

Example:

input:  arr = [1, 5, 4, 3, 2]

1 5 4 3 2
1 2 3 4 5

3 1 4 5 2
54132
23145

41325
23145

23145
32145
12345 flip(n) n is window size

one more flip for next biggest

flip(4) 5 to the front
flip(5) 5 to the back
flip(4) 
flip(4)

window = n

flip at the biggest idx --> flip(bidx+1)!
flip window size --> flip(window)
window --
do above len(arr) - 1 times, since last n-1 sorted from biggest means smallest is left in arr[0]

now narrow array


output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.

Note: it's called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.

Constraints:

[time limit] 5000ms

[input] array.integer arr

[input] integer k

0 ≤ k
[output] array.integer
time: 9:26 -- 

3 1 4 5 2
54132
23145

41325
23145

23145
32145
12345 flip(n) n is window size

one more flip for next biggest

flip(4) 5 to the front
flip(5) 5 to the back
flip(4) 
flip(4)

window = n

flip at the biggest idx --> flip(bidx+1)!
flip window size --> flip(window)
window --
do above len(arr) - 1 times, since last n-1 sorted from biggest means smallest is left in arr[0]
'''

from typing import List


def pancakeSort(arr: List[int]) -> List[int]:
    def findmaxidx() -> int:
        bidx = 0
        maxval = arr[0]
        for i in range(window): #2, 1
            if arr[i] > maxval:
                bidx, maxval = i, arr[i]
        return bidx

    def flip(k: int) -> None: #1,2
        for i in range(k//2): # 1 one time
            j = k - 1 - i #1
            arr[i], arr[j] = arr[j], arr[i]

    window = len(arr)
    for window in range(len(arr), 1, -1): # 3, 2
        bidx = findmaxidx() # 1
        flip(bidx + 1) # 123 -> 213
        flip(window) # 321 -> 123, 213 -> 123
    return arr

arr = [2,3,1]
print(pancakeSort(arr))

