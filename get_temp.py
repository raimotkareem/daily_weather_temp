import requests
import bs4
import schedule
import time

def job(temp):
    url = "https://api.openweathermap.org/data/2.5/weather?lat=7.1475&lon=3.3619&appid=04ebe6de1f091199b7ec50ea6f2ba5b9"
    response = requests.get(url)
    weather = response.json()
    temp = (weather['main']['temp'])


    print("I'm working..." ,temp)
    return temp

    
schedule.every().day.at("07:59").do(job,'It is time')

while True:
    schedule.run_pending()
    time.sleep(60) 

job(1)    

# def job(t):
#     print("I'm working...", t)
#     #return

# schedule.every().day.at("08:07").do(job,'It is 01:00')

# while True:
#     schedule.run_pending()
#     time.sleep(60) # wait one minute

job(1)    
