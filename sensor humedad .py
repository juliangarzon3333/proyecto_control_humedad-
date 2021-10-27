from machine import Pin, ADC
import utime
import network, time, urequests
 
sensor = ADC(Pin(36))



    

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              
          miRed.active(True)                 
          miRed.connect(red, password)         
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True



if conectaWifi ("RedMiHugo", "12345678"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://api.thingspeak.com/update?api_key=3QGMC1ZVPU8WVPPJ"  
    
    while (True):
       
        
        
        lectura =  int(sensor.read())
        print(lectura)
        utime.sleep(0.5)
        print("Lectura = {:02d}".format(lectura))
        respuesta = urequests.get(url+"&field1="+str(lectura))
        print(respuesta.text)
        print (respuesta.status_code)
        respuesta.close ()
        
   
              
else:
       print ("Imposible conectar")
       miRed.active (False)