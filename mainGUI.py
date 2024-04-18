import tkinter as tk
from tkinter import filedialog
from downloader import download_video


def browse_button_clicked(url_entry, status_label):
    url = url_entry.get()
    save_directory = filedialog.askdirectory()
    if url and save_directory:
        download_video(url, save_directory, status_label)
    else:
        status_label.config(text="Please provide a YouTube URL and select a directory")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Video Downloader")

    root.geometry("600x300")

    url_label = tk.Label(root, text="Enter the YouTube video URL:")
    url_label.pack()

    url_entry = tk.Entry(root, width=50)
    url_entry.pack()

    browse_button = tk.Button(root, text="Browse", command=lambda: browse_button_clicked(url_entry, status_label))
    browse_button.pack()

    status_label = tk.Label(root, text="")
    status_label.pack()

    root.mainloop()
