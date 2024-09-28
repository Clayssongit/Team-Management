import tkinter as tk
from tkinter import simpledialog, messagebox

teams = {}

def print_teams():
    team_list.delete(0, tk.END)
    for i, team in enumerate(teams.values()):
        team_list.insert(tk.END, f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

def add_team():
    team_name = simpledialog.askstring("Adicionar Time", "Digite o nome do time:")
    if team_name:
        teams[team_name] = {'name': team_name, 'players': []}
        print_teams()

def remove_team():
    selected = team_list.curselection()
    if selected:
        team_name = list(teams.keys())[selected[0]]
        del teams[team_name]
        print_teams()
    else:
        messagebox.showwarning("Remover Time", "Selecione um time para remover.")

def add_player():
    selected = team_list.curselection()
    if selected:
        team_name = list(teams.keys())[selected[0]]
        player_name = simpledialog.askstring("Adicionar Jogador", "Nome do jogador:")
        if player_name:
            teams[team_name]['players'].append(player_name)
            print_teams()
    else:
        messagebox.showwarning("Adicionar Jogador", "Selecione um time para adicionar um jogador.")

def remove_player():
    selected = team_list.curselection()
    if selected:
        team_name = list(teams.keys())[selected[0]]
        player_name = simpledialog.askstring("Remover Jogador", "Nome do jogador:")
        if player_name in teams[team_name]['players']:
            teams[team_name]['players'].remove(player_name)
            print_teams()
        else:
            messagebox.showwarning("Remover Jogador", "Jogador não encontrado no time.")
    else:
        messagebox.showwarning("Remover Jogador", "Selecione um time para remover um jogador.")

def list_players():
    selected = team_list.curselection()
    if selected:
        team_name = list(teams.keys())[selected[0]]
        players = teams[team_name]['players']
        messagebox.showinfo("Jogadores", f"Jogadores do {team_name}: {', '.join(players)}")
    else:
        messagebox.showwarning("Listar Jogadores", "Selecione um time para listar os jogadores.")

root = tk.Tk()
root.title("Gerenciamento de Times")

frame = tk.Frame(root)
frame.pack(pady=20)

team_list = tk.Listbox(frame, width=50, height=10)
team_list.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

team_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=team_list.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

add_team_button = tk.Button(button_frame, text="Adicionar Time", command=add_team)
add_team_button.grid(row=0, column=0, padx=10)

remove_team_button = tk.Button(button_frame, text="Remover Time", command=remove_team)
remove_team_button.grid(row=0, column=1, padx=10)

add_player_button = tk.Button(button_frame, text="Adicionar Jogador", command=add_player)
add_player_button.grid(row=1, column=0, padx=10)

remove_player_button = tk.Button(button_frame, text="Remover Jogador", command=remove_player)
remove_player_button.grid(row=1, column=1, padx=10)

list_players_button = tk.Button(button_frame, text="Listar Jogadores", command=list_players)
list_players_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()