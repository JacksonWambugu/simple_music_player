import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas =tk.Tk()
canvas.title("Simple music PLayer")
canvas.geometry("600x800")
canvas.config(bg ='black')

rootpath ="C:\\Users\Public\Desktop\mp3"
patter= "*.mp3"
mixer.init()

def select():
    label.config(text = listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def playnext():
    next_song= listbox.curselection()
    next_song = next_song[0]+1
    next_song_name = listbox.get(next_song)
    label.config(text= next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def playprev():
    prev_song= listbox.curselection()
    prev_song = prev_song[0]-1
    prev_song_name = listbox.get(prev_song)
    label.config(text= prev_song_name)
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)

def pause_song():
    if(pausebutton["text"]=="pause"):
        mixer.music.pause()
        pausebutton["text"]="play"
    else:
        mixer.music.unpause()
        pausebutton["text"]="pause"




listbox=tk.Listbox(canvas,fg="cyan",bg="black",width=100,font=('ds-digital',16))
listbox.pack(padx=15,pady =15)
label = tk.Label(canvas,text='',bg='black',fg='yellow',font=('ds-digital',18))
label.pack(pady=15)
top = tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor='center')

prevbutton=tk.Button(canvas,text="prev",borderwidth='20',command=playprev)
prevbutton.pack(pady=15,in_=top,side='left')
stopbutton=tk.Button(canvas,text="stop",borderwidth='20',command=stop)
stopbutton.pack(pady=15,in_=top,side='left')
nextbutton=tk.Button(canvas,text="Next",borderwidth='20',command=playnext)
nextbutton.pack(pady=15,in_=top,side='left')
pausebutton=tk.Button(canvas,text="Pause",borderwidth='20',command=pause_song)
pausebutton.pack(pady=15,in_=top,side='left')
playbutton=tk.Button(canvas,text="Play",borderwidth='20',command=select)
playbutton.pack(pady=15,in_=top,side='left')


for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,patter):
        listbox.insert('end',filename)



canvas.mainloop()
