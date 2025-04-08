from auth import auth
from reservation import reservation
from load_data import load_data

#change user authenticators
login = "example.email@gmail.com" 
password = "password" 
#change input file directorie
file = "C:\example\directorie\input.txt" 

access_token = auth(login, password)
hours_set = load_data(file)
date = list(hours_set)[0][0]
hour = list(hours_set)[0][1]

reservation(date, hour, access_token)
