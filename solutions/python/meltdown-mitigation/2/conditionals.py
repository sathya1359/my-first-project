
"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Check if the reactor is balanced."""
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Calculate reactor efficiency."""
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    if efficiency >= 60:
        return "orange"
    if efficiency >= 30:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Determine reactor safety status."""
    value = temperature * neutrons_produced_per_second

    if value < 0.9 * threshold:
        return "LOW"
    if value <= 1.1 * threshold:
        return "NORMAL"
    return "DANGER"
