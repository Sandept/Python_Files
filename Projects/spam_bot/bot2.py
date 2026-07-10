# Automated import from: https://github.com/ndleah/python-mini-project.git
# Original Author: ndleah


from bot1 import spammingBot

with open('spam_bot/text.txt','r') as txt :
    content = txt.read()
    for word in content.split(" "):
        print(word)
        spammingBot(word)
