# Check whether each number smaller than n is a prime
# Append the primes into a list
num = int(input("Please enter an integer n, n > 2: "))
prime_list = list()
for digit in range(2, num):
    flag = True
    #for i in range(2, digit):     
    for i in range(2, int(digit ** 0.5 + 1)):
        if digit % i == 0:
            flag = False
            break
    if flag:
        prime_list.append(digit)
print("All the prime numbers smaller than", num, "are:")
print(prime_list)