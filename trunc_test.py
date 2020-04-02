import numpy as np
import math

def arb_round(a,thresh):
    remainder=a%thresh
    if remainder<thresh/2:
        # round down
        b=math.floor(a/thresh)
        
    else:
        #round up
        b=math.ceil(a/thresh)
    
    arb_round_a=thresh*b

    return arb_round_a

if __name__ == "__main__":
    print(trunc(12.1,7))