from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

def get_value(x):
    return x.value

list_of_years = list(map(get_value, sheet['A'][1:]))
list_of_temperature = list(map(get_value, sheet['C'][1:]))
list_of_activity = list(map(get_value, sheet['D'][1:]))

pyplot.plot(list_of_years, list_of_temperature, label="first")
pyplot.plot(list_of_years, list_of_activity, label='second')
pyplot.legend()
pyplot.show()