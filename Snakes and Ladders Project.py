import random
import tkinter as tk

class Player:
    def __init__(self, id, color):
        self.id = id
        self.position = 0
        self.color = color

class Game:
    def __init__(self, num_players):
        colors = ['red', 'blue', 'green', 'yellow']
        self.players = [Player(i, colors[i]) for i in range(num_players)]
        self.snakes, self.ladders = self.create_snakes_and_ladders()
        self.board = self.create_board()
        self.current_player = 0

    def create_snakes_and_ladders(self):
        snakes = {}
        ladders = {}
        for _ in range(10):
            start = random.randint(20, 80)
            while start in snakes or start in ladders:
                start = random.randint(20, 80)
            if random.choice([True, False]):
                end = random.randint(1, start-1)
                snakes[start] = end
            else:
                end = random.randint(start+1, 100)
                ladders[start] = end
        return snakes, ladders

    def create_board(self):
        board = [['-']*10 for _ in range(10)]
        for snake in self.snakes:
            row, col = divmod(snake-1, 10)
            board[9-row][col] = f'S({self.snakes[snake]})'
        for ladder in self.ladders:
            row, col = divmod(ladder-1, 10)
            board[9-row][col] = f'L({self.ladders[ladder]})'
        return board

    def play_turn(self, roll_buttons):
        player = self.players[self.current_player]
        roll = random.randint(1, 6)
        print(f"Player {player.id+1} rolled a {roll}.")
        if player.position + roll <= 100:
            player.position += roll
            player.position = self.snakes.get(player.position, player.position)
            player.position = self.ladders.get(player.position, player.position)
        print(f"Player {player.id+1} is now on square {player.position}.")
        if player.position == 100:
            print(f"Player {player.id+1} wins!")
            return True
        self.current_player = (self.current_player + 1) % len(self.players)
        for i in range(len(roll_buttons)):
            if i == self.current_player:
                roll_buttons[i].config(state='normal')
            else:
                roll_buttons[i].config(state='disabled')
        return False

    def play_game(self):
        root = tk.Tk()
        buttons = []
        for i in range(10):
            row = []
            for j in range(10):
                tile_num = 10 * (9 - i) + j + 1
                button = tk.Button(root, text=f'{self.board[i][j]}\n{tile_num}', width=10, height=3)
                button.grid(row=i, column=j, padx=1, pady=1)  # Adjust padding here
                row.append(button)
            buttons.append(row)

        def update_board():
            for i in range(10):
                for j in range(10):
                    tile_num = 10 * (9 - i) + j + 1
                    buttons[i][j].config(text=f'{self.board[i][j]}\n{tile_num}', bg='white')
            for player in self.players:
                row, col = divmod(player.position-1, 10)
                buttons[9-row][col].config(text=f'{player.id+1}\n{player.position}', bg=player.color)

        roll_buttons = []
        for player in self.players:
            def roll_dice(player=player):
                if self.play_turn(roll_buttons):
                    for button in roll_buttons:
                        button.config(state='disabled')
                update_board()
            button = tk.Button(root, text=f"Player {player.id+1} Roll Dice", command=roll_dice)
            button.grid(row=10, column=player.id, padx=1, pady=1)  # Adjust padding here
            roll_buttons.append(button)

        for i in range(1, len(roll_buttons)):
            roll_buttons[i].config(state='disabled')

        root.mainloop()

if __name__ == "__main__":
    num_players = int(input("Enter the number of players (2-4): "))
    game = Game(num_players)
    game.play_game()
