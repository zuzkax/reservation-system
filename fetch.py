import requests
import json

def fetch_data():
    url = "https://api..." #api endpoint for checking court occupancy 

    headers = { #here paste your request headers 
        "Host": "api....",
        "Sec-Ch-Ua-Platform": "",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "",
        "Sec-Ch-Ua": "",
        "X-Tenis-User-Agent": "",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "",
        "Origin": "",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() #checking for http errors
        data = response.json()
        formated_data = []
        for station in data.get("stations", []):
            for day in station.get("days", []):
                date = day.get("date")  
                free_hours = day.get("free_hours", [])

                for hour in free_hours:
                    begin_time = hour.get("begin_time")

                    if begin_time:
                        formated_data.append({"date": date, "time": begin_time})

        return formated_data
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error; {e}")
    except json.JSONDecodeError as e:
        print(f"Bad json from server")
    return None

