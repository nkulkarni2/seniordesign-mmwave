import math
import time

distance = 90
azimuth = 67
vehicle_speed = 6.72 # m/s        
human_avg_speeed = 1.4 # m/s        

#Distance will be calculated using the current speed
#Azimuth will be incorporated as an angle


def dead_reckoning():
    # Scooter is going straight and person1 approaching at angle=azimuth
    x = abs(math.sin(azimuth)*distance)
    y = abs(math.cos(azimuth)*distance)
    
    print("Collision will happen @", x,y)

    # Time till collision
    # Wrong: does not take in consideration human speed 
    t_1 = y/vehicle_speed
    print("Collision time in", t_1, "sec")

    while y > 0:
        y = y - vehicle_speed
        time.sleep(1)
        print(y)

        if math.floor(y) <= 10:
            print("PERSON APPROACHING!!")
            break
        
    
dead_reckoning()
