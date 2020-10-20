from . import setting_callback

@setting_callback('test')
async def testing(data):
    print(data)

