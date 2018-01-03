from Pubnub import Pubnub

## Initiat Class
pubnub = Pubnub( None, 'sub-c-52a9ab50-291b-11e5-baaa-0619f8945a4f', None, False )

## History Example
history = pubnub.history({
    'channel' : 'lightning_executions_BTC_JPY',
    'limit'   : 1
})
print(history)

