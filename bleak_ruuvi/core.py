from bleak import discover

from bleak_ruuvi.decoders import RuuviMeasurementV3
from bleak_ruuvi.consts import MANUFACTURER_ID_RUUVI

data_formats = {
    MANUFACTURER_ID_RUUVI: {
        3: RuuviMeasurementV3
    }
}

async def scan(timeout=5):
    while True:
        devices = await discover(timeout=timeout)
        for d in devices:
            try:
                for manufacturer_id in d.details['props']['ManufacturerData']:
                    manufacturer_formatters = data_formats[manufacturer_id]
                    data = d.details['props']['ManufacturerData'][manufacturer_id]
                    yield manufacturer_formatters[data.pop(0)](d.name, d.address, d.rssi, *data)
            except KeyError:
                # For unknown reason the ManufacturerData may sometimes not be
                # present, thus the inner loop is in try-except block.
                # Might be a bug in bleak. Usually this will catch
                # "unsuported format" error
                continue