class thermo_system:
    
    def __init__(self, vol, perm):
        # volume
        self.vol = vol
        # permeability : energy, matter
        print(perm)
        if self.test_permeability(perm):
            self.perm = perm
        
    def test_permeability(perm):
        assert perm in ["energy", "matter", 'e', 'm']