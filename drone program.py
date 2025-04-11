# Connect to the Vehicle
print("Connecting to vehicle...")
vehicle = connect('127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(target_altitude):
    """
    Arms vehicle and fly to a target altitude.
    """
    print("Arming motors")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def fly_to_location(target_location):
    """
    Fly to a specific location.
    """
    print(f"Flying to location: {target_location}")
    vehicle.simple_goto(target_location)

    while True:
        current_location = vehicle.location.global_relative_frame
        print(f"Current location: {current_location}")
        if abs(current_location.lat - target_location.lat) < 0.00001 and \
           abs(current_location.lon - target_location.lon) < 0.00001 and \
           abs(current_location.alt - target_location.alt) < 0.5:
            print("Reached target location")
            break
        time.sleep(1)

# Define the target location (latitude, longitude, altitude)
target_location = LocationGlobalRelative(22.805618, 86.202875, 10)  # Example coordinates

# Arm and take off to 10 meters altitude
arm_and_takeoff(10)

# Fly to the target location
fly_to_location(target_location)

# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()

