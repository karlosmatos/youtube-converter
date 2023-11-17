import os
import streamlit as st
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def download_audio_from_youtube(url):
    """Download audio from YouTube video and return the file path."""
    try:
        video = YouTube(url)
        progress_text = "Downloading audio..."
        progress_number = 0
        progress_bar = st.progress(progress_number, text=progress_text)

        audio_stream = video.streams.get_audio_only()
        progress_bar.progress(progress_number + 20, text=progress_text)

        title = video.title
        photo_url = video.thumbnail_url
        st.write(f'Video title: {title}')  # Print the video title in Streamlit
        st.image(photo_url, width=200)  # Print the video thumbnail in Streamlit
        progress_bar.progress(progress_number + 30, text=progress_text)

        downloaded_file = audio_stream.download(filename=title)
        progress_bar.progress(progress_number + 100, text=progress_text)

        renamed_file = f"{title}.mp3"
        os.rename(downloaded_file, renamed_file)
        progress_bar.empty()
        st.success('Audio downloaded successfully!')

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