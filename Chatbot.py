import nltk
from nltk.chat.util import Chat, reflections
import pyttsx3

# Download required NLTK data files
nltk.download('punkt')

# Define a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today? I am a Chatbot created by J And J industries. I will eventually be placed in a robot head!.",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a currently nameless, but you created me.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's OK, never mind",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great!",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want?",
        ["I just want to help you!",]
    ],
    [
        r"(.*) created?",
        ["I was created by Jordan and Jeff!",]
    ],
    [
        r"(.*) (location|city)?",
        ['I am everywhere!',]
    ],
    [
        r"how (.*) weather in (.*)?",
        ["Weather in %2 is always great.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!",]
    ],
    [
        r"What's your favorite animal?",
        ["The best animal is the Hedge E Moe Hog",]
    ],
]

# Reflections
reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

# Create the chatbot
chatbot = Chat(pairs, reflections)

#Start text-to-speech
engine = pyttsx3.init()

#Function Text to Speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Start the chatbot
def chat():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Bye, take care. See you soon!")
            speak("Bye, take care. See you soon!")
            break
        response = chatbot.respond(user_input)
        print(response)
        speak(response)

# Run the chatbot
chat()
