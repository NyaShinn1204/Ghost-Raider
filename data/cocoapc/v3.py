import tkinter as tk
import tkinter.messagebox as tmsg
import tkinter.ttk as ttk
root = tk.Tk()
root.title(u"Ghost Raider")
root.geometry("1280x720")
root.iconbitmap(default="ghost.ico")
root.resizable(0,0)
root.configure(bg='grey13')
# 上の部分
 # nm = name
 # cd = credits
toplabel = tk.Label(background='#545454')
toplabel.place(x=0, y=0, height=95, width=1300)
canvas = tk.Canvas(root,width = 1060, height = 90, bg = "white")
canvas.place(x=240, y=0)
rectangle = canvas.create_rectangle(0, -1, 1062, 91, outline = "gray", width = 1, fill = "#545454")
nmlabel0 = tk.Label(background='#2C2C2C')
nmlabel0.place(x=10, y=8, width=230, height=80)
nmlabel1 = tk.Label(text='Ghost Raider', foreground='white', background='#2C2C2C', font=("Supernova",20,"bold"))
nmlabel1.place(x=25, y=10)
nmlabel2 = tk.Label(text='V3', foreground='white', background='#2C2C2C', font=("Supernova",20,"bold"))
nmlabel2.place(x=95, y=50)
cdlabel0 = tk.Label(background='#2C2C2C')
cdlabel0.place(x=250, y=8, height=80, width=1020) #1055
cdlabel1 = tk.Label(text='Created By cocoapc911', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
cdlabel1.place(x=270, y=20)
cdlabel2 = tk.Label(text='Discord: ここあ#0001', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
cdlabel2.place(x=280, y=45)
cdlabel3 = tk.Label(text='discord.gg/CvCwYKxZ', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
cdlabel3.place(x=560, y=30)
# Spammer
frame = tk.Frame(root, width=1165, height=540)
frame.place(x=20, y=115)
frame.configure(bg="grey13")#grey13 ##fff
canvas = tk.Canvas(frame, bg="grey13", height=365, width=450)
canvas.place(x=0, y=15)




root.mainloop()