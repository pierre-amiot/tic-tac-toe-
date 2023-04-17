import tkinter as tk
import random
from ia import ia

# Créer la fenêtre de jeu
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialiser les variables de jeu
player = 1  # Le joueur 1 commence
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Plateau de jeu vide
game_over = False

# Fonction pour vérifier si un joueur a gagné
def check_win(player):
    # Vérifier les lignes
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Vérifier les colonnes
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Vérifier les diagonales
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    # Aucun alignement de trois signes trouvés
    return False

# Fonction pour afficher un message de fin de partie
def show_message(message):
    global label
    label.config(text=message)

# Fonction pour gérer le clic sur une case
def on_click(i):
    global player, game_over
    if not game_over and board[i] == 0:
        board[i] = player
        buttons[i].config(text="X" if player == 1 else "O")
        if check_win(player):
            show_message("Joueur " + str(player) + " a gagné !")
            game_over = True
        elif all(board):
            show_message("Match nul !")
            game_over = True
        else:
            player = 2 if player == 1 else 1
            if not game_over and player == 2:
                # Laisser l'IA jouer
                i = ia(board, "O" if player == 1 else "X")
                if i is False:
                    show_message("L'IA a rencontré une erreur.")
                    game_over = True
                elif board[i] != 0:
                    player = 2 if player == 1 else 1
                else:
                    on_click(i)

# Créer les boutons pour les cases du plateau de jeu
buttons = []
for i in range(9):
    button = tk.Button(root, text="", width=6, height=3,
                       command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Créer une étiquette pour afficher le message de fin de partie
label = tk.Label(root, text="")
label.grid(row=3, column=0, columnspan=3)

# Lancer le jeu
root.mainloop()