import os
from datetime import datetime
from datetime import timezone
import sys
app_dir = os.path.dirname(__file__)
sys.path.append(app_dir)
import requests
from user import User
from db import DB
import dotenv
import re
import json

dotenv.load_dotenv(".env")

city_file = open("/home/pavan/gitclones/weather-cli/app/city.list.json", "r")
city_data = json.loads(city_file.read())
city_file.close()

def print_intro():
    print(" __      __                  __    __                        _________   __    __  ",
          "/  \\    /  \\  ____  _____  _/  |_ |  |__    ____ _______     \\_   ___ \\ |  |  |__| ",
          "\\   \\/\\/   /_/ __ \\ \\__  \\ \\   __\\|  |  \\ _/  __ \\_  __ \\    /    \\  \\/ |  |  |  | ",
          " \\        / \\  ___/  / __ \\_|  |  |   Y  \\\\  ___/ |  | \\/    \\     \\____|  |__|  | ",
          "  \\__/\\  /   \\___  >(____  /|__|  |___|  / \\___  >|__|        \\______  /|____/|__| ",
          "       \\/        \\/      \\/            \\/      \\/                    \\/            ", sep="\n")
    print("\t==========================")

def get_coords(query):
    pattern = r'([a-zA-z]+)|(((\d+\.\d+)|(\d+)) ((\d+\.\d+)|(\d+)))'
    match = re.match(pattern, query)
    if match:
        if match.group(1) is not None:
            name = match.group(1)
            for city in city_data:
                if city['name'] == name:
                    return city['coord']['lat'], city['coord']['lon']
            return match.group(1)
        else:
            return list(map(float, match.group(2).split()))
    else:
        return None

def match_date(data, date):
    for day in data['daily']:
        day_timestamp = datetime.fromtimestamp(day['dt'], timezone.utc).date()
        if day_timestamp == date:
            return day
    return None

def call_api():
    query = input("\tEnter Location name/[latitude longitude]: ")
    date_str = input("\tEnter date in YYYY-MM-DD format: ")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    cords = get_coords(query)
    if cords is None:
        print("\tInvalid location")
        return
    lat, lon = cords
    api_key = os.environ.get("API_KEY")
    url = os.environ.get("API_URL").format(lat, lon, api_key)
    print("\tFetching data...")
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        weather_data = match_date(data, date_obj)
        if weather_data is None:
            print("\tDate exceedes the range of data")
            return
        print("\tHumidity: {}".format(weather_data['humidity']))
        print("\tPressure: {}".format(weather_data['pressure']))
        temp = weather_data['temp']
        print("\tAverage temperature: {}K".format((temp['min'] + temp['max']) / 2))
        print("\tWind Speed: {}".format(weather_data['wind_speed']))
        print("\tWind Direction: {}".format(weather_data['wind_deg']))
        print("\tUV Index: {}".format(weather_data['uvi']))
    else:
        print("\tError fetching data")


def print_menu(adminMenu):
    print("\tMain Menu")
    print("\t==========")
    print("\t1. Print This Menu")
    print("\t2. Weather Data")
    if adminMenu:
        print("\t3. View All users")
        print("\t4. Add user")
        print("\t5. Delete user")
        print("\t6. Change user password")
        print("\t7. Logout")
    else:
        print("\t3. Change password")
        print("\t4. Logout")

def run_choice(user):
    choice = input("\n\tEnter your choice: ")
    print()
    if choice == "1":
        print_menu(user.isAdmin)
    elif choice == "2":
        call_api()
    else:
        if user.isAdmin:
            if choice == "3":
                user.showUsers()
            elif choice == "4":
                uName = input("\tEnter username: ")
                uPass = input("\tEnter password: ")
                res = user.addUser(uName, uPass)
                if res:
                    print("\tUser added successfully")
                else:
                    print("\tFailed to add user")
            elif choice == "5":
                uName = input("\tEnter username: ")
                res = user.deleteUser(uName)
                if res:
                    print("\tUser deleted successfully")
                else:
                    print("\tFailed to delete user")
            elif choice == "6":
                res = user.changePassword()
                if res:
                    print("\tPassword changed successfully")
                else:
                    print("\tFailed to change password")
            elif choice == "7":
                exit(0)
            else:
                print("\tInvalid choice\n")
                print_menu(user.isAdmin)
        else:
            if choice == "3":
                res = user.changePassword()
                if res:
                    print("\tPassword changed successfully")
                else:
                    print("\tFailed to change password")
            elif choice == "4":
                exit(0)
            else:
                print("\tInvalid choice")
                print_menu(user.isAdmin)

def runtime():
    print_intro()
    uName = input("\tEnter your username: ")
    uPass = input("\tEnter your password: ")
    if uName == "":
        print("\tUsername cannot be empty")
        return runtime()
    user = User(uName)
    if user.login(uPass):
        print("\tLogin successful\n")
        print_menu(user.isAdmin)
        while True:
            run_choice(user)
    else:
        print("\tLogin failed\n")
        return runtime()

if __name__ == "__main__":
    runtime()
