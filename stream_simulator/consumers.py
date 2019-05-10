import json
import time
from channels.generic.websocket import AsyncWebsocketConsumer
from stream_simulator.normal_distribution_generator import NormalDistributionGenerator


class ClientConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index = 0

    async def connect(self):
        group_id = str(round(time.time() * 1000))
        await self.accept()
        await self.send(group_id)

    async def receive(self, text_data=None, **kwargs):
        samples_store = NormalDistributionGenerator()
        sample = samples_store.get_sample()
        self.index += 1
        await self.send(text_data=json.dumps({'index': self.index, 'value': sample}))


class ClientWebListener(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_id = self.scope["path"].replace("/", "")
        await self.channel_layer.group_add(
            self.group_id, self.channel_name
        )
        await self.accept()

    async def receive(self, text_data=None, **kwargs):
        await self.channel_layer.group_send(
            self.group_id,
            {
                'type': 'generate_sample',
                'message': text_data
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_id,
            self.channel_name
        )

    async def generate_sample(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
