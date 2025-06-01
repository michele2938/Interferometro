from machine import ADC, Pin
import time

ldr = ADC(Pin(26))
led = Pin(25, Pin.OUT)

val = []

try:
    while True:
        lect = 65535 - ldr.read_u16()
        val.append(lect)
        time.sleep(0.001)
        print(lect)
except KeyboardInterrupt:
    with open("data.txt", "w") as f:
        for lect in val:
            f.write(str(lect) + "\n")
    print("Dati salvati.")

    frange = 0
    direction = 0  

    for i in range(1, len(val)):
        if val[i] > val[i - 1]:
            if direction == -1:
                frange += 1  
            direction = 1
        elif val[i] < val[i - 1]:
            if direction == 1:
                frange += 1  
            direction = -1

    print("Numero frange:", frange)
