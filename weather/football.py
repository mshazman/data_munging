"""This Module have class to perform all calculation realted to Football"""
import calculation

class FootballCalculation(calculation.Computation):

    """class object takes data in form of dictionary and apply functions on it"""
    def __init__(self, team_data):
        self.team_data = team_data

    def goal_difference(self):
        """Function Return day on with temp diffrence is minimum"""
        min_value = (self.compute_min_value(self.team_data))
        min_value_key = self.compute_min_value_key(min_value, self.team_data)
        return min_value, min_value_key
