def calculate_annihilation_energy(mass_grams):
    # Constants
    c = 3 * 10**8  # Speed of light in meters per second (m/s)
    
    # Convert grams to kilograms since SI units are required for this calculation
    mass_kg = mass_grams / 1000
    
    # Total mass (matter + antimatter) is double the input mass
    total_mass = 2 * mass_kg
    
    # Calculate energy released (E = mc^2)
    energy_joules = total_mass * c**2
    
    # Print result
    print(f"Energy released from {mass_grams} grams of antimatter and {mass_grams} grams of matter:")
    print(f"{energy_joules:.2e} joules")
    return energy_joules

# Example usage
mass_of_antimatter = float(input("Enter the mass of antimatter in grams: "))
calculate_annihilation_energy(mass_of_antimatter)
