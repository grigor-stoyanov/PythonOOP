class PhotoAlbum:
    IS_FULL = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for i, page in enumerate(self.photos):
            if not len(page) == PhotoAlbum.IS_FULL:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = [f'{"[] " * len(page)}'.strip() for page in self.photos]
        return f"-----------\n"+f'\n-----------\n'.join(result)+"\n-----------"


album = PhotoAlbum(2)
print(album.add_photo('baby'))
print(album.add_photo('first grade'))
print(album.add_photo('eight grade'))
print(album.add_photo('party with friends'))
print(album.photos)
print(album.add_photo('prom'))
print(album.add_photo('wedding'))
print(album.display())
