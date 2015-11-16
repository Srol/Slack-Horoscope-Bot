# Horoscope Slackbot

## Disclaimer

I am not a professional coder, I'm a journalist by trade and a self-taught Python programmer. There are probably many problems with this bot. All I can say is it works for us. If you need help setting it up, I'll do what I can.

## Setup process

1. Clone the repository to your local machine. Make sure you have the Heroku toolbelt installed and authenticated.
2. Go into the directory of the repository at the command line and type `heroku create` to initialize a new Heroku app. Note the name of the new app. 
3. Open up your Slack integrations control panel panel and click "Outgoing Webhooks." Create a new integration as /horoscope.
4. Set channel to whatever you desire (we have it set to any) and set the Trigger Word to `Horoscope: `. Change the URL to the name of your Heroku app with the subdirectory "horos" (i.e. http://your-app-name.herokuapp.com/horos). Finally, generate a token and save it for later. The rest of the form you can customize as you wish.
5. Open up the file horoscope.py in the text editor of your choice and set the variable SLACK_TOKEN on line 7 to equal the token slack gave you (in the quotes of course).
6. Save the file and commit the changes, and then type `git push heroku master` to send the bot to Heroku.
7. Wait a few moments, and you should be good to go by typing "Horoscope: Sign" in Slack.