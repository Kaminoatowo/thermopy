from .constants import *
from math import log

class ideal_gas:
    
    def __init__(self, thermo_type=None, boundaries=None):

        if thermo_type is None:
            self.thermo_type = "i"
        elif thermo_type in ["open", "o", "closed", "c", "t-isolated", "ti", "m-isolated", "mi", "isolated", "i"]:
            self.thermo_type = thermo_type
        else:
            raise Exception("ideal_gas class only accepts types: \n\topen\t\to\n\tclosed\t\tc\n\tt-isolated\tti\n\tm-isolated\tmi\n\tisolated\ti\n")
        
        if boundaries is None:
            self.boundaries = [[["r", "f"], ["r", "f"]], 
                            [["r", "f"], ["r", "f"]],
                            [["r", "f"], ["r", "f"]]]

    # state quantities
    internal_energy = 0
    volume = 0
    pressure = 0
    entropy = 0
    temperature = 0
    number_of_particles = 0
    chemical_potential = 0
    mass = 0

    # equation of state
    def equation_of_state(self):
        return (self.pressure*self.volume 
                - boltzmann * self.number_of_particles * self.temperature)

    # derivative quantities
    specific_heat_v_mol = 1
    specific_heat_p_mol = specific_heat_v_mol + R
    heat_capacity_v = specific_heat_v_mol * number_of_particles * avogadro
    heat_capacity_p = heat_capacity_v + number_of_particles * boltzmann

    # thermodynamic processes
    def isothermal(self, new_volume=None, new_pressure=None):

        work_local = self.pressure * self.volume

        if new_volume is None:
            if new_pressure is None:
                raise Exception("At least a new volume or a new pressure must be passed as argument.")
            else:
                new_volume = work_local / new_pressure

        work = (work_local * log(new_volume / self.volume))

        heat = work 

        self.volume = new_volume
        if new_pressure is None:
            self.pressure = work_local / new_volume
        else:
            self.pressure = new_pressure

        return heat, work
    
    def isobaric(self, new_volume=None, new_temperature=None):

        if new_temperature is None:
            if new_volume is None:
                raise Exception("At least a new volume or a new temperature must be passed as argument.")
            else:
                new_temperature = self.temperature / self.volume * new_volume

        work = self.number_of_particles * boltzmann * (new_temperature - self.temperature)

        heat = self.heat_capacity_p * (new_temperature - self.temperature)

        if new_volume is None:
            self.volume = self.volume / self.temperature * new_temperature
        else: 
            self.volume = new_volume
        self.temperature = new_temperature
        self.internal_energy += self.heat_capacity_v * (new_temperature - self.temperature)

        return heat, work
    
    def isochoric(self, new_pressure=None, new_temperature=None):

        if new_temperature is None:
            if new_pressure is None:
                raise Exception("At least a new pressure or a new temperature must be passed as argument.")
            else:
                new_temperature = self.temperature / self.pressure * new_pressure

        work = 0.0

        heat = self.heat_capacity_v * (new_temperature - self.temperature)

        if new_pressure is None:
            self.pressure = self.pressure / self.temperature * new_temperature
        else: 
            self.pressure = new_pressure
        self.temperature = new_temperature
        self.internal_energy += heat

        return heat, work
    
    def adiabatic(self, new_volume=None, new_pressure=None, new_temperature=None):
        
        gamma = self.heat_capacity_p / self.heat_capacity_v

        if new_temperature is None:
            if (new_pressure is None) and (new_volume is None):
                raise Exception("At least one of new volume, new pressure or new temperature must be passed as argument.")
            elif new_volume is None:
                new_temperature = (new_pressure / self.pressure) ^ (1 - 1 / gamma) * self.temperature            
            elif new_pressure is None:
                new_temperature = (self.volume / new_volume) ^ (gamma - 1) * self.temperature
            
        work = - self.heat_capacity_v * (new_temperature - self.temperature)

        heat = 0.0

        if new_volume is None:
            self.volume = (self.temperature / new_temperature) ^ (1 / (gamma - 1)) * self.volume
        if new_pressure is None:
            self.pressure = (new_temperature / self.temperature) ^ (gamma / (gamma -1)) * self.pressure
        self.temperature = new_temperature
        self.internal_energy -= work

        return heat, work
    
