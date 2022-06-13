from flask import Flask, render_template, url_for


#create the object of Flask
app  = Flask(__name__)

#creating our routes
@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/cv')
def CV():
    return render_template('cv.html')

@app.route('/akita_aboutcopy')
def akita_aboutcopy():
    return render_template('akita_aboutcopy.html')    

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/cv_copy')
def cv_copy():
    return render_template('cv_copy.html')

@app.route('/mythology_greek')
def mythology_greek():
    return render_template('mythology_greek.html')


@app.route('/akita_furtherreading')
def Further_Reading():
    return render_template('akita_further_reading.html')

@app.route('/engineering_tools')
def engineering_tools():
    return render_template('engineering_tools.html')

@app.route('/engineering_hazardous_area_tool')
def engineering_hazardous_area_tool():
    return render_template('engineering_hazardous_area_tool.html')

#run flask app
if __name__ == "__main__":
    app.run(debug=True)