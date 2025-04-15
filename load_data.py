def load_data(file):
    hours = []
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if line: 
                    date, hour = line.split() 
                    hours.append((date, hour))

    except FileNotFoundError:
        print("There is no config file")
    except Exception as e:
        print(f"ERROR {e}")
    return hours
