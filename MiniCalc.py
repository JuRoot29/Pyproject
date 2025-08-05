import tkinter as tk
from tkinter import ttk
from math import sqrt

# === Fonctions utiles ===
def puissance(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * puissance(a, n - 1)
    else:
        return 1 / puissance(a, -n)

def pgcdrec(a, b):
    if b == 0:
        return a
    return pgcdrec(b, a % b)

def racine(a):
    if a>=0:
        return a**(1/2)
    else:
        return complex(0, (-a)**(1/2))

# === Interface ===
def calculer():
    op = operation.get()
    try:
        a = float(entry1.get())
        b = float(entry2.get()) if entry2.winfo_ismapped() else None
        
        if op == "Puissance":
            res = puissance(a, int(b))
        elif op == "PGCD":
            res = pgcdrec(int(a), int(b))
        elif op == "Racine":
            res = racine(a)
        else:
            res = "Opération non reconnue"
        
        result_var.set(f"Résultat : {res}")
    except Exception as e:
        result_var.set(f"Erreur : {e}")

def afficher_champs(event):
    op = operation.get()
    if op in ["Puissance", "PGCD"]:
        entry2.grid()
        label2.grid()
        label1.config(text="a :")
        label2.config(text="b :")
    elif op == "Racine":
        entry2.grid_remove()
        label2.grid_remove()
        label1.config(text="a :")

# === Fenêtre principale ===
fenetre = tk.Tk()
fenetre.title("Mini Calculatrice")
fenetre.geometry("400x250")

operation = ttk.Combobox(fenetre, values=["Puissance", "PGCD", "Racine"])
operation.bind("<<ComboboxSelected>>", afficher_champs)
operation.grid(row=0, column=1, padx=10, pady=10)
ttk.Label(fenetre, text="Opération :").grid(row=0, column=0)

label1 = ttk.Label(fenetre, text="a :")
label1.grid(row=1, column=0)
entry1 = ttk.Entry(fenetre)
entry1.grid(row=1, column=1)

label2 = ttk.Label(fenetre, text="b :")
label2.grid(row=2, column=0)
entry2 = ttk.Entry(fenetre)
entry2.grid(row=2, column=1)

ttk.Button(fenetre, text="Calculer", command=calculer).grid(row=3, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(fenetre, textvariable=result_var, foreground="blue")
result_label.grid(row=4, column=0, columnspan=2)

fenetre.mainloop()
