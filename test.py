import tkinter as tk
from tkinter import ttk, messagebox
import datetime as dt

class MahjongCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Mahjong Calculator")
        self.root.geometry("400x600")

        self.players = []
        self.scores = [0, 0, 0, 0]
        self.round_no = 1
        self.taino = 1.0
        self.start_time = dt.datetime.now()

        self.setup_player_input()

    def setup_player_input(self):
        self.clear_window()

        tk.Label(self.root, text="Enter Player Names:").pack(pady=10)
        self.name_entries = [tk.Entry(self.root) for _ in range(4)]
        for entry in self.name_entries:
            entry.pack()

        tk.Label(self.root, text="How much is one tai?").pack(pady=10)
        self.taino_entry = tk.Entry(self.root)
        self.taino_entry.pack()

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=20)

    def start_game(self):
        self.players = [e.get() or f"Player {i+1}" for i, e in enumerate(self.name_entries)]
        try:
            self.taino = float(self.taino_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Tai must be a number.")
            return
        self.setup_round_ui()

    def setup_round_ui(self):
        self.clear_window()

        self.root.configure(bg="#f7f7f7")  # Soft background

        title_font = ("Helvetica", 16, "bold")
        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 12)

        self.round_label = tk.Label(self.root, text=f"Round {self.round_no}", font=title_font, bg="#f7f7f7")
        self.round_label.pack(pady=(20, 10))

        form_frame = tk.Frame(self.root, bg="#f7f7f7")
        form_frame.pack(pady=5)

        # Winner
        winner_row = tk.Frame(form_frame, bg="#f7f7f7")
        winner_row.pack(pady=5)
        tk.Label(winner_row, text="Winner:", font=label_font, bg="#f7f7f7").pack(side="left", padx=10)
        self.winner_var = tk.StringVar()
        self.winner_menu = ttk.Combobox(winner_row, textvariable=self.winner_var, values=self.players, state="readonly", font=entry_font, width=22)
        self.winner_menu.set("Select Winner")
        self.winner_menu.pack(side="left")

        # Loser
        loser_row = tk.Frame(form_frame, bg="#f7f7f7")
        loser_row.pack(pady=5)
        tk.Label(loser_row, text="Loser / Zimo:", font=label_font, bg="#f7f7f7").pack(side="left", padx=10)
        self.loser_var = tk.StringVar()
        self.loser_menu = ttk.Combobox(loser_row, textvariable=self.loser_var, values=self.players + ["Zimo"], state="readonly", font=entry_font, width=22)
        self.loser_menu.set("Select Loser or Zimo")
        self.loser_menu.pack(side="left")

        # Tai input
        tai_row = tk.Frame(form_frame, bg="#f7f7f7")
        tai_row.pack(pady=10)
        tk.Label(tai_row, text="Tai:", font=label_font, bg="#f7f7f7").pack(side="left", padx=10)
        self.tai_entry = tk.Entry(tai_row, font=entry_font, width=5)
        self.tai_entry.insert(0, "1")
        self.tai_entry.pack(side="left")

        # Bonus section
        tk.Label(self.root, text="Flower/Kang Bonuses", font=label_font, bg="#f7f7f7").pack(pady=(15, 5))
        self.bonus_entries = []
        bonus_frame = tk.Frame(self.root, bg="#f7f7f7")
        bonus_frame.pack()
        for i, player in enumerate(self.players):
            row = tk.Frame(bonus_frame, bg="#f7f7f7")
            row.pack(pady=2)
            tk.Label(row, text=f"{player}:", font=label_font, width=10, anchor="e", bg="#f7f7f7").pack(side="left", padx=5)
            entry = tk.Entry(row, font=entry_font, width=5)
            entry.insert(0, "0")
            entry.pack(side="left")
            self.bonus_entries.append(entry)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f7f7f7")
        button_frame.pack(pady=15)
        tk.Button(button_frame, text="Submit Round", font=label_font, command=self.submit_round, width=18).pack(side="left", padx=10)
        tk.Button(button_frame, text="End Game", font=label_font, command=self.end_game, width=18).pack(side="left", padx=10)

        # Score display
        self.score_display = tk.Label(self.root, text="", font=("Courier", 12), bg="#f7f7f7", justify="left")
        self.score_display.pack(pady=10)

        self.update_score_display()


    def submit_round(self):
        winner = self.winner_var.get()
        loser = self.loser_var.get()
        try:
            tai = int(self.tai_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Tai must be an integer.")
            return

        if winner not in self.players or loser not in self.players + ["Zimo"]:
            messagebox.showerror("Input Error", "Select valid players.")
            return

        if winner == loser:
            messagebox.showerror("Input Error", "Winner and loser can't be the same.")
            return

        winner_idx = self.players.index(winner)

        if loser == "Zimo":
            for i in range(4):
                if i != winner_idx:
                    self.scores[i] -= tai * 2
            self.scores[winner_idx] += tai * 6
        else:
            loser_idx = self.players.index(loser)
            self.scores[loser_idx] -= tai * 2
            for i in range(4):
                if i != loser_idx and i != winner_idx:
                    self.scores[i] -= tai
            self.scores[winner_idx] += tai * 4

        # Flower/Kang bonus points
        for i, entry in enumerate(self.bonus_entries):
            try:
                bonus = int(entry.get())
            except ValueError:
                bonus = 0
            self.scores[i] += bonus * 6
            for j in range(4):
                if j != i:
                    self.scores[j] -= bonus * 2

        # Reset bonus fields
        for entry in self.bonus_entries:
            entry.delete(0, tk.END)
            entry.insert(0, "0")

        self.round_no += 1
        self.round_label.config(text=f"Round {self.round_no}")
        self.winner_var.set("Select Winner")
        self.loser_var.set("Select Loser or Zimo")
        self.tai_entry.delete(0, tk.END)
        self.update_score_display()

    def update_score_display(self):
        text = "\n".join(
            f"{player}: ${score * self.taino:.2f}"
            for player, score in zip(self.players, self.scores)
        )
        self.score_display.config(text=text)

    def end_game(self):
        end_time = dt.datetime.now()
        duration = end_time - self.start_time
        summary = f"Game ended after {self.round_no - 1} rounds, duration: {duration}."

        with open("mahjong.txt", "a") as f:
            timestamp = end_time.strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"{self.scores} {self.players} {timestamp}\n")

        messagebox.showinfo("Game Summary", summary)
        self.root.quit()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MahjongCalculator(root)
    root.mainloop()
