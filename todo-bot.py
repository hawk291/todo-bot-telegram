#!/usr/bin/python3.9

# todo bot for telegram

import telebot
#from datetime import date

token = ''

todos = {}
todos_today = {}
todos_tomorrow = {}

bot = telebot.TeleBot(token)

def add_todo(date, task):
	if date == 'today':
	    todos_today[date] = task
	elif date == 'tomorrow':
	    todos_tomorrow[date] = task
	else:
	    todos[date] = task

# TODO
#welcome = 'TODO App [' + str(date.today()) + '] Type help for info >> '

@bot.message_handler(commands=["help"])
def help(message):
	bot.send_message(message.chat.id, "Available commands are:\n/show - print tasks\n/add - add a new task\n/help - show available commands")

@bot.message_handler(commands=["add"])
def add(message):
	# syntax: /add 20-12-2020 task 1
	# for debug - print(f'Received: {message.text}')
	explode_command = message.text.split(maxsplit=2)
	date = explode_command[1]
	task = explode_command[2]
	add_todo(date, task)
	bot.send_message(message.chat.id, f'Task \"{task}\" added for {date}')

@bot.message_handler(commands=["show"])
def show(message):
	todos_empty = bool(todos)
	if str(todos_empty) == 'False':
	    bot.send_message(message.chat.id, "There are no tasks yet")
	else:
	    for date, task in todos.items():
	    	bot.send_message(message.chat.id, date + " : " + task)
	       
	# output todos_today
	todos_today_empty = bool(todos_today)
	if str(todos_today_empty) == 'False':
	    bot.send_message(message.chat.id, "There are no tasks for today yet!")
	else:
	    for date, task in todos_today.items():
	    	bot.send_message(message.chat.id, date + " : " + task)

	# output todos_tomorrow
	todos_tomorrow_empty = bool(todos_tomorrow)
	if str(todos_tomorrow_empty) == 'False':
	    bot.send_message(message.chat.id, "There are no tasks for tomorrow yet!")
	else:
	    for date, task in todos_tomorrow.items():
	        bot.send_message(message.chat.id, date + " : " + task)

# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    bot.send_message(message.chat.id, "I don't understand \"" + message.text + "\"\nMaybe try the help page at /help")

bot.polling(none_stop=True)







   

    



