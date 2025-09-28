import math

def estimate_energy(distance_km, grade, vehicle_type='diesel', load_kg=500):
    """Very simplified energy model (for demo purposes)"""
    base_energy = distance_km * (1.5 if vehicle_type == 'diesel' else 0.3)  # L diesel or kWh for EV
    grade_factor = 1 + 0.01 * max(grade, 0)  # uphill penalty
    load_factor = 1 + 0.0005 * load_kg
    return base_energy * grade_factor * load_factor

def energy_to_co2(energy, vehicle_type='diesel'):
    if vehicle_type == 'diesel':
        return energy * 2.68 * 1000  # L diesel -> gCO2
    else:
        grid_intensity = 400  # gCO2/kWh
        return energy * grid_intensity
