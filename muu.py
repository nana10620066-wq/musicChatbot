def greet():
    print("="*50)
    print("'Me Me' Music Chatbot")
    print("="*50)
    print("HELLO! Welcome to Music Chatbot.")
    print("I am here to make your day better with music.")
    print("Let's find the perfect song for your mood!")
    print("="*50)
    
def recommend_music(mood):
    
    print("\n Searching for your favourite songs....")
    
    if mood == "happy":
        print("\n Happy Mood - Feel Good Songs")
        print("-" * 40)
        print("1. Happy - Pharrell Williams")
        print("2. Shake It Off - Taylor Swift")
        print("3. Cheerleader - OMI")
        print("4. Baby - Justin Bieber")
        print("5. Dear Future Husband - Meghan Trainor")

    elif mood == "sad":
        print("\n Sad Mood - Emotional Songs")
        print("-" * 40)
        print("1. Someone Like You - Adele")
        print("2. Let Her Go - Passenger")
        print("3. Cheating on You - Charlie Puth")
        print("4. Tell Me Where to Go - JhonDerek")
        print("5. Unconditionally - Katy Perry")

    elif mood == "love":
        print("\n Love Mood - Romantic Songs")
        print("-" * 40)
        print("1. Perfect - Ed Sheeran")
        print("2. I Think They Call This Love - Elliot James Reay")
        print("3. Love Story - Taylor Swift")
        print("4. Beautiful in White - Westlife")
        print("5. Dandelions - Ruth B.")

    elif mood == "heartbroken":
        print("\n Heartbroken Mood - Healing Songs")
        print("-" * 40)
        print("1. The Man Who Can't Be Moved - The Script")
        print("2. Why - Doublej")
        print("3. Rewrite the Stars - Anne-Marie & James Arthur")
        print("4. Multo - Cup of Joe")
        print("5. About You - The 1975")

    else:
        print("\nSorry! I don't know this mood.")
        print("Please choose a mood from the list.")

    print("-" * 40)
def show_genre():
        print("\n MUSIC GENRES")
        print("=" * 50)
        print("1. Pop")
        print("2. Rock")
        print("3. Jazz")
        print("4. Classical")
        print("5. Hip-Hop")
        print("6. R&B")
        print("=" * 50)


def show_help():
        print("\n HOW TO USE MUSIC CHATBOT")
        print("-" * 40)
        print("1. Type 'Hello' to greet the chatbot.")
        print("2. Type 'Music' to get song recommendations.")
        print("3. Type 'Genre' to see music genres.")
        print("4. Type 'Help' to see instructions.")
        print("5. Type 'Exit' to close the chatbot.")
        print("-" * 40)

def chatbot():
   greet()
   while True:
    
        user=input("\n You: ").lower()
        if "hello" in user or "hi" in user:
            print("\n Bot: Hello! How are you today?")
            print("\n Bot: I hope you are having in wonderful day!")
        
        elif "fine" in user:
             print("\n OK!!Good...")
        
        elif "song" in user or "music" in user:
            print("\n Bot: What kind of mood are you in?")
            print("1. Happy")
            print("2. Sad")
            print("3. Love")
            print("4. Heartbroken")
        
            mood=input("\n Enter your mood: ").lower()
        
            recommend_music(mood)
        
            again=input("\n Do you want more music? (yes/no): ")
        
            if again=="yes":
                print("\n Bot: Great! let's enjoy more music!")
            else:
                print("\n Bot: Okay!Enjoy your song!")
            
        elif "genre" in user:
            show_genre()
            
        elif "help" in user:
            show_help()
            
        elif "exit" in user or "thank" in user:
            print("="*50)
            print("\n Bot: Thank you for chatting with me!")
            print("\n Bot: Keep smiling and enjoy your music!")
            print("\n Bot: Goodbye! See you again")
            print("="*50)
            
            break   
        else:
            print("\n Bot: Sorry! I don't understand!")
            print("\n Bot: Please try again...")
            
chatbot()
    

