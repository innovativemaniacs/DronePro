# DroneKit Python Script: Connect, Takeoff, and Navigate

This repository contains a Python script using the [DroneKit](http://python.dronekit.io/) library to control a drone via a simulated or real MAVLink connection. The script demonstrates basic operations such as connecting to the vehicle, arming, taking off to a specified altitude, flying to a GPS coordinate, and safely disconnecting.

## ✈️ Features

- Connects to vehicle (e.g., drone simulator or real drone)
- Arms and takes off to a specified altitude
- Navigates to a specified GPS location
- Includes simple telemetry printout
- Gracefully closes connection after mission

## 🧠 Requirements

- Python 3.x
- DroneKit
- MAVProxy (for simulation)
- Drone simulator (e.g., SITL) **or** a real MAVLink-compatible drone

## 🧰 Installation

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install DroneKit and dependencies
pip install dronekit

