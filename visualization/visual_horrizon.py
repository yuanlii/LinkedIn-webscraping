import plotly.plotly as py
import plotly.graph_objs as go

def VisualizeHorizontal():

	data = [go.Bar(
	            x=[6, 33, 106],
	            y=['Greater Philadelphia Area', 'Greater Detroit Area', 'San Francisco Bay Area'],
	            orientation = 'h'
	)]

	py.plot(data, filename='horizontal-bar')



if __name__ == "__main__":
  
  # location_dict = {}
  # location_dict['Greater Philadelphia Area'] = 6
  # location_dict['Greater Detroit Area'] = 33
  # location_dict['San Francisco Bay Area'] = 106
	VisualizeHorizontal()