import asyncio
import datetime
from typing import NamedTuple

from bleak_ruuvitag.core import scan
from aioinflux import (
    InfluxDBClient,
    TAGENUM,
    TAG,
    FLOAT,
    INT,
    STR,
    lineprotocol
)

influxdb_client_configuration = {
    'host': 'influxdb.lan',
    'port': 80,
    'db': 'mydb',
    'username': 'myuser',
    'password': 'mypassword'
}

@lineprotocol
class RuuviTagMeasurementTest1(NamedTuple):
    name: TAG
    temperature: FLOAT
    humidity: FLOAT
    pressure: INT
    voltage: INT


async def main():
    client = InfluxDBClient(**influxdb_client_configuration)
    async for result in scan(5):
        measurement = RuuviTagMeasurementTest1(
            name=result.name,
            temperature=result.temperature,
            humidity=result.humidity,
            pressure=result.pressure,
            voltage=result.voltage,
        )
        asyncio.create_task(client.write(measurement))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
