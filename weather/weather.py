"""This Module have class to perform all calculation realted to weather"""
import calculation

class WeatherCalculation(calculation.Computation):

    """class object takes data in form of dictionary and apply functions on it"""
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def min_spread_day(self):
        """Function Return day on with temp diffrence is minimum"""
        min_value = self.compute_min_value(self.weather_data)
        min_value_key = self.compute_min_value_key(min_value, self.weather_data)
        return min_value, min_value_key
