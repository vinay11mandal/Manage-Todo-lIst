# TODO LIST

#### Description
Rest Api's for Managing the Todo List.

#### Tools and technologies
Language: Python 3.6
Framework: Django 2.2
Database: Postgres 11.5 (RDS)
API: Django rest framework
Code Repository : Gitlab
API test tool: Swagger
Containerization: Docker

#### Install Docker into ubuntu
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo systemctl status docker
```

#### Application run  into local.
1. Take a clone of the repo using https.
```
git clone https://gitlab.com/vinay11mandal/todo-list.git
```

2. Install docker compose
```
sudo apt install docker-compose
```
Run below to commands

```
sudo docker-compose -f docker-compose-prod.yml build
```

```
sudo docker-compose -f docker-compose-prod.yml up --no-build
```
or for running the process in background run

```
sudo docker-compose -f docker-compose-prod.yml up --no-build -d
```

4. Open URL into the browser.
```
http://0.0.0.0:8000
```
5. API test and doc's
```
http://0.0.0.0:8000/swagger/
http://0.0.0.0:8000/redoc/
```

