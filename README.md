# local docker - game score board 
it will run on your terminal.. to check if all the func are work properly


```
sudo apt install docker -y
docker --version
git clone https://github.com/Roiko96/docker.git
cd docker
sudo systemctl enable docker
sudo systemctl start docker
sudo docker build -t gamescoreboard-app .
sudo docker run -it gamescoreboard-app
sudo docker ps -a
sudo docker images
```

***enjoy***
