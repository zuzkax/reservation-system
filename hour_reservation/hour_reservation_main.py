from auth import auth
from reservation import reservation
from load_data import load_data

#change user authenticators
login = "example.email@gmail.com" 
password = "password" 
#change input file directorie
file = "C:\example\directorie\input.txt" 

access_token = auth(login, password)
try:
    hours = load_data(file)
    print(f"Hours have been imported from the input file: {hours}")
except Exception as e:
    print(f"Error while loading data from the file: {e}")
    exit(1)

for i in range(len(hours)):
    date = hours[i][0]
    hour = hours[i][1]
    try:
        reservation(date, hour, access_token)
        break
    except Exception as e:
        print((f"Failed to make reservation for {date} at {hour}: {e}"))try:
