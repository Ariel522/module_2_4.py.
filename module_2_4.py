numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue
    is_primes = True
    for j in range (2, number):
        if number % j == 0:
            is_primes = False
            break
    if is_primes == True:
        not_primes.append(number)
    else:
        primes.append(number)
print('Список простых чисел:' , primes)
print('Список не простых чисел:', not_primes)
