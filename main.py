from fetch import fetch_data
from load_data import load_data
from auth import auth
from reservation import reservation
from check import check

#enter your data
login = ""
password = ""
input_file = ""

avaiable_slots = fetch_data()
if not avaiable_slots:
    print("No available dates")
    exit()


user_slots = load_data(input_file) 
if not user_slots:
    print("No preferred hours given")
    exit()

matching_slots = check(avaiable_hours=avaiable_slots, user_hours=user_slots)
if not matching_slots:
    print("No matching dates and hours")
    exit()

access_token = auth(login,password)
if not access_token:
    print("auth() error")
    exit()

for date, hour in matching_slots:
    print(f"Found matching date and hour {date}, {hour}")
    print("Starting reservation...")
    reservation(date, hour, access_token)
