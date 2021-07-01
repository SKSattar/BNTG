"""A video player class."""

import random
from .video_library import VideoLibrary
from .video_playlist import Playlist
playlists = []
play = {}
current = ""
currentID = ""
pause = False

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        for x in self._video_library.get_all_videos():
          print(x.title,"(",x.video_id,") [",x.tags,"]")

    def play_video(self, video_id):
        """Plays the video."""
        global current
        global currentID
        if self._video_library.get_video(video_id) == None:
            print("Cannot play video: Video does not exist")
        else:
            t = self._video_library.get_video(video_id).title
            currentID = video_id
            if current == "":
                print("Playing video:",t)
                current = t;
            else:
                print("Stopping video:",current)
                print("Playing video:",t)
                current = t;

    def stop_video(self):
        """Stops the current video."""
        global current
        global pause
        if current == "":
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:",current)
            current = "";
            pause = False;

    def play_random_video(self):
        """Plays a random video from the video library."""
        #need to add if no videos
        global current
        t = random.choice(self._video_library.get_all_videos())
        m = t.title
        if current == "":
            print("Playing video:",m)
            current = m;
        else:
            print("Stopping video:",current)
            print("Playing video:",m)
            current = m;

    def pause_video(self):
        """Pauses the current video."""
        global pause
        if pause == True:
            print("Video already paused:", current)
        else:
            if current == "":
                print("Cannot pause video: No video is currently playing")
            else:
                print("Pausing video:",current)
                pause = True;


    def continue_video(self):
        """Resumes playing the current video."""
        global pause
        if current == "":
            print("Cannot continue video: No video is currently playing")
        elif pause == False:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video:",current)
            pause = False;


    def show_playing(self):
        """Displays video currently playing."""
        if current == "":
                print("No video is currently playing")
        else:
            x = self._video_library.get_video(currentID).title
            y = self._video_library.get_video(currentID).tags
            if pause == True:
                print("Currently playing:",x,"(",currentID,") [",y,"] - PAUSED")
            else:
                print("Currently playing:",x,"(",currentID,") [",y,"]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name."""
        global playlists
        playlist_name = playlist_name.lower() 
        if playlist_name in playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            playlists.append(playlist_name)
            print("Successfully created new playlist:",playlist_name)



    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name."""
        global playlists
        global play
        playlist_name = playlist_name.lower() 
        if self._video_library.get_video(video_id) == None:
            print("Cannot add video to",playlist_name,": Video does not exist")
        elif playlist_name not in playlists:
            print("Cannot add video to",playlist_name,": Playlist does not exist")
        elif playlist_name in play and video_id in play.values():
            print("Cannot add video to",playlist_name,": Video already added")
        else:
            play[playlist_name]=video_id
            t = self._video_library.get_video(video_id).title
            print("Added video to", playlist_name,":",t)



    def show_all_playlists(self):
        """Display all playlists."""
        global playlists
        if len(playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for x in range(len(playlists)):
                print(playlists[x])


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name."""
        playlist_name = playlist_name.lower()
        print(play)
        if playlist_name not in playlists:
            print("Cannot show playlist",playlist_name,": Playlist does not exist")
        else:
            print("Showing playlist:",playlist_name)
            x = self._video_library.get_video(play[playlist_name]).title
            y = self._video_library.get_video(play[playlist_name]).tags
            print(x,"(",play[playlist_name],") [",y,"]")


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name."""
        playlist_name = playlist_name.lower()
        if playlist_name not in playlists:
            print("Cannot remove video from",playlist_name,": Playlist does not exist")
        elif self._video_library.get_video(video_id) == None:
            print("Cannot remove video from",playlist_name,": Video does not exist")
        elif video_id not in play.values():
            print("Cannot remove video from",playlist_name,": Video is not in playlist")
        elif playlist_name in play and video_id in play.values():
            t = self._video_library.get_video(video_id).title
            print("Removed video from",playlist_name,":",t)
            play.pop(video_id)


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name."""
        if playlist_name not in playlists:
            print("Cannot remove video from",playlist_name,": Playlist does not exist")
        else:
            play.clear()
            print("Successfully removed all videos from",playlist_name)


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in playlists:
            print("Cannot delete playlist",playlist_name,": Playlist does not exist")
        else:
            playlists.remove(playlist_name)
            print("Successfully removed all videos from",playlist_name)


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("Here are the results for :",search_term)
        search_term = search_term.lower()
        a = 1
        options = {}
        for x in self._video_library.get_all_videos():
          if search_term in x.title.lower():
              print(a,")",x.title,"(",x.video_id,") [",x.tags,"]")
              options[a] = x.video_id
              a = a+1
        if a == 1:
            print("No search results for",search_term)
        else:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            y = input()
            if y in options:
                v = options.get(y)
                print("Playing video:",self._video_library.get_video(v).title)
        
        

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("Here are the results for :",video_tag)
        a = 1
        options = {}
        for x in self._video_library.get_all_videos():
          if video_tag in x.tags:
              print(a,")",x.title,"(",x.video_id,") [",x.tags,"]")
              options[a] = x.video_id
              a = a+1
        if a == 1:
            print("No search results for",video_tag)
        else:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            y = input()
            if y in options:
                v = options.get(y)
                print("Playing video:",self._video_library.get_video(v).title)



    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        if self._video_library.get_video(video_id) == None:
            print("Cannot flag video: Video does not exist")
        elif flag_reason == "":
            print("Successfully flagged video:",self._video_library.get_video(video_id).title,"(reason: Not supplied)")
        else:
            print("Successfully flagged video:",self._video_library.get_video(video_id).title,"(reason:",flag_reason,")")


        

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        if self._video_library.get_video(video_id) == None:
            print("Cannot flag video: Video does not exist")
        else:
            print("Successfully removed flag from video:",video_id)
