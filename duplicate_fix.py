from mutagen.mp4 import MP4
from os import chdir, remove, listdir
from os.path import isdir
import glob
import shutil
from musicOrganizer_v2 import charReplace

if __name__ == "__main__":
    # Go to musicPath & Get music file
    musicPath = 'D:/music'
    chdir(musicPath)
    musicFiles = glob.glob('**/*.m4a', recursive=True)
    # Remove mismatch album inside artist folder
    for music in musicFiles:
        try:
            metadata = MP4(music)
        except:
            pass
        artist_name = metadata.get(u'\xa9ART')[0]
        artist_name = charReplace(artist_name)
        if ';' in artist_name:
            artist_name = artist_name.split(';')[0]
            music = music.split('\\')
            if artist_name != music[0]:
                path = '/'.join(music[:-1])
                if path != '' and '/' in path:
                    try:
                        shutil.rmtree(path)
                    except:
                        pass
                else:
                    remove(path+'/'+music[-1])
    # Remove empty folder
    pathDir = [p for p in listdir() if isdir(p)]
    for p in pathDir:
        if not listdir(p):
            shutil.rmtree(p)
