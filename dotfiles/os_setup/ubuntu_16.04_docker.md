

## Docker Community Edition

<https://docs.docker.com/install/linux/docker-ce/ubuntu/>

```text
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -    
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get -y install docker-ce docker-ce-cli containerd.io
sudo docker run hello-world
```

## Docker Compose

```text
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
#docker compose会自动安装所依赖的python2.7
python -V #检查是否是2.7
```

## Node.js 6.x npm

```text
curl -sL https://deb.nodesource.com/setup_6.x | sudo bash -
sudo apt install nodejs
node -v
npm -v
```

## Basic Dev Tools

```text
sudo apt-get install git
sudo apt -y install make gcc g++ libtool
```

