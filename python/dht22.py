import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
GPIO = 18
humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)

degree_sign=u'\N{DEGREE SIGN}'
print("Luftfeuchtigkeit:")
print(str(humidity)+"%")
print("Temperatur:")
print(str(temperature)+degree_sign+"C")
