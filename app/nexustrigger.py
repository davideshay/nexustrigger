import asyncio, os
from websockets import connect

async def trigger(uri):
    async with connect(uri,ping_timeout=None,open_timeout=None) as websocket:
        await websocket.send("start")
        message = await websocket.recv()
        print(message,flush=True)
        finished=False
        while not finished:
            message = await websocket.recv()
            if message=="end":
                finished=True
            else:
                print(message,flush=True)

nexus_svc_hostname=os.environ.get('NEXUS_BACKUP_SVC_HOSTNAME')
nexus_svc_port=os.environ.get('NEXUS_BACKUP_SVC_PORT')
nexus_svc_url="ws://"+nexus_svc_hostname+":"+nexus_svc_port

asyncio.run(trigger(nexus_svc_url))
