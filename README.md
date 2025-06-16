
# YouTube to Spotify playlist converter

This project provides a Python-based tool to import a YouTube playlist into Spotify. By using the Spotify API and yt-dlp, this tool allows users to create a new playlist on their Spotify account, name it, add a description, and populate it with music from a given YouTube playlist

## Video Demo
<https://youtu.be/4mIzWjcfORA>


## Description

The YouTube to Spootify play list converter is a python based, command line application that lets the user import his/her YouTube playlist over to spotify

## Features
- YouTube Playlist Parsing, extracts the titles of all videos from a given YouTube playlist URL.
- Allows the user the user to import their existing YouTube playlist to Spotify
- Allows for good tracking, which means the program automatically makes the playlist exactly how the YouTube one was made
- Authenticates with the Spotify API using OAuth2 to allow the app to interact with a user's Spotify account.
- easy to use, all one has to do is put in any youtube playlist link
- Automated Spotify Playlist Creation with your own custom name and description
- Gives you a link to the created playlist
- The Loading Mechanism displays a neat little animation to enhance the user experience during the process


## Usage

- Run the main() function
- Enter the prompt asking you for a YouTube playlist
- Enter the prompt asking you to fill in the name and description

## Technologies used

- Python
- Spotipy
- yt_dlp library
- dotenv library
- os library
- time library


## Prerequisites

- Python 3.6 or higher
- A spotify developers account
- Spotipy
- yt_dlp
- dot env

## Set up

### run pip install for yp_dlp, dot env and spotipy

### spotify api
- go to the spotify developers dashboard
- create a new application
- obtain the spotify client id , client secret, and uri
- Add these credentials to a .env file in the root directory of the project

### run the script

- python project.py


### User Interaction:

- The program will prompt you to input a YouTube playlist URL.
- You will then be asked to name your new Spotify playlist and provide a description.
- The script will search for tracks from the YouTube playlist and add them to your newly created Spotify playlist.



## How It Works

- Extract YouTube Playlist Titles: The yt-dlp library is used to extract the titles of all videos in the given YouTube playlist URL. These titles are collected into a regular python list.

- Spotify Authentication: The script authenticates the user with the Spotify API using the Spotipy library and the OAuth2 protocol. This allows the script to interact with the user's Spotify account securely.

- Create Spotify Playlist: The script creates a new playlist on the user's Spotify account, using the user-provided name and description.

- Add Tracks to Spotify Playlist: The script then searches for each track from the YouTube playlist by title and adds the found tracks to the newly created Spotify playlist.

- Loading Mechanism: A loading animation is displayed to make the process feel more dynamic and aesthetic.
