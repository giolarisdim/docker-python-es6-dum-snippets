# forex api documentation

Docker Client:

Version:           18.06.1-ce

API version:       1.38

Mongo version 3.6.7



the first 8 steps will install docker and docker compose to our system
those can be found here too:
* ` https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository`
* ` https://docs.docker.com/compose/install/#prerequisites`


copy paste in terminal of forex dir


*  ` sudo apt-get update`

 
*  ` sudo apt-get install     apt-transport-https     ca-certificates     curl     software-properties-common`


*  ` curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

  (this must give an OK)


*  ` sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test"
sudo apt update
sudo apt install docker-ce`


*  ` sudo docker run hello-world`


*  ` sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`


*  ` sudo chmod +x /usr/local/bin/docker-compose`


*  ` docker-compose --version`


*  ` sudo apt install python-pip`


*  ` pip install bcrypt`


*  ` sudo docker-compose build`


*  ` sudo docker-compose up`


in ubuntu apps open postman - 
set up steps above:
*  ` http://ubuntuhandbook.org/index.php/2018/09/install-postman-app-easily-via-snap-in-ubuntu-18-04/`


time to make some tests with postman

 
with POST selected in postman we hit:

localhost:5000\here we put our routes like ---->>
` localhost:5000\register`

in postman we choose the "body" with "raw" data and "JSON(application/json)" then we hit above 

{
	"username": "yourusername",
	"password": "yourpassword"
}

those will return 

{
    "msg": "You successfully signed up for the API",
    "status": 200
}


in this case we will see how much we take for 50 usd 

* ` localhost:5000/usdtoeuro` OR 
* ` localhost:5000/usdtogbp`

{
	"username": "yourusername",
	"password": "yourpassword",
	"x": 50
}

those will return a msg with the amount you take at this moment 

{
    "msg": 43.685,
    "status": 200
}
