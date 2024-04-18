from pytube import YouTube


def download_video(url, save_path, status_label):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        if stream:
            stream.download(output_path=save_path)
            status_label.config(text="Video downloaded successfully")
        else:
            status_label.config(text="No progressive stream available for the video.")
    except Exception as e:
        status_label.config(text=f"Error: {e}")
