import os
import feedparser
import json
from flask import Flask, request

# Add your Slack token to the variable below.
SLACK_TOKEN = ""
url = ""
payload = {}
headers = {'content-type': 'application/json'}

app = Flask(__name__)

# this endpoint listens for incoming slash commands from Slack.
@app.route('/horos', methods=['POST'])
def horos():
	if request.method == "POST" and request.form.get('token') == SLACK_TOKEN:
		from_number = request.form.get('text')
		from_number = from_number[11:]
		channel = request.form.get('channel_name')
		message = matchHoroscope(from_number)
		payload = {
			"text": message,
			"channel": channel,
			"username": "Star-Messenger",
		}
		return json.dumps(payload)

final = ""
signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]

# One half of the process of matching a horoscope with an actual reading.
def matchHoroscope(sign):
	if sign.lower() in signs:
		return getHoroscope(sign)
	else:
		return "The answer you seek is not written in the stars."

# This function pulls today's horoscope through the RSS feeds of FindYourFate.com
def getHoroscope(sign):
	url = 'http://www.findyourfate.com/rss/dailyhoroscope-feed.asp?sign=' + sign.title()
	d = feedparser.parse(url)
	container = d.entries[0]
	horoscope = container['summary_detail']['value']
	return horoscope