import datetime
import random
import os

# Get today's date
today = datetime.date.today().strftime("%Y-%m-%d")

# Ask for your diary entry
entry = input("Write your diary entry: ")

# Define mood-based emojis
moods = {
    "happy": ["😃", "😊", "🥳", "😁", "🎉"],
    "sad": ["😢", "😞", "💔", "😭", "🥺", "💔"],
    "tired": ["😴", "🥱", "💤", "😩", "😓", "🛌"],
    "angry": ["😡", "😠", "🤬", "💢", "😤", "🖕", "👿"],
    "love": ["❤️", "😍", "😘", "💖", "💕", "🤟", "💑"],
    "random": ["🌟", "🎶", "🍕", "🌸", "🔥", "🍀", "✨"]
}

# Ask user for their mood
print("How are you feeling today?")
print("[1] Happy 😁 [2] Sad 😢  [3] Tired 😴  [4] Angry 😡  [5] Love ❤️  [6] Random 🎲")
mood_choice = input("Choose a number: ")

# Map user input to moods
mood_keys = ["happy", "sad", "tired", "angry", "love", "random"]
selected_mood = mood_keys[int(mood_choice) - 1] if mood_choice.isdigit() and 1 <= int(mood_choice) <= 6 else "random"

# Pick a random emoji based on mood
emoji = random.choice(moods[selected_mood])

# Create a diary file and write the entry
file_name = f"{today}.md"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(f"## {today} {emoji}\n\n{entry}\n")

print(f"Diary entry saved as {file_name} with mood {emoji}!")

os.system("git add .")
os.system('git commit -m "Updated diary entry"')
os.system("git push origin main")

print("Changes pushed to GitHub! 🚀")
