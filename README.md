## docker - game score board 

# run in cli
```
sudo apt install docker -y
docker --version
git clone https://github.com/Roiko96/docker
cd docker
sudo systemctl enable docker
sudo systemctl start docker
sudo docker build -t gamescoreboard-app .
sudo docker run -it gamescoreboard-app

```
# run in localhost :
```
sudo docker build -t gamescoreboard-app .
sudo docker run -p 5000:5000 gamescoreboard-app


```
* URL : http://localhost:5000

***enjoy***
