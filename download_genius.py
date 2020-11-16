import lyricsgenius
import os
import json

# os.chdir("/Users/michal/Desktop/hhgen/")

artist_name = "Łona"

token = ""
genius = lyricsgenius.Genius(token)
artist = genius.search_artist(artist_name, max_songs=300)

artist.save_lyrics()

with open("/Users/michal/Desktop/hhgen/Lyrics_Łona.json") as f:
  data = json.load(f)
print(data)

with open('lona.txt', 'w') as outfile:
    for sng in data["songs"]:
        # print(sng["lyrics"])
        outfile.write(sng["lyrics"])


data["songs"][0]["lyrics"]
