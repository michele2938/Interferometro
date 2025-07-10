from machine import ADC, Pin
import time


ldr = ADC(Pin(26))
led = Pin(25, Pin.OUT)

n = 0
eseguito = False  

print("Inizio acquisizione dati...")

while True:
    valore = 65535 - ldr.read_u16()  
    print("luce", valore)
#
    if valore < 6900 and not eseguito:
        n += 1
        print("Incremento n:", n)
        eseguito = True
    elif valore >= 5000:
      eseguito = False  


    if valore < 30000:
        led.high()
    else:
        led.low()

    time.sleep(0.001)
