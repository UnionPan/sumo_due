import traci
import sumolib

def run_simulation():
    # Start the SUMO simulation
    sumoCmd = ["sumo", "-c", "config/my_simulation.sumocfg"]
    traci.start(sumoCmd)

    step = 0
    while step < 1000:  # Run for 1000 simulation steps
        traci.simulationStep()  # Advance the simulation by one step
        # Your DUE algorithm logic goes here
        
        step += 1
    
    traci.close()

if __name__ == "__main__":
    run_simulation()