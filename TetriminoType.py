class TetriminoType:
    def __init__(self, shape, color, coordinates):
        self.shape = shape
        self.color = color
        self.coordinates = coordinates

    def draw(self, canvas, x, y):
        for dx, dy in self.coordinates:
            canvas.create_rectangle(x + dx * 30, y + dy * 30, x + (dx + 1) * 30, y + (dy + 1) * 30, fill=self.color)