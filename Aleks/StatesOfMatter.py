#Author: @MiggyYTOfficial ("Check my YouTube out ;)")
#Tutorial on how to use this script: https://youtu.be/c_-hVofQ1zk

#Finding an atomic radius from an fcc or bcc lattice constant
import math

class lattice_constant():

    def __init__(self, val1, val2):
    
        def fcc(a):
            fcc = 2*math.sqrt(2)*a
            print(f"{fcc}. pm")
            print(f"Round up: {round(fcc)}")

        def bcc(b):
            bcc = (4/math.sqrt(3))*b
            print(f"{bcc}. pm")
            print(f"Round up: {round(bcc)}")

        
        Type = val1
        pm = float(val2)
        
        if Type == "a":
            fcc(pm)
        elif Type == "b":
            bcc(pm)

        else:
            print("Error")
    
class radius():
    def __init__(self, val1, val2):
        
        def fcc(a):
            fcc = (1/(2*math.sqrt(2))) * a
            print(f"{fcc}. pm")
            print(f"Round up: {round(fcc)}")

        def bcc(b):
            bcc = (math.sqrt(3)/(4)) * b
            print(f"{bcc}. pm")
            print(f"Round up: {round(bcc)}")

            
        Type = val1
        pm = float(val2)
        
        if Type == "a":
            fcc(pm)
        elif Type == "b":
            bcc(pm)
        else:
            print("Error")
        

if __name__ == "__main__":
    
    Run = True
    
    while Run == True:
        
        Solve = input("""
Solving for what?
a: lattice constant
b: radius

Which one:""")

        print("---")

        Type = input("""
Which unit cell?
a: fcc
b: bcc 

Which one: """)
        
        pm = float(input("pm Value: "))
        
        if Solve == "a":
            lattice_constant(Type,pm)
        elif Solve == "b":
            radius(Type,pm)
        
        print("---")
        check = input("Press L to Leave, otherwise press anything else: ")
        
        if check == "L":
            Run = False
        else:
            pass
        
    
    
    
