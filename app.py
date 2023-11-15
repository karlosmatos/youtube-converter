import streamlit as st
from pytube import YouTube
import os

# Create a text input box
url = st.text_input('Enter your youtube video url:')

# Create a button
button = st.button('Submit')

# Action when button is pressed
if button:
    yt = YouTube(url)
    video = yt.streams.get_audio_only()
    video_title = yt.title
    downloaded_file = video.download(filename=video_title)
    new_file = f"{video_title}.mp3"
    os.rename(downloaded_file, new_file)
    with open(new_file, 'rb') as f:
        data = f.read()
    st.download_button(label='Download', data=data, file_name=new_file)
    os.remove(new_file)

