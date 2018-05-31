# Solar Powered Raspberry Pi Weather Station

We used a Raspberry Pi to collect data from a SparkFun HIH6130 temperature and relative humidity sensor using I2C, and a PiCamera to take a still photo of conditions in our outdoor discovery centre. The information is then tweeted out by our STEAM account, @lks_steam. The whole thing is powered by a sealed lead acid battery, charged by a solar panel and PWM solar charge controller.

The project needs Twython in order to tweet. Check out https://github.com/ryanmcgrath/twython for how to install.

For the temperature and relative humidity sensor to communicate with the Raspberry Pi, open a terminal window and install:

1. python-smbus
2. i2c-tools

You will also need to install the HIH6130 Python library: https://github.com/dhhagan/python-hih6130 

Future build will include an adafruit anemometer.
