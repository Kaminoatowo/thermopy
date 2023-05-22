import sys

def test_zeroth(function):

    print("\nTesting zeroth law")
    
    t1 = 31
    t2 = 135
    t3 = 135

    print("\tTesting systems at same temperature ...")

    assert function(t3, t2)

    print("\tTesting systems at different temperatures ...")     
    
    assert not function(t1, t2)     
                        
def test_first(function):
    
    print("\nTesting first law")
    
    U0 = 150
    U1 = 125
    U2 = 320
    
    Q = 50
    W = Q - (U2 - U0)
    
    print("\tTesting conservation of energy ...")
    
    assert function(Q, W, U2 - U0)
    
    print("\tTesting violation of conservation of energy ...")
    
    assert not function(Q, W, U1 - U0)
    
def test_second(function):
    
    print("\nTesting second law")
    
    S0 = 0.12
    S1 = 0.45
    S2 = 0.08
    
    print("\tTesting entropy production ...")
    
    assert function(S0, S1)
    
    print("\tTesting entropy reduction ...")
    
    assert not function(S0, S2)
   