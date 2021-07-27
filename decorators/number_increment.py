def number_increment(nums):
    def increase():
        # increase has access to nums from outer scope
        return [num + 1 for num in nums]

    # we return a reference to the function
    return increase


func = number_increment([1, 2, 3])
print(func())
