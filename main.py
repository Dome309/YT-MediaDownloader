import tkinter as tk
from gui import build_gui, center_window

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Media Downloader")
    icon_image = tk.PhotoImage(file="images/logo.png")
    root.iconphoto(True, icon_image)

    window_width = 900
    window_height = 500
    root.minsize(800, 400)
    root.configure(bg="white")
    build_gui(root, window_width, window_height)
    root.mainloop()
