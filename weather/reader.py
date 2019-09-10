"""This Module Contain Class To read Data from data file"""
import re


class ReadData():
    """This class object takes data file and return desired data in form of dictionary"""

    def __init__(self, file):
        self.file = file

    def get_data(self, key, index_first, index_second):
        """This method will read data from File and return list of dictionary with
        max and min temp"""
        data = {}
        with open(self.file) as weather_file:
            days = weather_file.readlines()
            for day in days[2:len(days)-1]:
                day = day.split()
                try:
                    day[index_first] = re.sub("[*]", "", day[index_first])
                    day[index_second] = re.sub("[*]", "", day[index_second])
                    data[day[key]] = [(day[index_first]), (day[index_second])]
                except Exception:
                    pass
        return data
