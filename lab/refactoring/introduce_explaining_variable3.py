# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cooking_criteria_satisfied(time, temperature, pressure, desired_state):
    if desired_state == 'well-done' and actual_state() >= WELL_DONE: 
        return True
    if desired_state == 'medium' and actual_state() >= MEDIUM:
        return True
    return False

def actual_state(time, temperature, pressure, desired_state):
    return time * pressure * temperature * COOKED_CONSTANT