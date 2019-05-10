import asyncio
import json
import math
import websockets
from datetime import datetime


WEBSOCKET_SERVER_URL = 'ws://localhost:8000'
HTTP_SERVER_URL = 'http://localhost:8000'


def is_out_of_deviation_range(value):
    return math.fabs(float(value)) - 2 > 0


async def client():
    async with websockets.connect(WEBSOCKET_SERVER_URL) as ws:
        cliend_id = await ws.recv()
        listen_client_url = f'{WEBSOCKET_SERVER_URL}/client/{cliend_id}'
        async with websockets.connect(listen_client_url) as ws_browser_sync:
            print(f'Listen to the client: {HTTP_SERVER_URL}/client/{cliend_id}')

            while True:
                await asyncio.sleep(0.05)
                await ws.send('received')
                response = await ws.recv()
                sample = json.loads(response)
                if is_out_of_deviation_range(sample['value']):
                    sample = {**sample, 'timestamp': str(datetime.now())}
                    print(sample)
                    await ws_browser_sync.send(json.dumps(sample))

if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(client())
    except websockets.exceptions.ConnectionClosed:
        print('Connection aborted')
    except KeyboardInterrupt:
        print('Disconnected')
