# Classes Lab - Tic-Tac Toe

class Game():
  def __init__(self):
    self.x_score = 0
    self.o_score = 0
    self.reset()

  def reset(self):
    self.turn = "X"
    self.tie = False
    self.winner = None
    self.board = {
      'a1': None, 'b1': None, 'c1': None,
      'a2': None, 'b2': None, 'c2': None,
      'a3': None, 'b3': None, 'c3': None,
    }    

  def print_board(self):
    b = self.board
    print(f"""
          A   B   C
      1) {b['a1'] or ' '}  | {b['b1'] or ' '} | {b['c1'] or ' '}
         ---|---|---
      2) {b['a2'] or ' '}  | {b['b2'] or ' '} | {b['c2'] or ' '}
         ---|---|---
      3) {b['a3'] or ' '}  | {b['b3'] or ' '} | {b['c3'] or ' '}
    """)
  
  def print_message(self):
    if self.winner is not None:
      print(f"{self.winner} wins!")
    elif self.tie is True:
      print("It's a tie!")
    else:
      print(f"It's Player {self.turn}'s turn")
  
  def render(self):
    self.print_board()
    self.print_message()

  def get_move(self):
    while True:
      move = input(f"Enter a valid move (example: A1): ").lower()
      if move in self.board and self.board[move] is None:
        self.board[move] = self.turn
        break
      else:
        print("Invalid move. Try again.")
  
  def check_winner(self):
    b = self.board
    if (b['a1'] == b['b1'] == b['c1'] != None or
      b['a2'] == b['b2'] == b['c2'] != None or
      b['a3'] == b['b3'] == b['c3'] != None or
      b['a1'] == b['a2'] == b['a3'] != None or
      b['b1'] == b['b2'] == b['b3'] != None or
      b['c1'] == b['c2'] == b['c3'] != None or
      b['a1'] == b['b2'] == b['c3'] != None or
      b['a3'] == b['b2'] == b['c1'] != None):
      self.winner = self.turn

  def check_tie(self):
    if self.winner is None and None not in self.board.values():
      self.tie = True
  
  def switch_turn(self):
    self.turn = "O" if self.turn == "X" else "X"

  def play_again(self):
    while True:
      choice = input("Do you want to play again? (y/n) ").lower()
      if choice == "y":
        return True
      elif choice == "n":
        return False
      else:
        print("Invalid choice. Try again.")

  def play_game(self):
    print("Welcome to Tic-Tac-Toe!")
    while self.winner is None and not self.tie:
      self.render()
      self.get_move()
      self.check_winner()
      self.check_tie()
      if self.winner is None and not self.tie:
        self.switch_turn()
    self.print_board()
    if self.winner == 'X':
      self.x_score += 1
    elif self.winner == 'O':
      self.o_score += 1
    self.print_message()
    print(f"Score: Player X - {self.x_score} | Player O - {self.o_score}")
    
game_instance = Game()

while True:
  game_instance.play_game()
  if not game_instance.play_again():
    print("Thanks for playing!")
    break
  game_instance.reset()
