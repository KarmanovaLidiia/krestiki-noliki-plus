import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")

current_player = "X"
buttons = []
score = {"X": 0, "0": 0}

score_label = tk.Label(window, text="Счёт - X: 0 | 0: 0", font=("Arial", 12))
score_label.grid(row=3, column=0, columnspan=3, pady=(10, 5))

def update_score():
    score_label.config(text=f"Счёт - X: {score['X']} | 0: {score['0']}")

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn.config(text="")

def on_click(row, col):
    global current_player
    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        score[current_player] += 1
        update_score()
        if score[current_player] == 3:
            messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл игру до трёх побед!")
            score['X'] = 0
            score['0'] = 0
            update_score()
        reset_game()
        return

    if check_draw():
        messagebox.showinfo("Ничья", "На поле не осталось клеток — ничья!")
        reset_game()
        return

    current_player = "0" if current_player == "X" else "X"

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

reset_button = tk.Button(window, text="Сбросить игру", font=("Arial", 12), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, pady=(10, 5))

window.mainloop()
