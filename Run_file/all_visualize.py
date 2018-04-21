from visual_barchart import *
from visual_piechart import *
from visual_table import *
from visual_horrizon import *

def VisualizeWithUserPrompt():
	user_input = input("which visualization? 1,2,3,4\n")
	if user_input == str(1):
		# bar chart
		location_dict = {}
		location_dict['Greater Philadelphia Area'] = 6
		location_dict['Greater Detroit Area'] = 33
		location_dict['San Francisco Bay Area'] = 106

		VisualizeWithBarchart(location_dict)

	elif user_input == str(2):
		# pie chart
		location_dict = {}
		location_dict['Greater Philadelphia Area'] = 6
		location_dict['Greater Detroit Area'] = 33
		location_dict['San Francisco Bay Area'] = 106

		VisualizeWithPiechart(location_dict)

	elif user_input == str(3):
		# table
		VisualizeWithTable()

	elif user_input == str(4):
		# horrizon chart
		VisualizeHorizontal()


if __name__ == "__main__":

	VisualizeWithUserPrompt()