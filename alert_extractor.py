import imaplib
import re
from bs4 import BeautifulSoup
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('elmahy2005@gmail.com', 'pass')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string

scholar_ids = []
for id in id_list[300:400]:
    result, data = mail.fetch(id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    if  "scholar_alert" in str(data[0][1]):
        print("found")
        scholar_ids.append(id)
    else:
        print(".")
        
        
id = scholar_ids[2]
result, data = mail.fetch(id, "(RFC822)")
soup = BeautifulSoup(data[0][1])


soup.find_all('h3')
for link in soup.find_all('a'):
    print(link.get('href'))
data.fin
