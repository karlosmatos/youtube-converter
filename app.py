import os
import logging
import requests
import streamlit as st
import yt_dlp

def download_audio_from_youtube(url):
    """Download audio from YouTube video and return the file path."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info['title']
            ydl.download([url])
            return f"{title}.mp3"
    except Exception as e:
        st.error(f'An error occurred: {str(e)}. Please check the URL or try another video.')
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

def handle_video_download(youtube_url, progress_bar):
    """Handle video download and UI updates."""
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            title = info['title']
            thumbnail_url = info['thumbnail']
        
        progress_bar.progress(20)
        st.write(f'Video title: {title}')
        st.image(thumbnail_url, width=200)
        progress_bar.progress(50)
        downloaded_file = download_audio_from_youtube(youtube_url)
        progress_bar.progress(100)
        if downloaded_file:
            create_download_button_for_file(downloaded_file)
            st.success('Audio downloaded successfully!')
            progress_bar.empty()
    except Exception as e:
        st.error(f'An error occurred: {str(e)}. Please check the URL or try another video.')
        progress_bar.empty()

def main():
    """Main function to orchestrate the flow of the application."""
    logging.basicConfig(filename='user_activity.log', level=logging.INFO, 
                        format='%(asctime)s:%(levelname)s:%(message)s')
    youtube_url, submit_button = get_user_input()
    if submit_button:
        progress_bar = st.progress(0, text="Downloading audio...")
        handle_video_download(youtube_url, progress_bar)

if __name__ == "__main__":
    main()