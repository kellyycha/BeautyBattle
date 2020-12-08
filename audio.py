import urllib.request
from pydub import AudioSegment
from pydub.playback import play

# Load into PyDub
loop = AudioSegment.from_mp3("background.mp3")
# Play the result
play(loop)