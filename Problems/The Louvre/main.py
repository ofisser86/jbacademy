class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


painter = Painting(input(), input(), input())
print(f'"{painter.title}" by {painter.artist} ({painter.year}) hangs in the {painter.museum}.')
