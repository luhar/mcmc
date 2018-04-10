from pydub import AudioSegment

song = AudioSegment.from_mp3("party.mp3")

print(song)

song.export("output.mp3", format="mp3")
