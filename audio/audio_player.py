from tkinter import*
import pygame
import os

root = Tk()
root.title("Audio Player")
root.geometry("300x200")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu = menubar)

organise_menu = Menu(menubar)
organise_menu.add_command(label="Select Folder")

songlist = Listbox(root, bg="black", fg = "white", width = 50, height= 10)
songlist.pack()

play_btn_image = PhotoImage(file = 'image\\play.png')
pause_btn_image = PhotoImage(file = 'image\\pause.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image = play_btn_image, borderwidth=0)
pause_btn = Button(control_frame, image = pause_btn_image, borderwidth=0)

play_btn.grid(row = 0, column = 1, padx= 7, pady = 10)
pause_btn.grid(row = 0, column = 2, padx= 7, pady = 10)

root.mainloop()