def empty_string_pro(name):
    @property
    def pro(self):
        return getattr(self, '__' + name)

    @pro.setter
    def pro(self, val):
        if isinstance(val, str) and not val == '':
            return setattr(self, '__' + name, val)
        err_msg = f'The {" ".join(name.split("_"))} cannot be an empty string'
        raise ValueError(err_msg)

    return pro


def sub_zero_pro(name):
    @property
    def pro(self):
        return getattr(self, '__' + name)

    @pro.setter
    def pro(self, val):
        if isinstance(val, int) and not val <= 0:
            return setattr(self, '__' + name, val)
        raise ValueError(f'The {" ".join(name.split("_"))} cannot be less or equal to zero')

    return pro


class Dough:
    flour_type = empty_string_pro('flour_type')
    baking_technique = empty_string_pro('baking_technique')
    weight = sub_zero_pro('weight')

    def __init__(self, flour_type: str, baking_technique: str, weight: int):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

