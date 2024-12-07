from TetriminoType import TetriminoType

class TetriminoFactory:
    _tetriminos = {}

    @staticmethod
    def get_tetrimino(shape, color):
        """Obtiene un Tetrimino compartido si ya existe, o lo crea si no"""
        key = (shape, color)
        if key not in TetriminoFactory._tetriminos:
            coordinates = TetriminoFactory.create_coordinates(shape)
            TetriminoFactory._tetriminos[key] = TetriminoType(shape, color, coordinates)
        return TetriminoFactory._tetriminos[key]

    @staticmethod
    def create_coordinates(shape):
        """Genera las coordenadas de cada forma de Tetrimino"""
        if shape == "I":
            return [(0, 1), (1, 1), (2, 1), (3, 1)]
        elif shape == "O":
            return [(0, 0), (1, 0), (0, 1), (1, 1)]
        elif shape == "T":
            return [(0, 1), (1, 1), (2, 1), (1, 0)]
        elif shape == "S":
            return [(1, 0), (2, 0), (0, 1), (1, 1)]
        elif shape == "Z":
            return [(0, 0), (1, 0), (1, 1), (2, 1)]
        elif shape == "L":
            return [(0, 1), (1, 1), (2, 1), (2, 0)]
        elif shape == "J":
            return [(0, 1), (1, 1), (2, 1), (0, 0)]