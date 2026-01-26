/*
could get the prime factors of n, and return true if they're only 2 3 5
false otherwise. 

special case for 1 --> ugly

brute force: just enumerate on odd numbers seeing if they divide n
inefficient because we are testing numbers like 27 which aren't prime
but if we could know if a number is prime first, then if that number
divides n, then it isn't ugly when it doesn't divide 2, 3, or 5.

oh wait, even simpler. do a div on 2 3 5, and if anything is e


14 -- 
1. get all prime numbers less than 14
2. if any divides 14, then ugly

14 / 2 = 7 <-- could stop here, well if u knew 7 was prime
14 / 3  don't do it since it doesnt divide
14 / 5 dont do it, doesnt divide

approach: after diving through the three (if they divide), if something remains, 
then not ugly. otherwise ugly
*/
func isUgly(n int) bool {
    if n < 1 {
        return false
    } else if n == 1 {
        return true
    }

    for ; ; {
        if n == 1 {
            return true
        }
        if n % 2 == 0 { 
            n /= 2
        } else if n % 3 == 0 {
            n /= 3
        } else if n % 5 == 0 {
            n /= 5
        } else {
            return false
        }
    }

}