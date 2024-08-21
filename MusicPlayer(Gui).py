import tkinter as tk
from tkinter import filedialog
import customtkinter
from tkinter.ttk import Progressbar
import pygame
from PIL import Image, ImageTk
from threading import Thread
import time
import math

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

##### Tkinter setup ######
root = customtkinter.CTk()
root.title('Universal Media Player')
root.geometry('400x480')
root.configure(bg="#212121")
pygame.mixer.init()
##########################

list_of_media = []
n = 0

def load_media():
    global list_of_media
    media_files = filedialog.askopenfilenames(filetypes=[("Media Files", "*.mp3;*.wav;*.mp4;*.mkv;*.avi")])
    list_of_media.extend(media_files)
    if list_of_media:
        play_media()

def get_album_cover(media_name):
    try:
        image1 = Image.open('img/default_cover.jpg')
    except FileNotFoundError:
        # Handle the case where the image file is not found
        image1 = Image.new('RGB', (250, 250), color='grey')  # Create a grey placeholder
    image2 = image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)

    label1 = tk.Label(root, image=load, bg="#212121")
    label1.image = load
    label1.place(relx=.19, rely=.06)

    media_name_label = tk.Label(root, text=media_name, bg='#212121', fg='white')
    media_name_label.place(relx=.4, rely=.6)

def progress():
    if pygame.mixer.music.get_busy():
        media_length = pygame.mixer.Sound(list_of_media[n]).get_length()
        for _ in range(0, math.ceil(media_length)):
            time.sleep(0.4)
            progressbar.set(pygame.mixer.music.get_pos() / 1000)

def threading_func():
    t1 = Thread(target=progress)
    t1.start()

def play_media():
    threading_func()
    global n
    if n >= len(list_of_media):
        n = 0
    media_name = list_of_media[n]
    pygame.mixer.music.load(media_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)
    get_album_cover(media_name)
    n += 1

def skip_forward():
    global n
    n = (n + 1) % len(list_of_media)
    play_media()

def skip_back():
    global n
    n = (n - 1) % len(list_of_media)
    play_media()

def volume(value):
    pygame.mixer.music.set_volume(float(value))

def seek_forward():
    # This function doesn't work with pygame.mixer.music
    pass

def seek_backward():
    # This function doesn't work with pygame.mixer.music
    pass

# Buttons
load_button = customtkinter.CTkButton(master=root, text='Load Media', command=load_media, bg_color="#1DA756", fg_color="#212121")
load_button.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

play_button = customtkinter.CTkButton(master=root, text='Play', command=play_media, bg_color="#1DA756", fg_color="#212121")
play_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>>', command=skip_forward, width=50, bg_color="#1DA756", fg_color="#212121")
skip_f.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<<', command=skip_back, width=50, bg_color="#1DA756", fg_color="#212121")
skip_b.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

speed_slider = customtkinter.CTkSlider(master=root, from_=0.5, to=2.0, command=volume, width=150, bg_color="#1DA756", fg_color="#212121")
speed_slider.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

forward_button = customtkinter.CTkButton(master=root, text='+5s', command=seek_forward, width=50, bg_color="#1DA756", fg_color="#212121")
forward_button.place(relx=0.7, rely=0.85, anchor=tk.CENTER)

backward_button = customtkinter.CTkButton(master=root, text='-5s', command=seek_backward, width=50, bg_color="#1DA756", fg_color="#212121")
backward_button.place(relx=0.3, rely=0.85, anchor=tk.CENTER)

volume_slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210, bg_color="#1DA756", fg_color="#212121")
volume_slider.place(relx=0.5, rely=0.78, anchor=tk.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a', width=250)
progressbar.place(relx=.5, rely=.9, anchor=tk.CENTER)

root.mainloop()
