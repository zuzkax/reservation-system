import requests

def auth(login, password):
    url = "https://api..."  #rndpoint for authentication

    headers = { #check your headers and paste it here
        "Host": "",
        "Sec-Ch-Ua-Platform": "",  
        "Authorization": "",  #
        "Accept-Language": "",
        "Sec-Ch-Ua": "",  
        "X-Tenis-User-Agent": "",
        "Sec-Ch-Ua-Mobile": "?0", 
        "User-Agent": "",
        "Accept": "",
        "Content-Type": "",
        "Origin": "",
        "Sec-Fetch-Site": "",
        "Sec-Fetch-Mode": "",
        "Sec-Fetch-Dest": "",
        "Referer": "",
        "Accept-Encoding": "",
        "Priority": "",
        "Connection": ""

    }

    data = {
        "grant_type": "password",
        "username": login,
        "password": password
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        payload = response.json()
        access_token = payload.get('access_token')

        if access_token:
            print("TOKEN: ", access_token)
            return access_token
        else:
            print("Cant obtain token")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Login error: {e}")
        return None
