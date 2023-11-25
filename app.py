import os
import logging
import requests
import streamlit as st
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def download_audio_from_youtube(url):
    """Download audio from YouTube video and return the file path."""
    try:
        video = YouTube(url)
        audio_stream = video.streams.get_audio_only()
        title = video.title
        downloaded_file = audio_stream.download(filename=title)
        renamed_file = f"{title}.mp3"
        os.rename(downloaded_file, renamed_file)
        return renamed_file
    except VideoUnavailable:
        st.error('The video is not available. This could be due to region restrictions or invalid URL. Please check URL or try another video.')
        return None

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

def log_user_activity(youtube_url):
    """Log user activity."""
    user_ip = requests.get('https://api.ipify.org').text
    logging.info(f'User with IP {user_ip} submitted URL: {youtube_url}')

def handle_video_download(youtube_url, progress_bar):
    """Handle video download and UI updates."""
    video = YouTube(youtube_url)
    progress_bar.progress(20)
    st.write(f'Video title: {video.title}')
    st.image(video.thumbnail_url, width=200)
    progress_bar.progress(50)
    downloaded_file = download_audio_from_youtube(youtube_url)
    progress_bar.progress(100)
    if downloaded_file:
        create_download_button_for_file(downloaded_file)
        st.success('Audio downloaded successfully!')
        progress_bar.empty()

def main():
    """Main function to orchestrate the flow of the application."""
    logging.basicConfig(filename='user_activity.log', level=logging.INFO, 
                        format='%(asctime)s:%(levelname)s:%(message)s')
    youtube_url, submit_button = get_user_input()
    if submit_button:
        progress_bar = st.progress(0, text="Downloading audio...")
        log_user_activity(youtube_url)
        handle_video_download(youtube_url, progress_bar)

if __name__ == "__main__":
    main()