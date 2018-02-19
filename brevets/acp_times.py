"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#
maxTable = [(200, 34), (400, 32), (600, 30), (1000,28), (1300,26)]
mTable = [(200, 34), (400, 32), (600, 28), (1000,)]

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
#check input 
if 



	hours = 0 
	min = 0 
	day = 0
	for i in range(len(maxTable)):
	    if maxTable[i][0] > control_dist_km:
            buff = control_dist_km / maxTable[i][1]
            hours = (buff//1)
	        if(hours >= 24):
                hours %= 24
                day+=1							
	        min = (buff%1)

	return arrow.get(startTime).shift(minutes = min, hours = hours, day = day).isoformat()



def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
	hours = 0 
	min = 0 
	day = 0
	for i in range(len(maxTable)):
	    if maxTable[i][0] > control_dist_km:
            buff = control_dist_km / maxTable[i][1]
            hours = (buff//1)
	        if(hours >= 24):
                hours %= 24
                day+=1						
	        min = (buff%1)

	return arrow.get(startTime).shift(minutes = min, hours = hours, day = day).isoformat()
