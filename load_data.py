def load_data(file):
    hours = set()
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if line: 
                    date, hour = line.split() 
                    hours.add((date, hour))

    except FileNotFoundError:
        print("There is no config file")
    except Exception as e:
        print(f"ERROR {e}")
    return hours
