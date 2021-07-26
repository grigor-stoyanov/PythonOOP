class vowels:
    def __init__(self, text):
        self.text = text
        self.start = -1
        self.all_vowels = 'AEOUIYaeouiy'
        self.vowels_list = [el for el in self.text if el in self.all_vowels]
        self.end = len(self.vowels_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.vowels_list[self.start]


my_string = vowels('adwebuirbbbAdduiib')
for char in my_string:
    print(char)
