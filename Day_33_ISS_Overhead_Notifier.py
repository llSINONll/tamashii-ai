#Challenge 1(ISS Overhead Notifier)
'''
🌍 Scenario:
Imagine being notified whenever the International Space Station (ISS) is
passing overhead during nighttime at your location.
This project will teach you how to interact with APIs and
automate notifications based on real-time data.

🧠 What You'll Learn:
How to make API requests using the requests library.

Parsing JSON data from API responses.

Working with date and time using the datetime module.

Automating tasks based on specific conditions.

🔧 Tools & Libraries:
requests: To make HTTP requests to APIs.

datetime: To work with dates and times.

smtplib: To send email notifications (optional).

📌 Steps to Implement:
Get Your Location Coordinates:

Determine your latitude and longitude. For example, Indore, Madhya Pradesh, India has:

MY_LAT = 22.7196
MY_LONG = 75.8577
Check ISS Position:

Use the Open Notify API to get the current position of the ISS:

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
Determine If ISS Is Overhead:

Check if the ISS is within ±5 degrees of your location:

if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
    # ISS is overhead
Check If It's Nighttime:

Use the Sunrise-Sunset API to determine if it's currently dark at
your location:

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.datetime.now().hour

if time_now >= sunset or time_now <= sunrise:
    # It's dark
Send Notification:

If the ISS is overhead and it's dark, send yourself an email notification (optional).

Automate the Check:

Use a loop to check every 60 seconds:

while True:
    time.sleep(60)
    # Repeat the above checks
🧪 Sample Output:

Subject: Look Up!

The ISS is currently overhead your location. Go outside and take a look!
'''

import requests
from datetime import datetime
import time

# Your coordinates (example: Jabalpur, India)
MY_LAT = 23.1815
MY_LONG = 79.9864

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is within ±5 degrees
    return (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow().hour  # Use UTC for accuracy

    return time_now >= sunset or time_now <= sunrise

# 🔁 Keep checking every 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("🔭 Look up! The ISS is currently overhead your location!")
