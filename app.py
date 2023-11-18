import os
import streamlit as st
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def download_audio_from_youtube(url):
    """Download audio from YouTube video and return the file path."""
    try:
        video = YouTube(url)
        progress_bar = st.progress(0, text="Downloading audio...")

        audio_stream = get_audio_stream(video, progress_bar)
        title = display_video_info(video, progress_bar)

        downloaded_file = download_audio_file(audio_stream, title, progress_bar)
        renamed_file = rename_downloaded_file(downloaded_file, title)

        progress_bar.empty()
        st.success('Audio downloaded successfully!')

        return renamed_file
    
    except VideoUnavailable:
        st.error('The video is not available. This could be due to region restrictions or invalid URL. Please check URL or try another video.')
        return None

def get_audio_stream(video, progress_bar):
    """Get the audio stream from the video and update the progress bar."""
    audio_stream = video.streams.get_audio_only()
    progress_bar.progress(20)
    return audio_stream

def display_video_info(video, progress_bar):
    """Display the video title and thumbnail, and update the progress bar."""
    title = video.title
    st.write(f'Video title: {title}')  # Print the video title in Streamlit
    st.image(video.thumbnail_url, width=200)  # Print the video thumbnail in Streamlit
    progress_bar.progress(50)
    return title

def download_audio_file(audio_stream, title, progress_bar):
    """Download the audio file and update the progress bar."""
    downloaded_file = audio_stream.download(filename=title)
    progress_bar.progress(100)
    return downloaded_file

def rename_downloaded_file(downloaded_file, title):
    """Rename the downloaded file to its title."""
    renamed_file = f"{title}.mp3"
    os.rename(downloaded_file, renamed_file)
    return renamed_file

def create_download_button_for_file(file_path):
    """Create a download button for the file and remove the file after download."""
    with open(file_path, 'rb') as file:
        file_data = file.read()

    st.download_button(label='Download', data=file_data, file_name=file_path)
    os.remove(file_path)

def get_user_input():
    """Get YouTube URL from user input."""
    youtube_url = st.text_input('Enter your YouTube video URL:')
    submit_button = st.button('Submit')
    return youtube_url, submit_button

def process_user_input(youtube_url, submit_button):
    """Process user input and download audio from YouTube."""
    if submit_button:
        downloaded_file = download_audio_from_youtube(youtube_url)
        if downloaded_file:
            create_download_button_for_file(downloaded_file)

def main():
    """Main function to orchestrate the flow of the application."""
    youtube_url, submit_button = get_user_input()
    process_user_input(youtube_url, submit_button)

if __name__ == "__main__":
    main()