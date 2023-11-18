# Ad-free YouTube Video Converter and MP3 Downloader

https://github.com/karlosmatos/youtube_converter/assets/105454484/f61f6185-5a69-489b-88b7-35a4b90175e7


## Overview

This application provides a user-friendly interface for converting YouTube videos to MP3 format without ads. It is built using the Streamlit framework and utilizes the pytube module for handling YouTube video interactions. The entire codebase is organized in the `app.py` file.

## Features

- Ad-free YouTube video conversion to MP3.
- Streamlit-based user interface for ease of use.
- Leveraging the pytube module for seamless YouTube interactions.

## Usage

### Cloud

The application is publicly available on Hugging Face Spaces. You can access it [here](https://huggingface.co/spaces/karelmaly/youtubeconverter).

### Locally

1. Clone the repository:

   ```
   git clone https://github.com/your-username/ad-free-youtube-converter.git
2. Navigate to the project directory:
   ```
   cd youtube_converter
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
4. Run the application:
   ```
   python -m streamlit run app.py
## GitHub Actions and Deployment
The project is configured with GitHub Actions to synchronize with the Hugging Face space repository and automatically deploy from the main branch.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENCE) file for details.
