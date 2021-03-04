To run this program, you need to have python, docker, pipenv and sqlalchemy installed. Python comes with pip which can be used to install some of the dependencies.

Command Line Prerequisites

Run the following commands:
pip install pipenv 
pipenv --three  

Create a docker database with the following command:
docker run --name stopwatch-db \
    -e POSTGRES_PASSWORD=watch \
    -e POSTGRES_USER=stop \
    -e POSTGRES_DB=sqlalchemy \
    -p 5432:5432 \
    -d postgres
    
Install the dependencies with the following command:
pipenv install sqlalchemy psycopg2

Start the virtual environment with the command: pipenv shell

In the Docker GUI, ensure the database is running.

Running the Browser Page
Within an IDE, open and run the file Presentation/approute.py
This activates the web server. It runs locally on your computer. Point your web browser to the following URL:  localhost:5000. You will now see the stopwatch webpage.
Unfortunately this page is not working correctly with the rest of the application. Ideally, the template named layout.html would contain JavaScript which links the python scripts to the html file. 

Using the Mock UI
Since our web page buttons are not functional, we have made a mock UI which simulates user interaction with a stopwatch in the command line. Run mock_ui.py. Pressing enter starts the count, pressing it once more stops it. The app displays the time between the presses, displays the value, records the data to the database, then lastly queries the database. 

