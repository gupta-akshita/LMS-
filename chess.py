from enum import Enum

class Color(Enum):
    BLACK = 1
    WHITE = 2

class Piece:
    def __init__(self, color, is_active):
        self.color = color
        self.is_active = is_active

    def is_valid_move(self, x1, y1, x2, y2):
        raise NotImplementedError

    def get_symbol(self):
        raise NotImplementedError

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Account:
    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_admin = is_admin

class Box:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

    def is_occupied(self):
        return self.piece is not None

class Board:
    def __init__(self):
        self.boxes = [[Box(i, j) for j in range(8)] for i in range(8)]

class Move:
    def __init__(self, _from, to, player):
        self._from = _from
        self.to = to
        self.player = player
        self.is_castling = False
        self.captured_piece = None

class Game:
    def __init__(self, white, black):
        self.current_player = white
        self.board = Board()
        self.moves = []
        self.game_result = None
        self.white = white
        self.black = black

class GameController:
    def __init__(self, game):
        self.game = game

    def make_move(self, _from, to):
        if _from is None or to is None:
            raise ValueError("Invalid move.")
        piece = _from.piece
        if piece is None or piece.color != self.game.current_player.color:
            raise ValueError("Invalid move.")
        if not piece.is_valid_move(_from.x, _from.y, to.x, to.y):
            raise ValueError("Invalid move.")
        move = Move(_from, to, self.game.current_player)
        if to.is_occupied():
            move.captured_piece = to.piece
        self.game.moves.append(move)
        piece.is_active = False
        to.piece = piece
        _from.piece = None
        self.game.current_player = self.game.black if self.game.current_player == self.game.white else self.game.white

class GameView:
    @staticmethod
    def display_game(game):
        board = game.board
        print("  a b c d e f g h")
        print(" -----------------")
        for i in range(7, -1, -1):
            print(f"{i + 1} |", end="")
            for j in range(8):
                piece = board.boxes[i][j].piece
                if piece is None:
                    print(" |", end="")
                else:
                    print(piece.color.name[0] + piece.get_symbol() + "|", end="")
            print(f" {i + 1}")
        print(" -----------------")
        print("  a b c d e f g h")

class Pawn(Piece):
    def is_valid_move(self, x1, y1, x2, y2):
        if y1 != y2:
            return False
        if self.color == Color.WHITE:
            return x2 == x1 - 1 or (x1 == 6 and x2 == 4)
        else:
            return x2 == x1 + 1 or (x1 == 1 and x2 == 3)

    def get_symbol(self):
        return 'P'

class Rook(Piece):
    def is_valid_move(self, x1, y1, x2, y2):
        return x1 == x2 or y1 == y2

    def get_symbol(self):
        return 'R'

class Knight(Piece):
    def is_valid_move(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

    def get_symbol(self):
        return 'N'

class Bishop(Piece):
    def is_valid_move(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return dx == dy

    def get_symbol(self):
        return 'B'

class Queen(Piece):
    def is_valid_move(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return dx == dy or x1 == x2 or y1 == y2

    def get_symbol(self):
        return 'Q'

class King(Piece):
    def is_valid_move(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return dx <= 1 and dy <= 1

    def get_symbol(self):
        return 'K'

# Example usage
if __name__ == "__main__":
    white = Player("Alice", Color.WHITE)
    black = Player("Bob", Color.BLACK)
    game = Game(white, black)
    controller = GameController(game)
    GameView.display_game(game)

    # Play a few moves
    try:
        controller.make_move(game.board.boxes[6][4], game.board.boxes[4][4])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[1][3], game.board.boxes[3][3])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[7][5], game.board.boxes[5][4])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[0][6], game.board.boxes[2][5])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[7][6], game.board.boxes[5][5])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[0][5], game.board.boxes[1][3])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[7][4], game.board.boxes[3][0])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[1][0], game.board.boxes[2][2])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[7][3], game.board.boxes[3][7])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[0][2], game.board.boxes[1][4])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[7][7], game.board.boxes[5][6])
        GameView.display_game(game)
        controller.make_move(game.board.boxes[0][3], game.board.boxes[4][7])
        GameView.display_game(game)
    except ValueError as e:
        print("Error:", e)

    # Game over
    print("Game over! Result:", game.game_result)

    # Clean up
    del white
    del black
    del game
