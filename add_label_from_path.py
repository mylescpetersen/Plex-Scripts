#!/usr/bin/python3
from plexapi.server import PlexServer
import re

# ----------------------------------------------------------------------------------------------------------------------------
# Plex script to add a specified sharing label to each show & movie whose path contains an inputted regex
# ----------------------------------------------------------------------------------------------------------------------------

def main():

    # --- Edit these ---
    plexURL = 'http://<local-plex-ip>:32400'
    plexToken = '<plex-token>'
    # A list of library names (strings) to search
    libraries = ["Movies", "TV Shows"]
    # The sharing label to add to each Show/Movie 
    label_to_add = "<label to add to each show/movie>"
    # Regex that will search against each Show/Movie's path
    path_search_regex = "<regex to search filepaths for>"

    plex = PlexServer(plexURL, plexToken)

    # Updated by getMediaFromPath, List of Videos (Shows/Movies) to add the sharing tag to
    videos = []

    # Updates videos list
    def getMediaFromPath(library, videos=videos):

        for video in plex.library.section(library).search():

            # Succeeds if a Movie library
            try:
                # Gets path of the movie file
                file_path = video.media[0].parts[0].file

            # Throws if a TV Show library   
            except AttributeError:

                # Gets path of TV Show folder
                file_path = video.locations[0]

            # Regex search the path of each show/movie
            if re.search(path_search_regex, file_path):
                videos.append(video)

    # Searches all libraries in the libraries list for shows/movies matching the desired path search'
    for library in libraries:
        getMediaFromPath(library)

    # Add the sharing label to each item
    for v in videos:
        v.addLabel(label_to_add)
        
        # Print each affected movies, shows
        print("%s - %s" % (v.title, v.type)
    
    
if __name__ == "__main__":
    main()



