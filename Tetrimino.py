from TetriminoFactory import TetriminoFactory

class Tetrimino:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.rotation = 0
        self.tetrimino_type = TetriminoFactory.get_tetrimino(shape, color)

    def draw(self, canvas):
        """Dibuja la pieza en el lienzo en la posición correspondiente"""
        self.tetrimino_type.draw(canvas, self.x * 30, self.y * 30)

    def rotate(self):
        """Rota la pieza 90 grados"""
        self.rotation = (self.rotation + 90) % 360
        self.tetrimino_type.coordinates = [(dy, -dx) for dx, dy in self.tetrimino_type.coordinates]

    def move_down(self):
        """Mueve la pieza hacia abajo"""
        self.y += 1

    def move_left(self):
        """Mueve la pieza hacia la izquierda"""
        self.x -= 1

    def move_right(self):
        """Mueve la pieza hacia la derecha"""
        self.x += 1

    def get_coordinates(self):
        """Devuelve las coordenadas actuales de la pieza"""
        return [(self.x + dx, self.y + dy) for dx, dy in self.tetrimino_type.coordinates]