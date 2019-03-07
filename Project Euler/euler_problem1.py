"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
def mult35(val):
    total = 0
    for i in range(0,val):
        if not i%3 or not i%5:
             total+=i
    return total

if __name__ == "__main__":
    print(mult35(1000))