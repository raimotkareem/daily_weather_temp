import requests
import bs4
import schedule
import time


def send(temp):
    mails = ['raimotkareem@gmail.com']
    api_base_url = "https://api.mailgun.net/v3/mg.hisect.com/messages"
    api_key = "key-00e69df5c6360e9b8eb4c6fd0bbe11f0"
    from_email = "raimot <raimotkareem@gmail.com>"
    to_email_list = "raimotkareem@gmail.com"
    subject = "FROM PYTHON"
    messages = "data scrapped sucessful" + str(temp)
    # this return help to post  auth and data to api_base_url
    return requests.post(
    api_base_url,
    auth=("api", api_key),
    data={"from": from_email, "to": to_email_list, "subject": subject, "text": messages})
    


def job(temp):
    url = "https://api.openweathermap.org/data/2.5/weather?lat=7.1475&lon=3.3619&appid=04ebe6de1f091199b7ec50ea6f2ba5b9"
    response = requests.get(url)
    weather = response.json()
    temp = (weather['main']['temp'])
    send(temp)
    print(temp)



schedule.every().day.at("11:44").do(job,'temp')


while True:
    schedule.run_pending()
    time.sleep(60) 


job()