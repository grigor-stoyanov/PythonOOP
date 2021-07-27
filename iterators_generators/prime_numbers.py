def get_primes(nums):
    is_prime = True
    for num in nums:
        if num <= 1:
            is_prime = False
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
        is_prime = True


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
