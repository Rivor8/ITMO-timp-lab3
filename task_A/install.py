import tkinter as tk
import tkinter.ttk as ttk
import time

master = tk.Tk()
master.title('Обновление Internet Explorer')
master.geometry('400x250+1000+300')

progress_bar = ttk.Progressbar(master, orient="horizontal", mode="determinate", maximum=100, value=0)
label_1 = tk.Label(master, text="Идёт установка подождите...")
progress_bar.pack(expand=True)
label_1.pack(expand=True)

while True:
    progress_bar['value'] += 2
    time.sleep(0.5)
    if progress_bar['value'] >= 100:
        master.destroy()
    master.update()
