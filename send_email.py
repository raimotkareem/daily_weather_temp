import sys
import requests
from aa import *
from main import *

#this function helps to send email and mails can be in form of list if we want
def send():
    """
        all required details are passed into variable below 
        e.g mail,api_base_url and api_key(gotten from mailgun),till messages.
    """
    mails = ['raimotkareem@gmail.com']
    api_base_url = "https://api.mailgun.net/v3/mg.hisect.com/messages"
    api_key = "key-00e69df5c6360e9b8eb4c6fd0bbe11f0"
    from_email = "raimot <raimotkareem@gmail.com>"
    to_email_list = "raimotkareem@gmail.com"
    subject = "FROM PYTHON"
    messages = "data scrapped sucessful" + temp
    # this return help to post  auth and data to api_base_url
    return requests.post(
    api_base_url,
    auth=("api", api_key),
    data={"from": from_email, "to": to_email_list, "subject": subject, "text": messages})

send()
print("Done!")




