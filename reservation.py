import requests
from datetime import datetime, timedelta

def reservation(date, time, access_token):
    date = date.replace("/", "-")
    #ISO 8601
    start_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
    end_time = start_time + timedelta(hours=1)

    print(start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z"))
    print(end_time.strftime("%Y-%m-%dT%H:%M:%S.000Z"))

    data = { #paste here your reservation data from captured package
        "starts_at": start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "ends_at": end_time.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "station_id": "",
        "payment_method": "",
        "tariff_id": , #int
        "multisport_cards": 0,
        "medicover_cards": 0,
        "lightning": True, # or False
        "message": "",
        "przelewy24_return_url": ""

    }
    headers = { 
          #paste here your headers
    }

    url = "" #endpoit for reservation

  
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print("Success!", response.json())

    except requests.exceptions.RequestException as e:
        print(f"Reservation error: {e}")
        if response is not None:
            print(response.text)
        raise
