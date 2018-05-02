import json
import os
import time
with  open("toemails.txt", "r") as f:
    to = f.readlines()


#stopped at 98
mails = ['elmahy2005@gmail.com',
          'elmahyahmed.gk@gmail.com',
          'elmahyahmed.gka@gmail.com',
          'elmahyahmed.gkb@gmail.com',
          'elmahyahmed.gkc@gmail.com',
          'elmahyahmed.gkd@gmail.com',
          'elmahyahmed.gke@gmail.com',
          'elmahyahmed.gkf@gmail.com',
          'elmahyahmed.gkg@gmail.com',
          'elmahyahmed.gkh@gmail.com',
          'elmahyahmed.gki@gmail.com',
          'elmahyahmed.gkj@gmail.com']


for mail in mails:
    print(mail)
    with  open("from.json", "w") as f:
        json.dump([mail],f)
    with open("log.json", "r") as log:
        x = json.load(log)['current']
        
    for j in range(x,x+8):
        to100 = to[j*100:((j+1)*100)-1]
        with  open("toemails100.json", "w") as f:
            json.dump(to100,f)
        os.system("python3 sender.py")
        print(j)
        time.sleep(1)
    x = x + 8
    with open("log.json", "w") as log:
        json.dump({"current":x},log)