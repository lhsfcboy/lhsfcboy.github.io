# http://pubsub.pubnub.com/v2/history/sub-key/sub-c-52a9ab50-291b-11e5-baaa-0619f8945a4f/channel/lightning_executions_BTC_JPY

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub_tornado import PubNubTornado
from pubnub.pnconfiguration import PNReconnectionPolicy

import json
import pymongo
import time

class Pubnub():
    def __init__(
        self,
        publish_key,
        subscribe_key,
        secret_key = False,
        ssl_on = False,
        origin = 'pubsub.pubnub.com'
    ) :
        """
        #**
        #* Pubnub
        #*
        #* Init the Pubnub Client API
        #*
        #* @param string publish_key required key to send messages.
        #* @param string subscribe_key required key to receive messages.
        #* @param string secret_key required key to sign messages.
        #* @param boolean ssl required for 2048 bit encrypted messages.
        #* @param string origin PUBNUB Server Origin.
        #**
        ## Initiat Class
        pubnub = Pubnub( 'PUBLISH-KEY', 'SUBSCRIBE-KEY', 'SECRET-KEY', False )
        """
        self.origin        = origin
        self.limit         = 1800
        self.publish_key   = publish_key
        self.subscribe_key = subscribe_key
        self.secret_key    = secret_key
        self.ssl           = ssl_on

        if self.ssl :
            self.origin = 'https://' + self.origin
        else :
            self.origin = 'http://'  + self.origin
            
            
            
            
            

channels = [
        # 'lightning_ticker_BTC_JPY',
        'lightning_executions_BTC_JPY',
        # 'lightning_board_snapshot_BTC_JPY',
        # 'lightning_board_BTC_JPY',
        # 'lightning_ticker_FX_BTC_JPY',
        # 'lightning_ticker_ETH_BTC',
    ]
    
    
    
pubnub = Pubnub( 'demo', 'demo', None, False )

## History Example
history = pubnub.history({
    'channel' : 'hello_world',
    'limit'   : 1
})
print(history)    