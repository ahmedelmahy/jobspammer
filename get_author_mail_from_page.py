from bs4 import BeautifulSoup
import requests
import re
import json

#' extract mail from text
#' @param text
#' @return mails in text

def extractMails(text):
    mails = re.findall("[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+", text)
    mails = list(set(mails))
    return mails

    
#' find author mail and exculde other mails in the page
#' learning model ?
#' each time we run the script it saves all the mails in the page after
#' running the script 1000 times the publisher emails will be repeated 
#' @param mails a list
#' assumes the publisher mails file contains an empty list and it exists
def saveMails(mails):
    with open("publisher_mails.json","r") as f:
            pubmails = json.load(f)
    pubmails.extend(mails)
    with open("publisher_mails.json","w") as f:
        json.dump(pubmails,f)


def excludeMails():
    with open("publisher_mails.json","r") as f:
            pubmails = json.load(f)
            
    s = set([x for x in pubmails if pubmails.count(x) > 1])
    return list(s)

def findAuthor(mails, excludedmails):
    return [i for i in mails if i not in excludedmails]
    

    
    

url = "http://scholar.google.com.eg/scholar_url?url=http://circres.ahajournals.org/content/122/9/1276.short&hl=ar&sa=X&scisig=AAGBfm1VVpv4Zxyc9XrrCwpqTBS5DZObXA&nossl=1&oi=scholaralrt"
if "google" in url:
    url = re.findall("url=(.+)&hl",url)[0]
page = requests.get(url)
txt = page.text

mails = extractMails(txt)
saveMails(mails)
excludedmails = excludeMails()
findAuthor(mails, excludedmails)
    