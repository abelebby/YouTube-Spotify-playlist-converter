import unittest
from unittest.mock import patch, MagicMock
from project import playlist, yt_playlist_titles, loading


def test_playlist():
    with patch('project.spotify_authentication') as mock_spotify_auth:

        mock_spotify = MagicMock()
        mock_spotify_auth.return_value = mock_spotify
        mock_spotify.user_playlist_create.return_value = {
            'id': 'mock_playlist_id',
            'external_urls': {'spotify': 'https://open.spotify.com/playlist/mock_playlist_id'}}
        
        mock_spotify.current_user.return_value = {'id': 'mock_user_id'}


        result_id, result_link = playlist(mock_spotify, 'mock_user_id', 'Test Playlist', 'Test Description')


        mock_spotify.user_playlist_create.assert_called_once_with('mock_user_id', 'Test Playlist', public=True, description='Test Description')

        assert result_id == 'mock_playlist_id'
        assert result_link == 'https://open.spotify.com/playlist/mock_playlist_id'




def test_yt_playlist_titles():

    with patch('project.yt_dlp.YoutubeDL.extract_info') as mock_extract_info:
        mock_extract_info.return_value = {'entries': [{'title': 'Song 1'}, {'title': 'Song 2'}]}


        titles = yt_playlist_titles('test_playlist_url')
        assert titles == ['Song 1', 'Song 2']



def test_loading():
    with patch('time.sleep', return_value=None) as mock_sleep:

        loading()
        assert mock_sleep.call_count == 5


if __name__ == '__main__':
    main()
