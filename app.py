import streamlit as st
from pytube import YouTube
import os

# Create a text input box for YouTube video URL
youtube_url = st.text_input('Enter your YouTube video URL:')

# Create a submit button
submit_button = st.button('Submit')

# Define action when submit button is pressed
if submit_button:
    # Initialize YouTube object with provided URL
    youtube_video = YouTube(youtube_url)
    
    # Get audio stream of the video
    audio_stream = youtube_video.streams.get_audio_only()
    
    # Get video title
    video_title = youtube_video.title
    
    # Download the audio stream and rename it
    downloaded_file = audio_stream.download(filename=video_title)
    renamed_file = f"{video_title}.mp3"
    os.rename(downloaded_file, renamed_file)
    
    # Read the downloaded file and provide a download button
    with open(renamed_file, 'rb') as file:
        file_data = file.read()
    st.download_button(label='Download', data=file_data, file_name=renamed_file)
    
    # Remove the downloaded file after providing download button
    os.remove(renamed_file)
