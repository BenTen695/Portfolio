Powershell terminal commands using Windows

py -3 -m venv venv
venv\Scripts\activate
pip3 install -r requirements.txt
pip install Flask
$env:FLASK_ENV = "development"
flask run
---------------------------------------------


launch the following commands:

``` bash
# Setup virtual environment
virtualenv venv -p python3;
source venv/bin/activate;

# Install python dependencies
pip install -r requirements.txt;

# Install npm modules
cd application/static/assets;
npm install;
cd -;

# Run the application
export FLASK_APP="application.app";
export FLASK_DEBUG="True"
flask run;  # localhost:5000
```

The application should be running locally on
[localhost:5000](http://localhost:5000)