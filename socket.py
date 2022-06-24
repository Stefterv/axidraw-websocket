import asyncio
import websockets
import pyaxidraw 
import json

ad = pyaxidraw.axidraw.AxiDraw()
ad.plot_setup()
ad.options.preview = True

print(dir())

class Error:
    error: str
    def __init__(self, error) -> None:
        self.error = error
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

async def handler(websocket):
    async def handleMessage(message):
        try:
            func = getattr(ad, message['function'])
            res = func()
            await websocket.send(json.dumps(res))
        except:
            await websocket.send(Error("An error occurred").toJSON())

    while True:
        try:
            message = await websocket.recv()
            cmd = json.loads(message)
            await handleMessage(cmd)
        except websockets.ConnectionClosedOK:
            break
        except json.JSONDecodeError:
            print("Error decoding JSON")
        except AssertionError:
            print("Improper data")
        





async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

