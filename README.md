## Supported protocols
See https://github.com/ruuvi/ruuvi-sensor-protocols
- [ ] data format 2 (https://github.com/ruuvi/ruuvi-sensor-protocols#data-format-2-and-4-protocol-specification)
- [x] data format 3 (https://github.com/ruuvi/ruuvi-sensor-protocols#data-format-3-protocol-specification-rawv1)
- [ ] data format 4 (https://github.com/ruuvi/ruuvi-sensor-protocols#data-format-2-and-4-protocol-specification)
- [ ] data format 5 (https://github.com/ruuvi/ruuvi-sensor-protocols#data-format-5-protocol-specification-rawv2)
## Examples

```python
import asyncio
from bleak_ruuvitag.core import scan

async def main():
   async for measurement in scan():
       print(measurement)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

```

```
F2:50:A2:35:BB:5E (RAWv1), rssi=-86, temperature=24.31°C, humidity=48.5%, pressure=102004Pa, accelerationX=848mG, accelerationY=-620mG, accelerationZ=36mG, voltage=2713mV
...
```
