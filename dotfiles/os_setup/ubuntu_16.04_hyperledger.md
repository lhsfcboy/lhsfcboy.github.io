# pass

<https://hyperledger-fabric.readthedocs.io/en/release-1.4/install.html>

## Prepare

```text
mkdir fabric
cd fabric

#latest production release
curl -sSL http://bit.ly/2ysbOFE | bash -s
# specific release
curl -sSL https://goo.gl/kFFqh5 | sudo bash -s 1.0.6
# <fabric_version> <fabric-ca_version> <thirdparty_version>
curl -sSL http://bit.ly/2ysbOFE | bash -s -- 1.4.3 1.4.3 0.4.15

echo 'export PATH=$PATH:$HOME/fabric/bin' >> ~/.profile
echo $PATH
. ~/.profile

# Download Sample
git clone https://github.com/hyperledger/fabriccd fab-samples.git -b v1.0.6
```

## Run fabcar

```text
cd fabric-samples/fabcar
npm install
./startFabric.sh
```
