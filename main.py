# StopLightSim.py
# Name: Jenna Kramer
# Date: 4/18
# Assignment: Lab 11

import simpy

# Global variable to track light state
greenLight = True


def stopLight(env):
    """Simulates a traffic light that cycles between green, yellow, and red."""
    global greenLight

    while True:
        print("Green at time", env.now)
        greenLight = True
        yield env.timeout(30)

        print("Yellow at time", env.now)
        yield env.timeout(2)

        print("Red at time", env.now)
        greenLight = False
        yield env.timeout(20)


def car(env, car_id):
    """Simulates a car arriving and waiting for the light."""
    
    print("Car", car_id, "arrived at", env.now)
    parking_duration = 5
    yield env.timeout(parking_duration)

    # TODO: Make the car wait while the light is red
    # Hint: use a loop and env.timeout(1)
    while True:
        if greenLight == False: 
            print("Car", car_id, "is waiting")
            yield env.timeout(1)
        else: 
            break 

    print("Car", car_id, "departed at", env.now)


def carArrival(env):
    """Creates cars at regular intervals."""
    
    car_id = 0

    while True:
        car_id += 1
        print("Creating Car", car_id)

        # TODO: Start a new car process
        env.process(car(env, car_id))

        yield env.timeout(5)


def main():
    env = simpy.Environment()

    # Start processes
    env.process(stopLight(env))
    
    # TODO: Start the carArrival process
    env.process(carArrival(env))
    # Run simulation
    env.run(until=100)

    print("Simulation complete")


if __name__ == "__main__":
    main()
