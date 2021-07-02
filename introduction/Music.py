class Music:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics


def print_info(self):
    return f'This is "{self.title}" from "{self.author}"'


def play(self):
    return self.lyrics


song = Music('Title', 'Artist', 'Lyrics')
print(song.print_info())
print(song.play())
