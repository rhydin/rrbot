from . import register_setting_callback

async def testing(data):
    print(data)

register_setting_callback('test', testing)
