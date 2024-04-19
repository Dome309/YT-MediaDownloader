import tkinter as tk
from tkinter import filedialog
from downloader import download_media


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
    welcome_label = tk.Label(root, text="Welcome to YouTube Media Downloader", font=("Helvetica", 18))
    welcome_label.pack(pady=20)

    description_label = tk.Label(root, text="To begin, please paste a YouTube URL, select the desired format type, "
                                            "and specify the save directory", font=14)
    description_label.pack(pady=(0, 20))

    url_entry = tk.Entry(root, width=50, fg='grey')
    url_entry.insert(0, "Enter the YouTube video URL")
    url_entry.bind("<FocusIn>", lambda event: on_entry_click(url_entry))
    url_entry.bind("<FocusOut>", lambda event: on_focusout(url_entry))
    url_entry.pack()

    format_choice = tk.StringVar()
    format_choice.set("mp4")

    mp4_radio = tk.Radiobutton(root, text="MP4", variable=format_choice, value="mp4")
    mp4_radio.pack()

    mp3_radio = tk.Radiobutton(root, text="MP3", variable=format_choice, value="mp3")
    mp3_radio.pack()

    browse_button = tk.Button(root, text="Browse",
                              command=lambda: browse_button_clicked(url_entry, format_choice, status_label))
    browse_button.pack()

    status_label = tk.Label(root, text="")
    status_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Media Downloader")
    root.minsize(800, 400)

    build_components()

    root.mainloop()
