import time
from datetime import datetime as dt

hosts_temp="Users/andrewyip/Desktop/hosts" #path to temp
hosts_path="/etc/hosts" #path to the actual host
redirect="127.0.0.1" #redirect is the IP address for error website
website_list=["www.facebook.com","facebook.com","www.instagram.com","instagram.com", "twitter.com"] #list of

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,13):
        print("Working hours...") 
        with open(hosts_path,'r+') as file: #opens file
            content=file.read()
            for website in website_list: 
                if website in content: #if the website is in the content already just pass
                    pass
                else:
                    file.write(redirect+" "+ website+"\n") #else you add it to the file by writing to it
    else: #if it is not within the hour
        with open(hosts_path,'r+') as file: #open the hosts path
            content=file.readlines() #read the file as a list
            file.seek(0) #change the pointer to the top
            for line in content: #each line in the content list
                if not any(website in line for website in website_list):
                    file.write(line) #adds lines that are contained in the website list to the top of the doc
            file.truncate() #then it truncates the extra lines of code from the bottom
        print("Fun hours...")
    time.sleep(5)


#The path to access this file

#"/Users/andrewyip/Desktop/udemy_python/intro stuff/app3 websiteblocker/website_blocker.py"



#The Links we want to block off

#"www.facebook.com","facebook.com","www.instagram.com","instagram.com"