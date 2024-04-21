import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from downloader import download_media
from tkinter import PhotoImage


def on_entry_click(url_entry):
    if url_entry.get() == "Enter the YouTube video URL":
        url_entry.delete(0, "end")
        url_entry.config(fg='black')


def on_focusout(url_entry):
    if not url_entry.get():
        url_entry.insert(0, "Enter the YouTube video URL")
        url_entry.config(fg='grey')


def browse_button_clicked(url_entry, format_choice, status_label):
    url = url_entry.get()
    save_directory = filedialog.askdirectory()
    if url and save_directory:
        download_media(url, save_directory, format_choice.get(), status_label)
    else:
        status_label.config(text="Please provide a YouTube URL and select a directory.")


def build_components():
    welcome_label = tk.Label(root, text="Welcome to YouTube Media Downloader", font=("Helvetica", 18),
                             background="white")
    welcome_label.pack(pady=20)

    description_label = tk.Label(root, text="Unlock the convenience of downloading either MP4 or MP3 "
                                            "files directly from YouTube links", font=14, background="white")
    description_label.pack(pady=(0, 40))

    url_frame = tk.Frame(root)
    url_frame.pack()

    url_entry = tk.Entry(url_frame, width=50, font=("Helvetica", 14), fg='grey')
    url_entry.insert(0, "Enter the YouTube video URL")
    url_entry.bind("<FocusIn>", lambda event: on_entry_click(url_entry))
    url_entry.bind("<FocusOut>", lambda event: on_focusout(url_entry))
    url_entry.pack(side=tk.LEFT, padx=0)

    format_choice = tk.StringVar()
    format_choice.set("mp4")

    format_menu = ttk.Combobox(url_frame, textvariable=format_choice, values=["mp4", "mp3"], width=5, state="readonly")
    format_menu.pack(side=tk.LEFT)

    browse_button = ttk.Button(root, text="Browse",
                               command=lambda: browse_button_clicked(url_entry, format_choice, status_label))
    browse_button.pack(pady=20)

    status_label = tk.Label(root, text="", background="white")
    status_label.pack()

    global image
    global image2
    global image3
    image = PhotoImage(file="images/circle1.png")
    image2 = PhotoImage(file="images/circle2.png")
    image3 = PhotoImage(file="images/circle3.png")

    image_frame = tk.Frame(root, background="white")
    image_frame.pack()

    image_label = tk.Label(image_frame, image=image, borderwidth=0, relief="flat", background="white")
    image_label.pack(side="left", pady=20)

    image_label2 = tk.Label(image_frame, image=image2, borderwidth=0, relief="flat", background="white")
    image_label2.pack(side="left", padx=200)

    image_label3 = tk.Label(image_frame, image=image3, borderwidth=0, relief="flat", background="white")
    image_label3.pack(side="left")

    description_frame = tk.Frame(root, background="white")
    description_frame.pack()

    circle1_label = tk.Label(description_frame, text="Paste a YouTube URL", font=14, background="white")
    circle1_label.pack(side="left", padx=10)

    circle2_label = tk.Label(description_frame, text="Select the desired format type", font=14, background="white")
    circle2_label.pack(side="left", padx=100)

    circle3_label = tk.Label(description_frame, text="Specify the save directory", font=14, background="white")
    circle3_label.pack(side="right")


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Media Downloader")
    window_width = 900
    window_height = 500
    root.minsize(600, 250)
    root.configure(bg="white")
    build_components()

    center_window(root, window_width, window_height)

    root.mainloop()
