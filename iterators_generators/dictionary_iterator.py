class dictionary_iter:
    def __init__(self, dic_obj):
        self.dic_obj = dic_obj
        self.keys = list(self.dic_obj.keys())
        # self.key_vlues = self.dic_obj.items()
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.keys):
            raise StopIteration
        return self.keys[self.i], self.dic_obj[self.keys[self.i]]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
