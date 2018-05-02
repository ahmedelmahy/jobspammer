import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json
import time

with  open("toemails100.json", "r") as f:
    to100 = json.load(f)
k = []
for i in to100:
    j = i.strip()
    j = j.replace("\n","")
    j = j.replace(" ","")
    if '@' in j:
        k.append(j)
    
filename = "CV- Ahmed-Elmahy.pdf"
attachment = open("CV- Ahmed-Elmahy.pdf", "rb")
body = '''Dear Sir/ Madam, \n \n
    I am looking for an internship for six months from June 2018. I studied Medicine(2011-2017) at Alexandria University, Egypt. I have five years experience with python, R, data analysis and machine learning. I won a fellowship to work until June 2018 at Helmholtz Zentrum Munchen, Institute of computational biology on developing RNASeq classification models where I use SVM, random forest and dimention reduction techniques. But my interests extends to business as I am really trying to translate research ideas into industry. 
    Please find attached my CV.
    \n\n
    Kind regards,\n
    Ahmed Elmahy'''  
    
with open("from.json","r") as f:
    fromaddr = json.load(f)[0]
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,"XXX")
i = 0
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['Subject'] = "Inquiry about available internship opportunities for international student"
msg.attach(MIMEText(body, 'plain'))
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)



msg['To'] = ""
text = msg.as_string()
server.sendmail(fromaddr, k, text)
i = i + 1



