# proyecto_control_humedad-
proyecto_control_humedad 

DECRIPCION DEL PROYECTO:

Con ánimos de presentar un proyecto que preste una funcionalidad y ofrezca una solución a un problema; usando la aplicación de los conocimientos en python adquiridos durante este curso, tenemos el agrado de presentar un proyecto cuya finalidad nace de una problemática fehaciente en las personas que poseen desde pequeñas huertas casera, hasta viveros de más amplio tamaño, y es que, algo ciertamente esencial en la cultivación  es la humedad correcta de la tierra, esta  juega un papel supremamente importante en la maduración y cosecha de la mayoría si no es que en todos los tipos de plantas.


Dispuestos a dar solución  usando los recursos brindados por la ACADEMIA CISCO JGC, se presenta una construcción de un sistema totalmente funcional cuya ocupación radica en controlar y consultar EN TIEMPO REAL la humedad conservada en la tierra de una plantación ademas de alertar de irregularidades en esta.


ELEMENTOS DE USO Y APLICACIÓN:

- Proto board  ordinaria 

![image](https://user-images.githubusercontent.com/88451810/138114416-d17584a9-1113-4ba3-89ca-8b426d9ca81d.png)





-  Micro controlador  ESP32

![image](https://user-images.githubusercontent.com/88451810/138113908-5d57a61e-9718-4b5a-9b85-5489ca1c7aab.png)


-  Sensor de humedad en tierra  fc-28

![image](https://user-images.githubusercontent.com/88451810/138113716-cadb1428-a6ee-45e6-8b8b-bf1e0b7aec23.png)



-  Led   5 milímetros común 

![image](https://user-images.githubusercontent.com/88451810/138113386-807e2622-fcb2-4890-a46a-edfb9f13db42.png)


-  Sofware de codigo abierto Thinspeak



![image](https://user-images.githubusercontent.com/88451810/138115696-bc169a23-793b-478e-8d53-85b2e9c4628b.png)





DISPOSICIÓN DE LOS ELEMENTOS:




![136988483-073d0be7-3961-4b2b-9fb6-14ea4bb24947](https://user-images.githubusercontent.com/88451810/138116751-4056cb6d-1237-4ea2-8439-a4619611c401.png)




![image](https://user-images.githubusercontent.com/88451810/139163320-5f9e432a-3f9b-447c-800d-ec812c9f0396.png)
![image](https://user-images.githubusercontent.com/88451810/139163333-3adaaf22-f773-414e-b933-00cfa3bcd5bb.png)



CODIGO UTILIZADO :

-  librerias requeridas y variables 


from machine import Pin, ADC
import utime
import network, time, urequests
 
sensor = ADC(Pin(36))

-  definicion  patrones para poder conectrase a la red 


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
 -   lecturas del sensor 


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



VIDEO DE EXPLICACION DEL PROYECTO 

https://youtu.be/pBy2uRxBrR4
