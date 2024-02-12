import time
from control.actuator_control import ActuatorController
from movement import generate_movement_sequence

# Placeholder function for getting movement commands (could be from sensors, remote control, etc.)
def get_current_command():
    # This function should be replaced with actual logic to receive commands.
    # For demonstration, it will cycle through different commands.
    commands = ["forward", "backward", "sideways_left", "sideways_right", "pivot_left", "pivot_right"]
    while True:  # Infinite generator cycling through commands
        for cmd in commands:
            yield cmd
            time.sleep(10)  # Change command every 10 seconds

def main():
    num_limbs = 8
    actuators_per_limb = 10

    controller = ActuatorController(num_limbs, actuators_per_limb)
    
    command_generator = get_current_command()  # Create a generator for commands

    try:
        while True:
            current_command = next(command_generator)  # Get the current movement command
            print(f"Current command: {current_command}")
            movement_sequence = generate_movement_sequence(current_command)

            for step in movement_sequence:
                for limb_id, positions in step.items():
                    for actuator_id, position in enumerate(positions):
                        actuator_ref = controller.get_actuator_reference(limb_id, actuator_id)
                        controller.actuate(actuator_ref, position)
                time.sleep(0.5)  # Adjust based on your actuator's response time

    except KeyboardInterrupt:
        # Implement your clean-up and reset logic here
        print("Stopping robot...")

if __name__ == "__main__":
    main()
