import tkinter as tk
from tkinter import filedialog
from downloader import download_media


def browse_button_clicked(url_entry, format_choice, status_label):
    url = url_entry.get()
    save_directory = filedialog.askdirectory()
    if url and save_directory:
        download_media(url, save_directory, format_choice.get(), status_label)
    else:
        status_label.config(text="Please provide a YouTube URL and select a directory.")


def build_components():
    url_label = tk.Label(root, text="Enter the YouTube video URL:")
    url_label.pack()

    url_entry = tk.Entry(root, width=50)
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
    root.geometry("600x300")

    build_components()

    root.mainloop()
