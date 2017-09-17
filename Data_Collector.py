
import Adafruit_DHT
import csv
import time
def calculate():    
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
    sensor = Adafruit_DHT.DHT11

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
    pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
    if humidity is not None and temperature is not None:
        if(humidity>100):
            return -1000
        else:
            return [temperature,humidity]
    else:
        return -1000

#write function 
def write_data(row):
    data=[float(i) for i in row]
    with open('data.csv','a') as csvfile:
        w=csv.writer(csvfile, delimiter=',')
        w.writerow(data)

#Execute       
t_end = time.time() + 60 * 15
t1=0
while(time.time() < t_end):
    z=calculate()
    time.sleep(15)
    if(z!=-1000):
        l=[t1]
        l.extend(z)
        write_data(l)
    t1+=15
    
