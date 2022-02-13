import requests


def main():
    choice = input("[R]eport weather or [S]ee reports? ")
    while choice:
        if choice.lower().strip() == "r":
            report_evet()
        elif choice.lower().strip() == "s":
            see_events()
        else:
            print(f"Don't know what to do with this{choice}.")
        choice = input("[R]eport weather or [S]ee reports? ")


def report_evet():
    desc = input("What is happening? ")
    city = input("What city? ")

    data = {"description": desc, "location": city}

    url = "http://127.0.0.1:8000/api/report"
    resp = requests.post(url, json=data)
    resp.raise_for_status()

    result = resp.json()
    print(f"Reported new event: {result.get('id')}")


def see_events():
    url = "http://127.0.0.1:8000/api/all_reports"
    res = requests.get(url)
    res.raise_for_status()

    data = res.json()
    print(data)

    for r in data:
        print(f"{r.get('location')} has {r.get('description')}")


if __name__ == "__main__":
    main()
