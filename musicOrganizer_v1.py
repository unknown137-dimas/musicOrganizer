from tinytag import TinyTag
from os import chdir, listdir, mkdir
from os.path import isfile, isdir
import shutil

# Locate folder, If not found create new folder
def dirSearch(q,p='.'):
    chdir(p)
    musicDir = [d for d in listdir() if isdir(d) and d == q]
    if len(musicDir) == 0:
        mkdir(q)
    else:
        pass

# Replace special characters
def charReplace(t):
    special_chars = ['/','*',':','?','"','<','>','|']
    for s in special_chars:
        if s in t:
            t = t.replace(s,'-')
    return t

if __name__ == "__main__":
    # Set working directory to musicPath
    musicPath = 'D:/Output'
    chdir(musicPath)
    musicFiles = [f for f in listdir() if isfile(f) and 'm4a' in f] # List music files inside musicPath
    # Organize music files
    for music in musicFiles:
        # Read music metadata
        metadata = TinyTag.get(music)
        artist_name = metadata.artist
        album_name = metadata.album
        artist_name = charReplace(artist_name)
        dirSearch(artist_name)
        # Only process album value if not empty
        if album_name != None:
            album_name = charReplace(album_name)
            dirSearch(q=album_name,p=artist_name)
            chdir('..')
            shutil.move(music, artist_name+'/'+album_name+'/'+music)
        else:
            shutil.move(music, artist_name+'/'+music)
        

