"""Main module to run the project"""
from reader import ReadData
from weather import WeatherCalculation
from football import FootballCalculation

def display_min_spread_day(file):
    """Function To display minimum spread day"""
    weather_data_reader = ReadData(file)
    weather_data = weather_data_reader.get_data(0, 1, 2)
    weather_cal = WeatherCalculation(weather_data)
    min_temp_spread = weather_cal.min_spread_day()
    print(f"\nMinimum Spread day is {min_temp_spread[1]}\
    with temprature differece {min_temp_spread[0]}")

def display_min_goal_diff_team(file):
    """Function to print team with minimum goal difference """
    team_data_reader = ReadData(file)
    team_data = team_data_reader.get_data(1, 6, 8)
    team_data_cal = FootballCalculation(team_data)
    min_diff_team = team_data_cal.goal_difference()
    print(f"\nMinimum Goal differnce is {min_diff_team[0]} by team {min_diff_team[1]}\n")


display_min_spread_day('weather.dat')
display_min_goal_diff_team('football.dat')
