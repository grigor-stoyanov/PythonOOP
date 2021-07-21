class ImageArea:
    def __init__(self, wth, hth):
        self.wth = wth
        self.hth = hth

    def get_area(self):
        return self.wth * self.hth

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()
