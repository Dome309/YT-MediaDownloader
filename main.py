from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_resolution_stream = streams.get_highest_resolution()
        highest_resolution_stream.download(output_path=save_path)
        print("Video downloaded successfully")
    except Exception as e:
        print(e)


def open_file_folder():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    #root.withdraw()

    video_url = input("Enter a youtube url: ")
    save_directory = open_file_folder()

    if save_directory:
        print("Starting download...")
        download_video(video_url, save_directory)
    else:
        print("Invalid save location")
