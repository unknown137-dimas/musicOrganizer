# V2 - Add support for multiple artist

import glob
from mutagen.mp4 import MP4
from os import chdir, mkdir, listdir
from os.path import isdir, basename
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
    # Go to musicPath & Get music file
    musicPath = 'D:/Output'
    chdir(musicPath)
    musicFiles = glob.glob('**/*.m4a',recursive=True)
    # Organize music files
    for music in musicFiles:
        # Extract filename
        music_file = basename(music)
        # Read music metadata
        metadata = MP4(music)
        artist_name = metadata.get(u'\xa9ART')[0]
        album_name = metadata.get(u'\xa9alb')
        if album_name != None:
            album_name = album_name[0]
        tmp = []
        artist_name = charReplace(artist_name)
        # Handle multiple artists value
        if ',' in artist_name:
            artist_name = artist_name.replace(',',';')
            tmp.append(artist_name)
            metadata[u'\xa9ART'] = tmp
            metadata.save()
        if ';' in artist_name:
            artist_name = artist_name.split(';')[0]
        dirSearch(artist_name)
        # Only process album value if not empty
        if album_name != None:
            album_name = charReplace(album_name)
            dirSearch(q = album_name,p = artist_name)
            chdir('..')
            out = artist_name+'/'+album_name+'/'+music_file
        else:
            out = artist_name+'/'+music_file
        try:
            shutil.move(music, out)
        except shutil.SameFileError:
            pass
            


