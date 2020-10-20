import logging
from configuration import update_live_prefix
from db import Session, Servers, Channels
from . import setting_callback

@setting_callback('prefix')
async def set_prefix(data):
    logging.info(f"Data received: {data}")
    for prefix in data:
        dkeys = prefix.keys()
        session = Session()
        if 'channel_id' in dkeys:
            target = session.query(Channels).get(prefix['channel_id'])
        elif 'server_id' in dkeys:
            target = session.query(Servers).get(prefix['server_id'])
        else:
            target = None

        if target and target.prefix == prefix.get('prefix', None):
            update_live_prefix(target.id, target.prefix)
