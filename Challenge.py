# import libraries
import requests
from bs4 import BeautifulSoup
import csv
import random
import sys

# specify the url to parse
url = "https://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-a-hilarious-response.html/"

# query the website and return the html to the variable ‘page’
page = requests.get(url)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, "html.parser")

# grab all 61 questions from the site
questions = soup.find_all("h2")
questions = [q.text for q in questions]

# save all questions to csv file
with open("questions.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    for q in questions:
        writer.writerow([q])

# generate random index to get the random question
i = random.randint(0,len(questions) - 1)

# get the API key from command arg
key=str(sys.argv[1])

# send the question
report = {}
report["value1"] = "programs@prepr.org"
report["value2"] = questions[i]
report["value3"] = ""
requests.post("https://maker.ifttt.com/trigger/send_mail/with/key/%s" % key, data=report)    