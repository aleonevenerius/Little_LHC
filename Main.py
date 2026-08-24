# Libraries
import random
import time

# Variables to LHC's Body
LHCTOP = """
################
##/////-###################||||||||
##|/|###-##|/|###-##|/|###-##|/|##~~####|/|##|/|###-###|/|####
########################|/|##-###|/|##-#||###-####|/|#####|/|###-###|/|######|/|##-#||
============================================================================================"""
LHCDOWN = """
============================================================================================
########################|/|##-###|/|##-#||###-####|/|#####|/|###-###|/|######|/|##-#||
##|/|###-##|/|###-##|/|###-##|/|##~~####|/|##|/|###-###|/|####
##/////-###################||||||||
################"""

# Particles
a = "*"
b = a
P_a = random.randint(0,91)
P_b = random.randint(0,91)

SPACE = list("                                                                                            ") # 92 -> 0,91

# Functions to explode
def ToExplode():
    EXPLOSION = explosao = """
    ·    .       *       .
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
    # When the particles crash
    if P_a == P_b:
        ToExplode() # Explosion
        print("The particles crash themselves. Bazinga!\nNow, Ana Maria can solve String Theory.\nCongratulations!")
        _ = False # End of the programme

    # When the particles do not crash
    else:
        # Particle A's position is shorter than Particle B's position
        if P_a < P_b:
            SPACE[P_a] = " "
            P_a += 1
            ToCast()
            ToWait()
            ToBody()
        # # Particle B's position is shorter than Particle A's position
        elif P_a > P_b:
            SPACE[P_b] = " "
            P_b += 1
            ToCast()
            ToWait()
            ToBody()
