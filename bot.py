import praw
import config
import facebook
import requests
import time
from time import sleep
		
def BotLogin():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "MetroBusTicketBot Reporting For Duty!")
	return r
	
def RunBot(r, p):
	date = p['message'].split("-")[0]
	color = p['message'].split("-")[1].split(" ")[0]
	letter = p['message'].split("-")[1].split(" ")[1][0]
	
	sr = r.subreddit("seattlemetrotickets")
	sr.submit(date + " - " + color + " " + letter, '')
	sr.sticky(1)
	print(letter)
	
def GetDateOfFBPost(p):
	date = p['message'].split("-")[0]
	print("Posted Date: " + config.last_date)
	print("Pulled Date: " + date)
	if date != config.last_date:
		r = BotLogin()
		config.last_date = date
		RunBot(r, p)
	
while 0 == 0:
	graph = facebook.GraphAPI(config.access_token)
	profile = graph.get_object(config.user)
	posts = graph.get_connections(profile['id'], 'posts')

	GetDateOfFBPost(posts['data'][0])
	time.sleep(600)