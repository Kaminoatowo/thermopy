from test import test 

def test_laws():
    
    from src import laws
    
    print("Testing laws of thermodynamics: \n")
    
    test.test_zeroth(laws.zeroth)
    test.test_first(laws.first)
    test.test_second(laws.second)
    
    print("\nEverything passed\n")
    print("---\n")

def test_systems():
    
    from src import system_class
    from src import constants
    
    print("Testing classes for thermodynamic systems: \n")

    myThermo_open = system_class.ideal_gas("o") 

    myThermo_open.volume = 10
    myThermo_open.pressure = 1
    myThermo_open.number_of_particles = constants.avogadro
    myThermo_open.temperature = 135

    print(myThermo_open.equation_of_state())
      
if __name__ == '__main__':
    test_laws()
    test_systems()