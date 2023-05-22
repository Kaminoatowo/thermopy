class thermo_system:
    
    def __init__(self, thermo_type):

        if thermo_type in ["open", "o", "closed", "c", "t-isolated", "ti", "m-isolated", "mi", "isolated", "i"]:
            self.thermo_type = thermo_type
        else:
            raise Exception("thermo_system class only accepts types: \n\topen\t\to\n\tclosed\t\tc\n\tt-isolated\tti\n\tm-isolated\tmi\n\tisolated\ti\n")
        
    # state quantities
    volume = 0
    energy = 0
    entropy = 0
    pressure = 0
    temperature = 0
    number_of_particles = 0
    mass = 0