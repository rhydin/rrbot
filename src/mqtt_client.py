import asyncio, json, re, logging, threading
from configuration import MQTT_URL
from asyncio_mqtt import Client, MqttError
from db import Session, Servers, Channels

TOPIC_PREFIX = 'rrbot/settings'
TOPIC_FILTER = f"{TOPIC_PREFIX}/+"
TOPIC = re.compile(f'{TOPIC_PREFIX}/(?P<topic>.+)')
MQTT_LIVE = True
DISPATCH = {}

def register_setting_callback(setting, callback):
    if DISPATCH.get(setting, None) is None:
        DISPATCH[setting] = [callback]
    else:
        DISPATCH[setting].append(callback)

async def dispatch_message(message):
    m = TOPIC.match(message.topic)
    if m is None:
        return
    fns = DISPATCH.get(m['topic'], [lambda msg: None])
    [await fn(json.loads(message.payload.decode())) for fn in fns]


async def mqtt_task():
    attempts = 1
    while MQTT_LIVE:
        try:
            async with Client(MQTT_URL) as client:
                logging.info(f'connected to client at {MQTT_URL}')
                attmpts = 1
                async with client.filtered_messages(TOPIC_FILTER) as messages:
                    await client.subscribe(TOPIC_FILTER)
                    async for message in messages:
                        await dispatch_message(message)
        except MqttError as err:
            logging.error(err)
        timeout = max(5 * attempts, 30)
        logging.info(f'Will attempt reconnect #{attempt} to {MQTT_URL} in {timeout}')
        await asyncio.sleep(timeout)
        attempts += 1

class MQTT_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.main_loop = asyncio.get_event_loop()
        #self.task = self.main_loop.create_task(mqtt_task())

    def run(self):
        logging.info(f"Prepped to listen for '{TOPIC_FILTER}' from '{MQTT_URL}'")
        #self.main_loop.run_until_complete(self.task())
        asyncio.run(mqtt_task())

mqtt_thread = MQTT_Thread();
mqtt_thread.start()
