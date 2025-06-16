import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp
import time
from dotenv import load_dotenv
import os

#loads in the hidden codes and keys for the api
load_dotenv()


def main():


    playlist_url = input('enter the youtube playlist: ')
    titles = yt_playlist_titles(playlist_url)

    sp = spotify_authentication()

    #users spotify id
    user_id= sp.current_user()['id']

    #users spotify name
    user_name= sp.current_user()['display_name']
    playlist_name = input(f'Hey {user_name}, What name would you like to give to your imported playlist? ')
    description = input('What kind of description would you like to give? ')

    playlist_id, new_playlist_link = playlist(sp, user_id, playlist_name, description)

    loading()

    playlist_music(sp, playlist_id, titles)
    print(f'Playlist {playlist_name} has been made')
    print(f"the given tracks have been added to {playlist_id} in {user_name}'s account :D")
    print(f'link: {new_playlist_link}')






#authenticating the api
def spotify_authentication():

    #using the .ev file to get out keys
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')


    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-public playlist-modify-private",
                                               open_browser=True))


#creating a playlist

def playlist(sp, user_id, playlist_name, description):
    playlist = sp.user_playlist_create(user_id, playlist_name, public=True, description=description)
    new_playlist_link= playlist['external_urls']['spotify']
    return playlist['id'], new_playlist_link


#adding music to the playlist

def playlist_music(sp, playlist_id, titles):
    track_uris = []

    for title in titles:
        results = sp.search(q=title, limit=1, type='track')
        if results['tracks']['items']:
            track_uris.append(results['tracks']['items'][0]['uri'])

    if track_uris:
        sp.playlist_add_items(playlist_id, track_uris)
    else:
        print("No tracks found to add.")





#getting the video titles from youtube

def yt_playlist_titles(playlist_url):
    ydl_opts = {'quiet': True, 'extract_flat': True,}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)

        titles = []
        for entry in playlist_info['entries']:
            titles.append(entry['title'])

        return titles


#creating a loading mechanic for nicer aesthetics


def loading():

    messages=['loading.', 'loading..', 'loading...', 'loading....', 'loading.....']

    for message in messages:
        print(message, end='\r')

        time.sleep(2)




if __name__ == '__main__':
    main()
