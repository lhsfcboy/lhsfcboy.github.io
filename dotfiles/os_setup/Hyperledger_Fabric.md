# pass

## Fabric v1.4

- Writing Your First Application
  - <https://hyperledger-fabric.readthedocs.io/en/release-1.4/write_first_app.html>
- Hyperledger Fabric v1.4 のプログラミングモデル
  - <https://www.ibm.com/developerworks/jp/cloud/library/cl-hyperledger-fabric-basic-6/index.html>

### Prerequisites

- Go version 1.11.x is required.

```text
npm install npm@5.6.0 -g
```

### FabCar
```text
curl -sSL http://bit.ly/2ysbOFE | bash -s 1.4.0
cd fabric-samples
cd fabcar

./startFabric.sh javascript
docker ps --format "{{.Names}}"
    dev-peer0.org1.example.com-fabcar-1.0
    cli
    peer0.org1.example.com
    couchdb
    orderer.example.com
    ca.example.com
cd javascript
npm install
node enrollAdmin.js
node registerUser.js
```
