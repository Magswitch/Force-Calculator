from unit import Unit
import part

def holdingCalc(unit, material, geometry):

    # start with thicknesses to scan through the data that we have.
    myList = unit.thicknesses

    #Start at the front and iterate forwards until we find a value lower than the entered thickness
    index=0
    for i,value in enumerate(myList):
        print(i,value)
        if value>geometry.height:
            index=i-1
            break

    # once we have the index of the lower bound, we know that the next index is the upper bound
    x1 = myList[index]
    x2 = myList[index + 1]
    y1 = unit.forces[index]
    y2 = unit.forces[index +1]

    # with our two coordinates we can perform a linear interpolation
    intForce = y1 + ((geometry.height - x1)*((y2-y1)/(x2-x1))) 

    print ("Interpolated Holding Force:  %s Kg" %intForce)

def main():

    ## Testing script for development - will be routed/called using flask on deployment
    thickness = input("Please suplly the material thickness:   ")
    Mfortyforty = Unit('M4040')
    steel = part.Material("Steel")
    block = part.Geometry(1,2, thickness)

    holdingCalc(Mfortyforty, steel, block)


if __name__ == "__main__":
    main()

