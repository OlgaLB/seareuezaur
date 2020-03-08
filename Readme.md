## Installation  

Install Python3 if it's not yet there.  
To do this on Ubuntu, run:  
  
sudo apt-get update  
sudo apt-get -y install python3.7  
  
For more details or other OSs please follow the documentation:  
https://docs.python.org/3/using/unix.html  
https://docs.python.org/3/using/windows.html  
  
Install PIP if it's not yet there. To do this on Ubuntu, run:  
  
sudo apt-get update  
sudo apt-get -y install python3-pip  

For more details please follow the documentation:  
https://pip.pypa.io/en/stable/installing/  

Install MySQL. To do this on Ubuntu, run:  
sudo apt-get install mysql-server  
For more information, please follow:
https://support.rackspace.com/how-to/install-mysql-server-on-the-ubuntu-operating-system/  
or  
https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/linux-installation.html  

For the details for others OS please follow:  
https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation.html  
https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/windows-installation.html  
https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/solaris-installation.html  

Install flask, flask-cors, mysql-connector-python, pytest, requests if they are not yet there.  

To do this, either run:  

sudo pip3 install -r requirements.txt  

Or, on Ubuntu, run:  

sudo pip3 install flask  
sudo pip3 install -U flask-cors  
sudo pip3 install mysql-connector-python  
sudo pip3 install pytest  
sudo pip3 install requests  

Or:
sudo pip3 install -r requirements.txt

For more details please follow:  
https://pypi.org/project/Flask/  
https://pypi.org/project/mysql-connector-python/  
https://pypi.org/project/pytest/  
https://pypi.org/project/requests/  
https://flask-cors.readthedocs.io/en/latest/

## Endpoints

To search by IATA use the following endpoint:  
### /api/IATA'  
method: 'GET'  
input parameter: iata  
output parameter: array of jsons  
Example:  
http://127.0.0.1:5000/api/IATA?iata=oca  

To search by name use the following endpoint:  
### /api/name'  
method: 'GET'  
input parameter: name  
output parameter: array of jsons  
Example:  
http://127.0.0.1:5000/api/name?name=tegel  

## Running tests

Please note that better to use a separate test database for testing.  
Go to tests folder, run:  
pytest endpoint_name_tests.py  
or  
pytest -v endpoint_name_tests.py  
and  
pytest endpoint_iata_tests.py  
or  
pytest -v endpoint_iata_tests.py  

## Running application locally

Go to lib/credentials.py and update the username and password of MySQL admin user, as well as username and password of the application user. If you update application username or database name, update also the appropriate queries in db/airports_db_v1.0.0.sql.  
From the current directory, run:  
python3 main.py  
to create and populate the database.  
Then, run:  
python3 api.py  
Then it's possible to observe URL and error codes, if any, in the console, and run requests for airports search in the web browser.  

## Running application on image

_Please note: MySQL configuration changes should be added. These is not fully supported with the current version. After all configurations are completed in the Dockerfile, please follow the steps below._
From the current directory, run:  
docker build --tag=airports_search .  
docker run airports_search:latest
