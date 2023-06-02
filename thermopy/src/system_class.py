class thermo_system:
    
    def __init__(self, thermo_type=None, boundaries=None):

        if thermo_type is None:
            self.thermo_type = "i"
        elif thermo_type in ["open", "o", "closed", "c", "t-isolated", "ti", "m-isolated", "mi", "isolated", "i"]:
            self.thermo_type = thermo_type
        else:
            raise Exception("thermo_system class only accepts types: \n\topen\t\to\n\tclosed\t\tc\n\tt-isolated\tti\n\tm-isolated\tmi\n\tisolated\ti\n")
        
        if boundaries is None:
            self.boundaries = [[["r", "f"], ["r", "f"]], 
                            [["r", "f"], ["r", "f"]],
                            [["r", "f"], ["r", "f"]]]

    # state quantities
    energy = 0
    volume = 0
    pressure = 0
    entropy = 0
    temperature = 0
    number_of_particles = 0
    chemical_potential = 0
    mass = 0