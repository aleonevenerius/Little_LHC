# Libraries
import random
import time

# Variables to LHC's Body
LHCTOP = "################\n##/////-###################||||||||\n##|/|###-##|/|###-##|/|###-##|/|##~~####|/|##|/|###-###|/|####\n########################|/|##-###|/|##-#||###-####|/|#####|/|###-###|/|######|/|##-#||\n============================================================================================"
LHCDOWN = "============================================================================================\n########################|/|##-###|/|##-#||###-####|/|#####|/|###-###|/|######|/|##-#||\n##|/|###-##|/|###-##|/|###-##|/|##~~####|/|##|/|###-###|/|####\n##/////-###################||||||||\n################"

# Particles
a = "*"
b = a
P_a = random.randint(0,91)
P_b = random.randint(0,91)

SPACE = list("                                                                                            ") # 92 -> 0,91

# Functions to explode
def ToExplode():
    EXPLOSION = explosao = """              ·    .       *       .
         .        /  |  /       ·
      *       · ---/ | /--- ·       *
                /   /|/   /
          · ------>  O  <------ ·
                /   /|/   /
      .       /  / | /  /       .
         *      ·  |  ·      *
              .    / /    .
                   ·"""
    print(EXPLOSION)

# Function to wait
def ToWait():
    time.sleep(0.05)

# Function to move the particles
def ToCast():
    SPACE[P_a] = a
    SPACE[P_b] = b

# Function to create the LHC's body
def ToBody():
    print("\n")
    print(LHCTOP)
    print("".join(SPACE))
    print(LHCDOWN)
    print("\n")

_ = True

# Main loop
while _:    
    ToCast()
    
    if P_a == P_b:
        ToExplode()
        print("The particles crash themselves. Bazinga!\nNow, Ana Maria can solve String Theory.\nCongratulations!")
        _ = False
    
    else:
        if P_a < P_b:
            SPACE[P_a] = " "
            P_a += 1
            ToCast()
            ToWait()
            ToBody()

        elif P_a > P_b:
            SPACE[P_b] = " "
            P_b += 1
            ToCast()
            ToWait()
            ToBody()
