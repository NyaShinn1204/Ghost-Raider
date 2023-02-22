import tkinter as tk
root = tk.Tk()
root.title(u"Ghost Raider")
root.geometry("1300x750")
root.iconbitmap(default="ghost.ico")
root.configure(bg='grey13')

# 上の部分
uenolabel = tk.Label(background='#545454')
uenolabel.place(x=0, y=0, height=95, width=1300)

canvas = tk.Canvas(root,width = 1060, height = 90, bg = "white")
canvas.place(x=240, y=0)
rectangle = canvas.create_rectangle(0, -1, 1062, 91, outline = "gray", width = 1, fill = "#545454")

namelabel0 = tk.Label(background='#2C2C2C')
namelabel0.place(x=10, y=8, width=230, height=80)
namelabel1 = tk.Label(text='Ghost Raider', foreground='white', background='#2C2C2C', font=("Supernova",20,"bold"))
namelabel1.place(x=25, y=10)
namelabel2 = tk.Label(text='V2', foreground='white', background='#2C2C2C', font=("Supernova",20,"bold"))
namelabel2.place(x=95, y=50)


creditlabel0 = tk.Label(background='#2C2C2C')
creditlabel0.place(x=250, y=8, height=80, width=1055)
creditlabel1 = tk.Label(text='Created By cocoapc911', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
creditlabel1.place(x=270, y=20)
creditlabel2 = tk.Label(text='Discord: ここあ#0001', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
creditlabel2.place(x=280, y=45)
creditlabel3 = tk.Label(text='discord.gg/cocoapc911', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
creditlabel3.place(x=560, y=30)

# Spammer
canvas = tk.Canvas(root, bg="grey13", height=330, width=400)
canvas.place(x=15, y=130)
spammerlabel = tk.Label(text="Spammer",font=("Supernova",20,"bold"),foreground="#fff",bg="grey13")
spammerlabel.place(x=30, y=110)
serveridlabel = tk.Label(text="Server ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
serveridlabel.place(x=30, y=160)
serveridentry = tk.Entry()
serveridentry.place(x=30, y=185)
channelidlabel = tk.Label(text="Channel ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
channelidlabel.place(x=30, y=220)
channelidentry = tk.Entry()
channelidentry.place(x=30, y=245)

root.mainloop()