"""This module have class to Compute common task related to weather and football"""
class Computation():
    """class to Compute common task related to weather and football """
    def compute_min_value(self, data):
        """Function will take two coloumn fetched from read data and return min value"""
        for key in data:
            data[key] = abs(int(data[key][0]) - int(data[key][1]))
        min_value = min(data.values())
        return min_value

    def compute_min_value_key(self, min_value, data):
        """Takes Two parameters min_value and dictionary and return key
        associated to minimum value"""
        min_value_key = ''
        for key in data:
            if data[key] == min_value:
                min_value_key = key
                break
        return min_value_key
