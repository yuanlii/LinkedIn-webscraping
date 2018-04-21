import plotly.plotly as py
import plotly.graph_objs as go


def VisualizeWithTable():

	trace = go.Table(
	    header=dict(values=['Greater Philadelphia Area', 'Greater Detroit Area','San Francisco Bay Area']),
		cells=dict(values=[[6,4],
	                       [33,10],
	                       [106,95] #degree(higher than bachelor's degree)
	                       ]))
	data = [trace] 
	py.plot(data, filename = 'visual_table')


if __name__ == "__main__":
  
  # location_dict = {}
  # location_dict['Greater Philadelphia Area'] = 6
  # location_dict['Greater Detroit Area'] = 33
  # location_dict['San Francisco Bay Area'] = 106
	VisualizeWithTable()