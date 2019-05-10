# import asyncio
# import websockets
# import json
# from normal_distribution_generator import NormalDistributionGenerator
#
#
# async def server(websocket, path):
#     client = await websocket.recv()
#     print(f'Client connected: {client}')
#     samples_store = NormalDistributionGenerator()
#
#     try:
#         index = 0
#         while True:
#             sample = samples_store.get_sample()
#             index += 1
#             await websocket.send(
#                 json.dumps({'index': index, 'value': sample})
#             )
#             await asyncio.sleep(0.03)
#     except websockets.exceptions.ConnectionClosed:
#         print(f'Client disconnected: {client}')
#
# start_server = websockets.serve(server, 'localhost', 8888)
#
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
