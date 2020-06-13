from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import pyttsx3 as px
import speech_recognition as s
file1 = open("data.txt", "r")
sr=s.Recognizer()


engine=px.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



bot = ChatBot('MyBot', logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
    ])
convo=[  "Hi",
         "Helloo",
         "How are you doing",
         "I am doing great",
         "Who designed you?",
         "My name is Chatty, I am created by Ishee",
         "Thank you, Chatty",
         "Stay safe,You are welcome",
        "where do u live",
         "I exist virtually",
         "Good morning",
        "Good Morning",
        "Tell me about your dreams",
	    "I dream that I will become rich.",
	    "I don't know if I dream or not.",
         "Tell me more about your feelings.",
	     "That feeling when?",
     	"Are you intoxicated",
    	"I'm softwareI can't drink.",
    	"Are you jealous",
         "I am not yet capable of feeling jealousy.",
     	"Are you amused",
	     "I like to laugh as much as the next being.",
	     "Are you glad",
          "Some people feel happy, others feel sad.",
	    "Should I be?  Did something happen?",
	   "I don't understand.",
       "Who designed you?",
        "My name is Chatty, I am created by Ishee"

]
for x in file1:
 convo.append(x)
trainer = ListTrainer(bot)
#training  the bot with convo
trainer.train(convo)
print("You can talk to bot")

main=Tk()

main.geometry("1000x1000")
main.title("Chatty")

img = PhotoImage(file='bot.gif')

photoL = Label(main, image=img)

photoL.pack()



def speak(word):
    engine.say(word)
    engine.runAndWait()

def ask_from_bot():
    query = textF.get()

    Answer_from_chatty = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    msgs.insert(END, "CHATTY : " + str(Answer_from_chatty))
    speak(Answer_from_chatty)
    textF.delete(0, END)
    msgs.yview(END)
frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, background="Pink", width=250, height=15 ,yscrollcommand=sc.set,xscrollcommand=sc.set)

sc.pack(side=BOTTOM, fill=X)
msgs.pack(side=LEFT, fill=BOTH)
sc.pack(side=RIGHT, fill=Y)
frame.pack()
# creating text field

textF = Entry(main, font=("Verdana", 23),background="Orange")
textF.pack(fill=X, pady=20)

button = Button(main, text="Ask from bot", font=("Verdana", 23), command=ask_from_bot,background="Red")
button.pack()

# creating a function for the enter event

def enter(event):
    button.invoke()

main.bind('<Return>', enter)

main=mainloop()
