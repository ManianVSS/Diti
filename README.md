# Diti
Test Automation Step Repository and Test Composer

### **Development Setup**

##### **Installing python dependencies on Ubuntu**<br>

##### **Pre-Requisites**</br>
Python 3, pip and libpq-dev </br>
> sudo apt install libpq-dev</br>
> cd diti_server</br>
> pip install -r requirements.txt</br>

##### **Creating and Migrating DB Schema**</br>

> cd diti_server</br>
> ./migrate.sh</br>

##### **Running server**

> cd diti_server</br>
> ./runserver.sh</br>

Admin console should be up on http://localhost:8000/admin

### **Production Setup**

##### **Installing python dependencies and postgres on Ubuntu**<br>
Note: Create files referring to the .example files in root directory</br>
##### **Pre-Requisites**</br>
Python 3, pip , postgres database and libpq-dev </br>
> sudo apt install libpq-dev</br>
> cd diti_server</br>
> pip install -r requirements.txt</br>

##### **Creating Postgres production DB and schema one time**</br>

> ./createdb.sh

##### **Migrating DB Schema for changes**</br>

> ./migrate.sh

##### **Running server**</br>

> ./runserver.sh

Admin console should be up on http://localhost:8000/admin
