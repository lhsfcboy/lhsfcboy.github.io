# Ugly number is a number that only have factors 2, 3 and 5.

# Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

def nthUglyNumber(n):
    located_ugly_numbers = set([1,])
    unlocated_ugly_number = set([])
    while n > len(located_ugly_numbers):
        current_max_ugly = max(located_ugly_numbers)
        for i in [current_max_ugly * i for i in (2,3,5)]:
            unlocated_ugly_number.add(i) 
        
        next_ugly_number = min(unlocated_ugly_number)
        unlocated_ugly_number.remove(next_ugly_number)
        located_ugly_numbers.add(next_ugly_number)
        print(located_ugly_numbers)
        print(unlocated_ugly_number)
    return max(located_ugly_numbers)

print(nthUglyNumber(9)    )