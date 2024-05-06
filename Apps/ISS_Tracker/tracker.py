import os
import smtplib
from datetime import datetime
from dotenv import load_dotenv
import requests

ISS_URL = "http://api.open-notify.org/iss-now.json"
SUN_URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 18.597059
MY_LONG = 73.718826

api_response = requests.get(url=ISS_URL)
api_response.raise_for_status()
iss_position = api_response.json()['iss_position']

# Sample Request : https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
sun_response = requests.get(url=SUN_URL, params=parameters)
sunrise = sun_response.json()['results']['sunrise']
sunset = sun_response.json()['results']['sunset']

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
current_hour = datetime.now().hour


def is_iss_overhead():
    if (MY_LAT - 5 <= float(iss_position['latitude']) <= MY_LAT + 5) \
            and (MY_LONG - 5 <= float(iss_position['latitude']) <= MY_LONG + 5):
        print('Overhead !')
        return True


def is_night():
    if sunset_hour <= current_hour <= sunrise_hour:
        print('Its Night !')
        return True


is_iss_overhead()

# TODO : If ISS is close to my position, and its dark -> send an email to tell me look up.
load_dotenv()
# Gathering My Secrets from environment variables, .gitignore has ignored .env file
my_email = os.getenv("MY_EMAIL")
app_pwd = os.getenv("APP_PASSWORD")  # Application Password for mail.
# while True:
if is_iss_overhead():
    # TODO: Establish connection using Short Message Transfer Protocol
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # TODO: Secure connection to mail server -> start Transport layer security; starttls()
        connection.starttls()
        # TODO: Login to mail
        connection.login(user=my_email, password=app_pwd)
        # TODO: Send Email
        # msg="Subject:Subject\n\nMail body
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: LookUp !! !!\n\nSpot the ISS ! It's crossing above you right now!!")
