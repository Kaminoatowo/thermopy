import sys

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
      
      print("Testing classes for thermodynamic systems: \n")
      
      myThermo_ene = system_class.thermo_system(10.2, "energy")
      
      myThermo_mat = system_class.thermo_system(11.2, "matter")
      
      test.test_class_init()
      
if __name__ == '__main__':
    test_laws()
    test_systems()