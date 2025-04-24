import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TelemedicinaCostumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"telemedicina_{self.room_name}"
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        
    async def disconnect(self, close_code):
            await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

            async def receive(self, text_data):
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        "type": "sinalizacao_mensagem",
                        "mensagem": text_data,
                    }
                )

            async def sinalizacao_mensagem(self, event):
                mensagem = event['mensagem']
                await self.send(text_data=mensagem)