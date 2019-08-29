# pass

<https://hyperledger-fabric.readthedocs.io/en/release-1.4/install.html>

## Prepare

```text
mkdir fabric
cd fabric
curl -sSL https://goo.gl/kFFqh5 | sudo bash -s 1.0.6

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
