"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


maxTable = [(1300,26), (1000,28), (600, 30), (400, 32), (200, 34)] 
minTable = [(1300,26), (1000,13.333), (600, 11.428), (400, 15), (200, 15)] 

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
   	#check input 
	#Basic error check
	#Make sure the distance entered is positive, shorter than total brevet dist
	#Return the time + 1 hour by default for

    utc = arrow.get(brevet_start_time)
    if 0 > control_dist_km:
        print("Cannot have negative distance! ")
    if control_dist_km > brevet_dist_km:
        print("Cant have lap longer than total brevet!")
    if control_dist_km == 0: 
        utc.shift(hours =+ 1)

    time = 0 
    
    for pair in maxTable:
        distance, speed = pair
        if distance > control_dist_km:
            time =+ control_dist_km / speed
            hour, min = divmod(time, 1)     		#seperate hours and min
            min =(time%1)*60  
            utc.shift(hour =+ hour, minute =+ min)      #add hours and minutes to current time
    return utc.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
	#check input 
	#Basic error check
	#Make sure the distance entered is positive, shorter than total brevet dist
	#Return the time + 1 hour by default for 
    
    utc = arrow.get(brevet_start_time)
    if 0 > control_dist_km:
        print("Cannot have negative distance! ")
    if control_dist_km > brevet_dist_km:
        print("Cant have lap longer than total brevet!")
    if control_dist_km == 0: 
        utc.shift(hours =+ 1)

    time = 0 
    
    for pair in minTable:
        distance, speed = pair
        if distance > control_dist_km:
            time =+ control_dist_km / speed
            hour, min = divmod(time, 1)     		#seperate hours and min
            min =(time%1)*60  
            utc.shift(hour =+ hour, minute =+ min)      #add hours and minutes to current time
    return utc.isoformat()

