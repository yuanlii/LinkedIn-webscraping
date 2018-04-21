import plotly
import plotly.plotly as py
import plotly.graph_objs as go


def VisualizeWithPiechart(location_dict):

	labels = []
	values = []

	for location in location_dict:
		labels.append(location)
		values.append(location_dict[location])

	trace = go.Pie(labels=labels, values=values)
	py.plot([trace], filename='basic_pie_chart')


# if __name__ == "__main__":
  
#   location_dict = {}
#   location_dict['Greater Philadelphia Area'] = 6
#   location_dict['Greater Detroit Area'] = 33
#   location_dict['San Francisco Bay Area'] = 106

#   VisualizeWithPiechart(location_dict)