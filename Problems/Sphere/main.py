class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = Sphere.PI * radius ** 3 * 4 / 3
