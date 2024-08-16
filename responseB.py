import random
import json

def main():
   with open('bible_verses.json', 'r') as file:  
       verse_bank = json.load(file)

   theme_dict = {theme: theme for theme in verse_bank.keys()}
   theme_dict['exit'] = 'exit'

   while True:
       theme = input("Which theme do you want for a Bible verse? (inspiration, hard times, encouragement, confidence, exit): ").lower()
       if theme in theme_dict:  
           if theme == 'exit': 
               print("Goodbye and may the Lord's blessings be upon you!")
               break
           else:
               verses = verse_bank[theme_dict[theme]]
               verse_key = random.choice(list(verses.keys()))
               print(f"{verse_key}  {verses[verse_key]}")
       else:    
           print("Invalid theme. Please try again.")

main()