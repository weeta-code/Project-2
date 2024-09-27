# Author: Victor DeSouza
# Email: victordesouz@umass.edu
# SPIRE ID: 34569497

def stop(traffic_light, pedestrian) -> bool:
    if traffic_light == 'Red' or pedestrian == True:
        return True
    else: 
        return False

def move_forward(traffic_light, pedestrian) -> bool:
    if traffic_light == 'Green' and pedestrian == False:
        return True
    elif traffic_light == 'Yellow' and pedestrian == False:
        return True
    else:
        return False

def turn_left(traffic_light, pedestrian, cars_opposite) -> bool:
    if traffic_light == 'Green' and cars_opposite == False and pedestrian == False:
        return True
    else:
        return False