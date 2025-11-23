import time
import sys

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_lyrics():
    # 🎬 Intro with your name
    type_text("🎬 Presented by: ASHISH KUMAR PRAJAPATI 🎬", 0.07)
    time.sleep(1)
    type_text("🎶  GALTI SE MISTAKE SONG  🎶", 0.08)
    print()
    time.sleep(1.5)

    lyrics = [
    "Chal muscle phulaa na...",
    "Thodi body banaana...",
    "Tere chikne gaalon pe...",
    "Stubble ki phasal ugaana...",

    "Arey re re aye...",
    "Abey aye...",
    "Chal beta shuru hoja...",
    "Guru bagal utha ke...",
    "Thoda deo laga na...",
    "Kisi bagal wali ko...",
    "Mardani khushbu sunghana...",

    "Chal upar ke do button...",
    "Dheele karke batana...",
    "Baalon waala seena dikhana...",
    "Baalon waala seena dikhana...",

    "Barson talak tu cycle pe ghuma hai...",
    "Highway pe motorcycle bhaga ke dekh...",
    "......................................",


    
    "Speed mein tujhko agar sardi lage toh...",
    "Seat pe piche ladki bitha ke dekh...",

    "Ye hi umar hai karle...",
    "Galti se mistake...",
    "Ye hi umar hai karle...",
    "Galti se mistake...",
    "Ye hi umar hai karle...",
    "Galti se mistake...",
    "Ye hi umar hai karle...",
    "Galti se mistake...",
    ]
    delays = [
        0.7, 0.6, 0.7, 0.8, 0.9, 0.3,
        0.8, 0.5, 0.8, 0.3,
        0.8, 0.7, 0.8, 0.7, 1.2
    ]

    for i, line in enumerate(lyrics):
        type_text(line, 0.045)
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics() 