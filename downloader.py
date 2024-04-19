from pytube import YouTube
import moviepy.editor as mp


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
            audio = yt.streams.filter(only_audio=True).first()
            if audio:
                audio_file_path = f"{save_path}/{yt.title}.mp3"
                audio.download(output_path=save_path)
                clip = mp.AudioFileClip(audio_file_path)
                clip.write_audiofile(audio_file_path)
                clip.close()
                status_label.config(text="Audio downloaded successfully")
            else:
                status_label.config(text="No audio stream available for the video.")
    except Exception as e:
        status_label.config(text=f"Error: {e}")
