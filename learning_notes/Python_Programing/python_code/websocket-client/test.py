# pip install websocket-client
import websocket
import json
CHANNEL = "lightning_executions_BTC_JPY"

def on_message(ws, message):
    message = json.loads(message)
    if message["method"] == "channelMessage":
        print("{} {}".format(message["params"]["channel"], message["params"]["message"]))

def on_open(ws):
    ws.send(json.dumps({"method": "subscribe", "params": {"channel": CHANNEL}}))

if __name__ == "__main__":
    # note: reconnection handling needed.
    ws = websocket.WebSocketApp("wss://ws.lightstream.bitflyer.com/json-rpc",
                              on_message = on_message, on_open = on_open)
    ws.run_forever()