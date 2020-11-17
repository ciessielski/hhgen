import lyricsgenius
import os
import json

artists = ["LSO", "R.A.U." ]

def cleansong(lyrics):
    l = lyrics.replace("[Intro]", "").replace("[Zwrotka 1]", "").replace("[Zwrotka 2]", "").replace("[Zwrotka 3]", "").replace("[Zwrotka 4]", "").replace("[Refren]", "").replace("[Refren 2]", "").replace("[Refren 3]", "").replace("[Outro]", "").replace("[Tekst i adnotacje na Rap Genius Polska]", "")
    return l

for a in artists:
    os.chdir("/Users/michal/Desktop/hhgen/")

    artist_name = a
    artist_plain = artist_name.replace(" ", "")
    artist_plain

    token = "zG4ymG1i-QLcpYazO-L0qZduCp5JVfBnZdagqDUA9mE-jtnp5DsQVvUjwns4gdHE"
    genius = lyricsgenius.Genius(token)
    artist = genius.search_artist(artist_name, max_songs=300)

    print("all songs downloaded")
    # genius.search_artist("Taco Hemingway")
    os.chdir("./json")

    artist.save_lyrics()

    # with open("/Users/michal/Desktop/hhgen/Lyrics_ŁonaiWebber.json") as f:
    with open(f"Lyrics_{artist_plain}.json") as f:
      data = json.load(f)

    data["songs"]

    with open(f'../txt/{artist_plain}.txt', 'w') as outfile:
        for sng in data["songs"]:
            try:
                lir = cleansong(sng["lyrics"])
                outfile.write(lir)
            except:
                print("no lyrics for song")

# pwd
#
# with open(f"./json/Lyrics_SokółPL.json") as f:
#   data = json.load(f)
#
# data["songs"]
#
# with open(f'./txt/Sokół.txt', 'w') as outfile:
#     for sng in data["songs"]:
#         try:
#             lir = cleansong(sng["lyrics"])
#             outfile.write(lir)
#         except:
#             print("no lyrics for song")
