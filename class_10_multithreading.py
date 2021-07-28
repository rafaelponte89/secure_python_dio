from threading import Thread
import time
def car(speed, pilot):
    target = 0
    while target <= 100:
        print(f'\nCarro: piloto {pilot}, km {target}')
        target+=speed
        time.sleep(0.3)

t_car_1 = Thread(target=car,args=[1,'Rafael'])
t_car_2 = Thread(target=car, args=[1,'Gabi'])

t_car_1.start()
t_car_2.start()

