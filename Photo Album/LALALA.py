from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("📸 My Photo Album")
window.geometry("450x500")
window.config(bg="#F3E8FF") 

title_label = Label(
    window,
    text="📸 My Photo Album ❤️",
    font=("Arial", 20, "bold"),
    fg="#FFFFFF",
    bg="#C8A2C8",  
    width=25
)
title_label.pack(pady=15)

image_file = Image.open("photo.jpeg")
image_file = image_file.resize((300, 200))

photo = ImageTk.PhotoImage(image_file)

image_label = Label(window, image=photo, bg="#F3E8FF")
image_label.pack(pady=10)

def show_reaction():
    messagebox.showinfo(
        "💖 Photo Reaction",
        "😍 This is a beautiful memory! ✨"
    )

def open_photo_details():
    details_window = Toplevel(window)
    details_window.title("🖼️ Photo Details")
    details_window.geometry("350x250")
    details_window.config(bg="#FFF1E6") 

    heading = Label(
        details_window,
        text="📷 Photo Details",
        font=("Arial", 16, "bold"),
        bg="#FFF1E6",
        fg="#9B6B9E"
    )
    heading.pack(pady=15)

    details = Label(
        details_window,
        text="📝 Photo Name: My Favourite Memory\n"
             "📂 Category: Personal Album\n"
             "❤️ Description: A special photo saved in my album.",
        font=("Arial", 11),
        bg="#FFF1E6",
        fg="#66546A",
        justify="left"
    )
    details.pack(pady=10)

    close_button = Button(
        details_window,
        text="❌ Close",
        bg="#D8B4E2",
        fg="#FFFFFF",
        activebackground="#C8A2C8",
        command=details_window.destroy
    )
    close_button.pack(pady=15)

reaction_button = Button(
    window,
    text="💖 React to Photo",
    font=("Arial", 12, "bold"),
    bg="#BDE0FE", 
    fg="#4A5270",
    activebackground="#A2D2FF",
    command=show_reaction
)
reaction_button.pack(pady=10)

details_button = Button(
    window,
    text="🖼️ View Photo Details",
    font=("Arial", 12, "bold"),
    bg="#CDEAC0", 
    fg="#49634A",
    activebackground="#B7DDB0",
    command=open_photo_details
)
details_button.pack(pady=10)

window.mainloop()