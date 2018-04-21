import plotly.plotly as py
import plotly.graph_objs as go

# bar chart [show different locations]

def VisualizeWithBarchart(location_dict):
  location_names =[]
  location_nums =[]

  for location in location_dict:
    location_names.append(location[0])
    location_nums.append(location[1])

  data = [go.Bar(
              x=location_names,
              y=location_nums
      )]

  py.plot(data, filename='location-bar')



if __name__ == "__main__":
  
  location_dict = {}
  location_dict['Greater Philadelphia Area'] = 6
  location_dict['Greater Detroit Area'] = 33
  location_dict['San Francisco Bay Area'] = 106

  VisualizeWithBarchart(location_dict)

