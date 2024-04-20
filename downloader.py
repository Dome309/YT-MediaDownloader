from pytube import YouTube
import moviepy.editor as mp
import os


def download_media(url, save_path, format_choice, status_label):
    try:
        yt = YouTube(url)
        if format_choice == "mp4":
            stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
            if stream:
                stream.download(output_path=save_path)
                status_label.config(text="Video downloaded successfully")
            else:
                status_label.config(text="No progressive stream available for the video.")
        elif format_choice == "mp3":
            video_file_path = f"{save_path}/{yt.title}.mp4"
            video_stream = yt.streams.filter(file_extension="mp4").first()
            video_stream.download(output_path=save_path)
            video_clip = mp.VideoFileClip(video_file_path)
            audio_clip = video_clip.audio
            audio_file_path = f"{save_path}/{yt.title}.mp3"
            audio_clip.write_audiofile(audio_file_path)
            video_clip.close()
            audio_clip.close()
            os.remove(video_file_path)
            status_label.config(text="Audio downloaded successfully")
    except Exception as e:
        status_label.config(text=f"Error: {e}")
