import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Indicators


class IndicatorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(json.dumps({"message":"WebSocket connetion"}))

    async def dicconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        indicator_id = data.get('id')
        new_value = data.get('value')
        try:
            indicator = Indicators.objects.get(id=indicator_id)
            indicator.value = new_value
            indicator.save()

            await self.send(json.dumps({
                'id': indicator.id,
                'value': indicator.value,
            }))
        except Indicators.DoesNotexit:
            await self.send(json.dumps({'error':'indicator not found'}))