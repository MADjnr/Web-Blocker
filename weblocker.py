'''
Blocking websites with python
This program blocks websites that are disturbing during work hours
'''

from datetime import datetime as dt

import time
hosts_temp = 'hosts'
hosts_path = '/etc/hosts'
redirect = '127.0.0.1'
website_list = ["www.facebook.com", "facebook.com", 'gmail.com', 'hotmail.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, 12) < dt.now() < \
            dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, 27):
        print("working hour...")
        with open(hosts_temp, 'r+') as file:  ## 'r+' means that you can read and append text in a file
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readline() ##readlines produces all the lines in our host file. Therefore, content is a list
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        #print("working hours...")


        print("fun hours...")

    time.sleep(5)


