from flask import Flask, render_template, request

# import CSV file
with open(csv_file_name) as f:
    reader = csv.reader(f)
    next(reader) # throw away headers
    next(reader) # throw away headers
    global bb_seasons
    bb_seasons = [] # reset, start clean
    for r in reader:
        r[3] = int(r[3])
        r[4] = int(r[4])
        r[5] = float(r[5])
        bb_seasons.append(r)


# writing app
app = Flask(__name__)

@app.route('/')
def hello_world():
    my_list = ['one', 'two', 'three']
    return render_template('list.html', title="Numbers", my_list=my_list)



@app.route('/bball', methods=['GET', 'POST'])
def bball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_bball_seasons(sortby, sortorder)
    else:
        seasons = model.get_bball_seasons()
        
    return render_template("seasons.html", seasons=seasons)



def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list


if __name__ == '__main__':
    model.init_bball()
    app.run(debug=True)

