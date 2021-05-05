import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC
import sys

# pincode = input('Enter your pincode we will fetch dose availability upto 5 days')
pincode = sys.argv[1]
x = datetime.datetime.now()
today = x.strftime("%d-%m-%Y")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={today}'.format(pincode,today)
# print(url)
covidData = None
try:
    covidData = requests.get(url,headers=headers)
    #if we fetched data
    if (covidData != None):
    #converting data into JSON format
        data = covidData.json()
        # print(data)
        for centre in data['centers']:
            for sessions in centre['sessions']:
                if sessions['available_capacity']>0:
                    print(centre['name'])
                    print(sessions['date'], sessions['available_capacity'])
                    notification.notify(
                        title='Vaccine available',
                        message="visit https://www.cowin.gov.in/home"
                    )
                    exit()
        # todo: add notification
except:
    #if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")