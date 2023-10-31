'''
sieve of eratosthenes
thinking: if you cancel all multiples of a prime, for some i, then the next number you run into is also prime.

(2) 3 4 5 6 7 8 9 10 11 12 13 14 15
2 (3) 5 7 9 11 13 15
2 3 5 7 11 13
now check if n is canceled off! can check early too
time: O(n), since we did at least half the least initially

repeat from x = 2 to sqrt(n) [inclusive]
run to next number, and scratch off multiples upto n


func sieve(n
'''
def isprime(n: int) -> bool:
    isprime = [True for _ in range(n+1)]
    x = 2
    while x <= 1 + int(n**0.5): #  3 <= 3
        for y in range(x**2, n+1, x):
            isprime[y] = False
        x += 1
        while not isprime[x]:
            x += 1
    return isprime[-1]
'''
0123456
  ttftf
  x
'''
print(isprime(6)) # false
print(isprime(7)) # true
print(isprime(25)) # false