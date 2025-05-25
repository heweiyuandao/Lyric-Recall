# This is a little game about Taylor Swift Lyric. 

import random
import string
import sys

# Define a class to represent a lyric card with song name, previous line, and next line
class LyricCard:
    def __init__(self, song, previous_line, next_line):
        self.song = song
        self.previous_line = previous_line
        self.next_line = next_line

# Clean and split the text for word comparison
def clean_words(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation)).split()

# Check if user wants to quit, display score then exit
def check_exit(user_input, score):
    if user_input.strip().lower() == 'exit':
        print(f"\nGame exited by user. Your final score is: {score:.1f}. Goodbye!")
        sys.exit()

# Main function
def start_quiz(lyrics_data):
    score = 0
    print("Welcome to the Taylor Swift Lyric Quiz! Type 'exit' anytime to quit.\n")

    while True:
        question = random.choice(lyrics_data)
        correct_line = question.next_line
        correct_song = question.song
        prev_line = question.previous_line

        print(f"\nLyric: \"{prev_line}\"")
        attempts = 0

# Guess the next line with up to 3 attempts and hint if 3+ words match
        while attempts < 3:
            guess = input("What comes next?\n> ")
            check_exit(guess, score)
            if guess.strip().lower() == correct_line.lower():
                print("Correct lyric! 🎉")
                break
            else:
                attempts += 1
                matched_words = list(set(clean_words(guess)) & set(clean_words(correct_line)))
                if len(matched_words) >= 3:
                    wants_hint = input("That was close! Do you want a hint? (yes/no)\n> ")
                    check_exit(wants_hint, score)
                    if wants_hint.strip().lower() == 'yes':
                        print(f"Hint: You got these words right: {', '.join(matched_words)}")
                else:
                    print("Not quite. Try again!")

# If failed after 3 attempts
        if attempts == 3:
            cont = input("You've used all attempts. Do you want to continue playing? (yes/no)\n> ")
            check_exit(cont, score)
            if cont.strip().lower() != 'yes':
                print(f"\nThe correct lyric was: \"{correct_line}\" from \"{correct_song}\".")
                print(f"Your final score is: {score:.1f}. Thanks for playing!")
                break
            continue

# Guess the song title with up to 3 attempts
        for i in range(3):
            song_guess = input("What song is this from?\n> ")
            check_exit(song_guess, score)
            if song_guess.strip().lower() == correct_song.lower():
                print("Correct song! You earn 1 point. 🎵")
                score += 1
                break
            else:
                if i < 2:
                    print(f"Not quite. You have {2 - i} attempts left.")
        else:
            print("You guessed the lyric but not the song. You earn 0.5 points.")
            score += 0.5

        print(f"Your current score: {score:.1f}")

# Define the lyric cards
if __name__ == "__main__":
    lyrics_data = [
        LyricCard("Love Story", "We were both young when I first saw you", "I close my eyes and the flashback starts"),
        LyricCard("Love Story", "I close my eyes and the flashback starts", "I'm standing there on a balcony in summer air"),
        LyricCard("Love Story", "That you were Romeo, you were throwing pebbles", "And my daddy said, stay away from Juliet"),
        LyricCard("Blank Space", "Nice to meet you, where you been?", "I could show you incredible things"),
        LyricCard("Blank Space", "I could show you incredible things", "Magic, madness, heaven, sin"),
        LyricCard("Blank Space", "Got a long list of ex-lovers", "They'll tell you I'm insane"),
        LyricCard("You Belong With Me", "You're on the phone with your girlfriend, she's upset", "She's going off about something that you said"),
        LyricCard("You Belong With Me", "She doesn't get your humor like I do", "I'm in the room, it's a typical Tuesday night"),
        LyricCard("You Belong With Me", "If you could see that I'm the one who understands you", "Been here all along, so why can't you see?"),
        LyricCard("Shake It Off", "I stay out too late", "Got nothing in my brain"),
        LyricCard("Shake It Off", "Got nothing in my brain", "That's what people say"),
        LyricCard("Shake It Off", "I'm dancing on my own (dancing on my own)", "I make the moves up as I go"),
        LyricCard("Enchanted", "There I was again tonight forcing laughter, faking smiles", "Same old tired, lonely place"),
        LyricCard("Enchanted", "Walls of insincerity, shifting eyes and vacancy", "Vanished when I saw your face"),
        LyricCard("Enchanted", "This night is sparkling, don't you let it go", "I'm wonderstruck, blushing all the way home"),
        LyricCard("Cruel Summer", "Fever dream high in the quiet of the night", "You know that I caught it"),
        LyricCard("Cruel Summer", "I don't wanna keep secrets just to keep you", "And I snuck in through the garden gate"),
        LyricCard("Cruel Summer", "It's new, the shape of your body", "It's blue, the feeling I've got"),
        LyricCard("Style", "Midnight, you come and pick me up, no headlights", "Long drive, could end in burning flames or paradise"),
        LyricCard("Style", "And I got that good girl faith and a tight little skirt", "And when we go crashing down, we come back every time"),
        LyricCard("Style", "You got that James Dean daydream look in your eye", "And I got that red lip classic thing that you like"),
        LyricCard("Cardigan", "Vintage tee, brand new phone", "High heels on cobblestones"),
        LyricCard("Cardigan", "And when I felt like I was an old cardigan", "Under someone's bed"),
        LyricCard("Cardigan", "You put me on and said I was your favorite", "A friend to all is a friend to none")
    ]

    if not lyrics_data:
        print("No lyrics found.")
    else:
        start_quiz(lyrics_data)

