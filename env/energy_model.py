import math

def estimate_energy(distance_km, grade, vehicle_type='diesel', load_kg=500):
    """Energy model accounting for cargo weight impact on fuel consumption"""
    # Base energy consumption per km (varies by vehicle type)
    if vehicle_type == 'diesel':
        base_energy = distance_km * 1.5  # L diesel
    elif vehicle_type == 'gasoline':
        base_energy = distance_km * 1.8  # L gasoline (higher consumption than diesel)
    else:  # EV
        base_energy = distance_km * 0.3  # kWh
    
    # Grade impact (uphill requires more energy)
    grade_factor = 1 + 0.01 * max(grade, 0)  # uphill penalty
    
    # Cargo weight impact (more significant for heavier loads)
    # Weight affects acceleration, braking, and rolling resistance
    if load_kg > 1500:  # Very heavy cargo
        load_factor = 1 + 0.001 * load_kg  # 0.1% per kg for very heavy loads
    elif load_kg > 1000:  # Heavy cargo
        load_factor = 1 + 0.0008 * load_kg  # 0.08% per kg for heavy loads
    elif load_kg > 500:  # Medium cargo
        load_factor = 1 + 0.0005 * load_kg  # 0.05% per kg for medium loads
    else:  # Light cargo
        load_factor = 1 + 0.0003 * load_kg  # 0.03% per kg for light loads
    
    return base_energy * grade_factor * load_factor

def energy_to_co2(energy, vehicle_type='diesel'):
    if vehicle_type == 'diesel':
        return energy * 2.68 * 1000  # L diesel -> gCO2
    elif vehicle_type == 'gasoline':
        return energy * 2.31 * 1000  # L gasoline -> gCO2 (lower than diesel)
    else:  # EV
        grid_intensity = 400  # gCO2/kWh
        return energy * grid_intensity
