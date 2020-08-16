
#1.1 Tower of Hanoi
def Move(fromPol, toPol):
    print("Moving disk from ", fromPol, toPol)

def Tower(num, fromPol, toPol, sparePol):
    if num ==1:
        Move(fromPol,toPol)
    else:
        Tower(num-1,fromPol,sparePol,toPol)
        Tower(1,fromPol,toPol,sparePol)
        Tower(num-1,sparePol,toPol,fromPol)



