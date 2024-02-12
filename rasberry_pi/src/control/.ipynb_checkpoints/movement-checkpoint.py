def generate_movement_sequence(motion):
    """
    Generates a movement sequence for different directions, including pivoting.
    
    Parameters:
    - motion: str, one of "forward", "backward", "sideways_left", "sideways_right", "pivot_left", "pivot_right"
    
    Returns:
    - sequence: List[Dict[int, List[int]]], a sequence of steps with actuator positions.
    """
    sequence = []
    steps = 4  # Number of steps in a complete movement cycle
    
    for step in range(steps):
        step_positions = {}
        for limb_id in range(8):  # 8 limbs
            positions = [0] * 10  # Reset actuator positions

            # Forward motion
            if motion == "forward":
                for actuator_id in range(10):
                    if limb_id % 2 == 0:
                        positions[actuator_id] = 1 if (step + actuator_id) % 4 < 2 else 0
                    else:
                        positions[actuator_id] = 0 if (step + actuator_id) % 4 < 2 else 1

            # Backward motion
            elif motion == "backward":
                for actuator_id in range(10):
                    if limb_id % 2 == 0:
                        positions[actuator_id] = 0 if (step + actuator_id) % 4 < 2 else 1
                    else:
                        positions[actuator_id] = 1 if (step + actuator_id) % 4 < 2 else 0

            # Sideways motion to the left
            elif motion == "sideways_left":
                for actuator_id in range(10):
                    positions[actuator_id] = 1 if limb_id % 4 == step % 4 else 0

            # Sideways motion to the right
            elif motion == "sideways_right":
                for actuator_id in range(10):
                    positions[actuator_id] = 1 if limb_id % 4 != step % 4 else 0

            # Pivot left
            elif motion == "pivot_left":
                for actuator_id in range(10):
                    if limb_id < 4:  # Left side limbs
                        positions[actuator_id] = 1 if actuator_id % 2 == 0 else 0
                    else:  # Right side limbs
                        positions[actuator_id] = 0 if actuator_id % 2 == 0 else 1

            # Pivot right
            elif motion == "pivot_right":
                for actuator_id in range(10):
                    if limb_id < 4:  # Left side limbs
                        positions[actuator_id] = 0 if actuator_id % 2 == 0 else 1
                    else:  # Right side limbs
                        positions[actuator_id] = 1 if actuator_id % 2 == 0 else 0

            step_positions[limb_id] = positions
        sequence.append(step_positions)
    
    return sequence
