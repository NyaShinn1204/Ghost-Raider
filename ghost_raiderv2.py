import tkinter as tk
import tkinter.messagebox as tmsg
import tkinter.ttk as ttk
import random
import requests
import threading
import time
import discum as discum
from concurrent.futures import ThreadPoolExecutor
root = tk.Tk()
root.title(u"Ghost Raider")
root.geometry("1300x750")
root.iconbitmap(default="ghost.ico")
root.configure(bg='grey13')
    
def start_spam():
    print("Start Spam")    
              
def stop_spam():
    print("Stop Spam") 
# 上の部分
uenolabel = tk.Label(background='#545454')
uenolabel.place(x=0, y=0, height=95, width=1300)
canvas = tk.Canvas(root,width = 1060, height = 90, bg = "white")
canvas.place(x=240, y=0)
rectangle = canvas.create_rectangle(0, -1, 1062, 91, outline = "gray", width = 1, fill = "#545454")
nmlabel0 = tk.Label(background='#2C2C2C')
nmlabel0.place(x=10, y=8, width=230, height=80)
nmlabel1 = tk.Label(text='Ghost Raider', foreground='white', background='#2C2C2C', font=("Supernova",20,"bold"))
nmlabel1.place(x=25, y=10)
nmlabel2 = tk.Label(text='V2', foreground='white', background='#2C2C2C', font=("Supernova",20,"bold"))
nmlabel2.place(x=95, y=50)
cdlabel0 = tk.Label(background='#2C2C2C')
cdlabel0.place(x=250, y=8, height=80, width=1055)
cdlabel1 = tk.Label(text='Created By cocoapc911', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
cdlabel1.place(x=270, y=20)
cdlabel2 = tk.Label(text='Discord: ここあ#0001', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
cdlabel2.place(x=280, y=45)
cdlabel3 = tk.Label(text='discord.gg/cocoapc911', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
cdlabel3.place(x=560, y=30)

# Spammer
canvas = tk.Canvas(root, bg="grey13", height=330, width=400)
canvas.place(x=15, y=130)
spamlabel = tk.Label(text="Spammer",font=("Supernova",20,"bold"),foreground="#fff",bg="grey13")
spamlabel.place(x=30, y=110)
svidlabel = tk.Label(text="Server ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
svidlabel.place(x=30, y=160)
svidentry = tk.Entry(width=25)
svidentry.place(x=30, y=185)
chidlabel = tk.Label(text="Channel ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
chidlabel.place(x=30, y=220)
chidentry = tk.Entry(width=25)
chidentry.place(x=30, y=245)
allch = tk.Checkbutton(text="AllChannel",bg="#7c64e4",height=0, width=17)
allch.place(x=30, y=275)
allmt = tk.Checkbutton(text="AllMention",bg="#7c64e4",height=0, width=17)
allmt.place(x=30, y=310)
smmelabel = tk.Label(text="Spam Text",font=("Supernova",10,"bold"),foreground="#fff",bg="grey13")
smmelabel.place(x=250, y=140)
#scroll_Y = tk.Scrollbar(orient='vertical')
#tex = tk.Text(background='white',yscrollcommand=scroll_Y.set)
#tex.place(x=190,y=170,width=200,height=200)
#scroll_Y['command'] = tex.yview
#scroll_Y.place( x = 390, y = 170, height = 200 )
scroll_Y = tk.Scrollbar( orient = 'vertical' )
metext = tk.Text(width=50, height=10)
metext.place(x=190,y=170,width=200,height=200)
scroll_Y[ 'command' ] = metext.yview
scroll_Y.place( x = 390, y = 170, height = 200 )
stsmbt = tk.Button(text="Start Spam",foreground='black', background='#88CEEB', command=start_spam)
stsmbt.place(x=40,y=400,width=150,height=40)
wismbt = tk.Button(text="Stop Spam",foreground='black', background='#88CEEB', command=stop_spam)
wismbt.place(x=230,y=400,width=150,height=40)

# Option
root.mainloop()