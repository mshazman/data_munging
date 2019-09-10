import re

def get_data(file):
    weather_data = {}
    with open(file) as weather_file:
        days = weather_file.readlines()
        for day in days[2:len(days)-1]:
            day = day.split()
            day[1] = re.sub("[*]", "", day[1])
            day[2] = re.sub("[*]", "", day[2])
            weather_data[day[0]] = int(day[1])-int(day[2])
    return weather_data

def display_data(weather_data):
    min_value = min(weather_data.values())
    min_temp_spread_day = ''
    for day in weather_data:
        if weather_data[day] == min_value:
            min_temp_spread_day = day
            break
    return min_temp_spread_day

print(display_data(get_data('weather.dat')))