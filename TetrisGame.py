import tkinter as tk
import random

from Tetrimino import Tetrimino
from TetriminoFactory import TetriminoFactory
from TetriminoType import TetriminoType

class TetrisGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=300, height=600)
        self.canvas.pack()
        self.pieces = []
        self.current_piece = None
        self.game_over = False
        self.board = [[0] * 10 for _ in range(20)]
        self.create_new_piece()

        # Eventos de teclado
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate)

        # Temporizador para el movimiento automático hacia abajo
        self.auto_move()

    def create_new_piece(self):
        """Crea una nueva pieza aleatoria"""
        shapes = ["I", "O", "T", "S", "Z", "L", "J"]
        colors = ["cyan", "yellow", "purple", "green", "red", "blue", "orange"]
        shape = random.choice(shapes)
        color = random.choice(colors)
        self.current_piece = Tetrimino(4, 0, shape, color)

    def auto_move(self):
        """Movimiento automático hacia abajo"""
        if not self.game_over:
            self.move_down(None)
            self.root.after(500, self.auto_move)

    def move_left(self, event):
        """Mueve la pieza hacia la izquierda"""
        if not self.game_over:
            self.current_piece.move_left()
            if self.check_collision():
                self.current_piece.move_right()  # Revierte el movimiento si hay colisión
            self.update_canvas()

    def move_right(self, event):
        """Mueve la pieza hacia la derecha"""
        if not self.game_over:
            self.current_piece.move_right()
            if self.check_collision():
                self.current_piece.move_left()  # Revierte el movimiento si hay colisión
            self.update_canvas()

    def move_down(self, event):
        """Mueve la pieza hacia abajo"""
        if not self.game_over:
            self.current_piece.move_down()
            if self.check_collision():
                self.current_piece.y -= 1  # Detiene el movimiento y coloca la pieza
                self.place_piece()
                self.create_new_piece()
                if self.check_game_over():
                    self.display_game_over()
            self.update_canvas()

    def rotate(self, event):
        """Rota la pieza"""
        if not self.game_over:
            self.current_piece.rotate()
            if self.check_collision():
                # Revierte la rotación si hay colisión
                self.current_piece.rotate()
                self.current_piece.rotate()
                self.current_piece.rotate()
            self.update_canvas()

    def check_collision(self):
        """Verifica si la pieza colisiona con los límites del tablero o con otras piezas"""
        for x, y in self.current_piece.get_coordinates():
            if x < 0 or x >= 10 or y >= 20 or self.board[y][x]:
                return True
        return False

    def place_piece(self):
        """Coloca la pieza en el tablero"""
        for x, y in self.current_piece.get_coordinates():
            self.board[y][x] = 1
        self.remove_full_lines()

    def remove_full_lines(self):
        """Elimina las líneas completas"""
        for y in range(19, -1, -1):
            if all(self.board[y]):
                self.board.pop(y)
                self.board.insert(0, [0] * 10)
                break

    def check_game_over(self):
        """Verifica si el juego ha terminado"""
        for x, y in self.current_piece.get_coordinates():
            if y < 0:
                return True
        return False

    def update_canvas(self):
        """Actualiza el lienzo dibujando todas las piezas en el tablero"""
        self.canvas.delete("all")
        for y in range(20):
            for x in range(10):
                if self.board[y][x]:
                    self.canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="gray")
        self.current_piece.draw(self.canvas)

    def display_game_over(self):
        """Muestra el mensaje de fin de juego"""
        self.canvas.create_text(150, 300, text="GAME OVER", fill="red", font=("Arial", 24))

# Inicialización del juego
root = tk.Tk()
root.title("Juego de Tetris")
game = TetrisGame(root)
root.mainloop()