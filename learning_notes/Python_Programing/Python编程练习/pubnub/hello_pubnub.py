from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time, random
from datetime import datetime

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-a7e153ae-ac30-11e6-b37b-02ee2ddab7fe"
pnconfig.publish_key = "pub-c-4185f85e-676a-48a6-9f8e-1f45ab5a0ed7"
pubnub = PubNub(pnconfig)

for i in range(1000):
    json_data = {
        'datetime' : datetime.now().isoformat(),
        'number_one' : random.randint(1,50),
        'number_two' : random.randint(10,35),
        'letter_one' : random.choice('ABCD'),
        'letter_two' : random.choice('XY'),
    }
    pubnub.publish().channel('pubnub_demo').message(json_data).sync()
    time.sleep(1)

