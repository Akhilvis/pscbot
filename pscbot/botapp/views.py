from django.shortcuts import render

# Create your views here.
from chatterbot import ChatBot
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

from chatterbot.trainers import ListTrainer


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(bot)

trainer.train(conversation)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])



def mainfun(request,query):
	print('Type something to begin...')

	while True:
	    try:
	        user_input = input()

	        bot_response = bot.get_response(user_input)

	        print(bot_response)

	    # Press ctrl-c or ctrl-d on the keyboard to exit
	    except (KeyboardInterrupt, EOFError, SystemExit):
	        break
