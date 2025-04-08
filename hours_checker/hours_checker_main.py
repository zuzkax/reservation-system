from fetch import fetch_data
from load_data import load_data
from auth import auth
from reservation import reservation
from check import check

#change user authenticators
login = "example.email@gamil.com"
password = "password"
#change input file directorie
input_file = "C:\example\directorie\input.txt"

avaiable_slots = fetch_data()
if not avaiable_slots:
    print("Brak wolnych godzin w najblizszym czasie")
    exit()

user_slots = load_data(input_file) 
if not user_slots:
    print("Nie podano preferowanych godzin")
    exit()
print(user_slots)

matching_slots = check(avaiable_hours=avaiable_slots, user_hours=user_slots)
if not matching_slots:
    print("Brak pasujacych godzin")
    exit()

access_token = auth(login,password)
if not access_token:
    print("Blad funkcji auth()")
    exit()

for date, hour in matching_slots:
    print(f"Znaleziono pasujaca godzine {date}, {hour}")
    print("Rozpoczynam rezerwacje...")
    reservation(date, hour, access_token)
