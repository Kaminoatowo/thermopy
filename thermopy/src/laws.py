def zeroth(T1, T2):
    if T1 == T2: 
        return True
    else: 
        return False
    
def first(Q, W, dU):
     if dU == Q - W: 
         return True
     else:
         return False
         
def second(S0, S1):
    if S1 >= S0:
        return True
    else:
        return False