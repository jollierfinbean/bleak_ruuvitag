import asyncio
from bleak_ruuvitag import scan

async def main():
   async for measurement in scan():
       print(measurement)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
