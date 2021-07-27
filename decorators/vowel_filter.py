def vowel_filter(function):
    def wrapper():
        result = function()
        result = list(filter(lambda x: True if x in 'aeouiyAEOUYI' else False, result))
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
