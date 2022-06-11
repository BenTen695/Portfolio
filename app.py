from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

# routes
@app.route("/")
def Index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/akita about')
def akita_about():
    return render_template('akita_about.html')

@app.route('/akita further reading')
def akita_further_reading():
    return render_template('akita_further_reading.html')

@app.route('/engineering hazardous area tool')
def engineering_hazardous_area_tool():
    return render_template('engineering_hazardous_area_tool.html.html')

@app.route('/engineering tools')
def engineering_tools():
    return render_template('engineering_tools.html')
# /Routes