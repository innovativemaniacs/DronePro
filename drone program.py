# Import necessary modules from dronekit and time
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the Vehicle on specified port (SITL or real drone)
print("Connecting to vehicle...")
vehicle = connect('127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(target_altitude):
    """
    Arms vehicle and flies to the target altitude.

    This function ensures the drone is ready to fly, switches to GUIDED mode,
    arms the drone, and initiates a takeoff to the specified altitude.
    """
    print("Arming motors")
    
    # Wait until the vehicle is ready to be armed
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    # Set the vehicle mode to GUIDED so we can control it with code
    vehicle.mode = VehicleMode("GUIDED")
    
    # Send command to arm the motors
    vehicle.armed = True

    # Wait until the drone confirms it's armed
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    # Command the drone to take off to the target altitude
    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    # Monitor altitude and wait until it's close to the target altitude
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        
        # Once we are within 95% of the target, we assume takeoff is successful
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def fly_to_location(target_location):
    """
    Fly to a specific GPS location.

    This function sends the drone to the desired location and monitors until arrival.
    """
    print(f"Flying to location: {target_location}")
    
    # Command the drone to fly to the specified location
    vehicle.simple_goto(target_location)

    # Continuously monitor the drone's location until it reaches close to the target
    while True:
        current_location = vehicle.location.global_relative_frame
        print(f"Current location: {current_location}")

        # Check if we're close enough to the target location (small tolerances for lat/lon/alt)
        if abs(current_location.lat - target_location.lat) < 0.00001 and \
           abs(current_location.lon - target_location.lon) < 0.00001 and \
           abs(current_location.alt - target_location.alt) < 0.5:
            print("Reached target location")
            break

        time.sleep(1)

# Define the destination GPS coordinates and target altitude
# These coordinates represent a point you want your drone to fly to
target_location = LocationGlobalRelative(22.805618, 86.202875, 10)  # Example location

# Take off to 10 meters altitude
arm_and_takeoff(10)

# Fly to the previously defined location
fly_to_location(target_location)

# After mission is complete, close the connection to the drone safely
print("Close vehicle object")
vehicle.close()
