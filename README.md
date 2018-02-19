# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax.

Credits to ADITYA NACHIAPPAN.

## For users 
The current RUSA controle time calculator is based on an underlying algorthim that divides each portion of your total 
ride into checkpoints, and calculates how long you have to complete the checkpoint.
The calculation of a control's opening time is based on the maximum speed. Calculation of a control's closing time is based on the minimum speed.
The table containing the max and min speeds can be found here https://rusa.org/octime_alg.html


## For developers 

Prior to my work, the calculator would automatically asume the brevet distance was 200. Now it can ask for time inputs, bounds check, then calculate the appropriate opening and closing times. 
I converted the algorithim into python code by dividing the control distance by its approriate max and min speeds, taking the result, separating minutes and hours, nd returning it in addition to the opening time. 
