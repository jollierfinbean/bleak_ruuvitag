from bleak_ruuvitag.utils import twos_complement

class RuuviMeasurementV3():
    version = 'RAWv1'
    temperature_unit = '°C'
    humidity_unit = '%'
    pressure_unit = 'Pa'
    acceleration_unit = 'mG'
    voltage_unit = 'mV'

    def __init__(self, name, mac_address, rssi, humidity, temperature, temperature_fraction, pressure1, pressure2,
                 acc_x1, acc_x2,  acc_y1, acc_y2, acc_z1, acc_z2, voltage1, voltage2, *args):
        self.name = name
        self.mac_address = mac_address
        self.rssi = rssi
        self._humidity = humidity
        self._temperature = temperature
        self._temperature_fraction = temperature_fraction
        self._pressure1 = pressure1
        self._pressure2 = pressure2
        self._acc_x1 = acc_x1
        self._acc_x2 = acc_x2
        self._acc_y1 = acc_y1
        self._acc_y2 = acc_y2
        self._acc_z1 = acc_z1
        self._acc_z2 = acc_z2
        self._voltage1 = voltage1
        self._voltage2 = voltage2

    def __str__(self):
        return (
            '{measurement.mac_address} ({measurement.version}), ' +
            'rssi={measurement.rssi}, ' +
            'temperature={measurement.temperature}{measurement.temperature_unit}, ' +
            'humidity={measurement.humidity}{measurement.humidity_unit}, ' +
            'pressure={measurement.pressure}{measurement.pressure_unit}, ' +
            'accelerationX={measurement.acc_x}{measurement.acceleration_unit}, ' +
            'accelerationY={measurement.acc_y}{measurement.acceleration_unit}, ' +
            'accelerationZ={measurement.acc_z}{measurement.acceleration_unit}, ' +
            'voltage={measurement.voltage}{measurement.voltage_unit}'
        ).format(measurement=self)

    @property
    def humidity(self):
        return self._humidity / 2

    @property
    def temperature(self):
        #TODO: check what happens on negative values
        return self._temperature + self._temperature_fraction/100

    @property
    def pressure(self):
        return (self._pressure1 << 8) + self._pressure2 + 50_000

    @property
    def acc_x(self):
        return twos_complement((self._acc_x1 << 8) + self._acc_x2, 16)

    @property
    def acc_y(self):
        return twos_complement((self._acc_y1 << 8) + self._acc_y2, 16)

    @property
    def acc_z(self):
        return twos_complement((self._acc_z1 << 8) + self._acc_z2, 16)

    @property
    def voltage(self):
        return (self._voltage1 << 8) + self._voltage2
