import os
import streamlit as st
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def download_audio_from_youtube(url):
    try:
        video = YouTube(url)
        audio_stream = video.streams.get_audio_only()
        title = video.title
        downloaded_file = audio_stream.download(filename=title)
        renamed_file = f"{title}.mp3"
        os.rename(downloaded_file, renamed_file)
        return renamed_file
    
    except VideoUnavailable:
        st.error('The video is not available. This could be due to region restrictions. Please try another video.')
        return None


def create_download_button_for_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    st.download_button(label='Download', data=file_data, file_name=file_path)
    os.remove(file_path)


def main():
    youtube_url = st.text_input('Enter your YouTube video URL:')
    submit_button = st.button('Submit')

    if submit_button:
        downloaded_file = download_audio_from_youtube(youtube_url)

        if downloaded_file:
            create_download_button_for_file(downloaded_file)


if __name__ == "__main__":
    main()