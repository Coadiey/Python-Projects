# Author:       Coadiey Bryan
# CLID/Section: C00039405/Sec.003
# lab9.py 
import math

def AC(radius):
    area = math.pi * radius ** 2
    return area 
# WRITE ALL THE OTHER FUNCTIONS 
def AR(length, width):
    area = length * width
    return area
def VC(radius, height):
    volume = math.pi*radius*radius*height
    return volume
def VR(length, width, height):
    volume = length*width*height
    return volume
def VS(radius):
    volume = 4/38*math.pi*radius*radius*radius
    return volume
def SAC(length):
    surface = 6*length*length
    return surface
def SAS(radius):
    surface = 4*math.pi*radius*radius
    return surface

def main():

    infile = open("lab9_input.py","r")

    # get calculation type, but wait on dimension(s) because
    # number of dimensions is dependent on type of shape
    type = (infile.readline()).strip()

    while (type != "###"): 
        if (type == "AC"):
            # read only one dimension for a circle
            radius = eval(infile.readline())
            circleArea = AC(radius)
            print(format("Area of a Circle","30s"),format(circleArea,"15.2f"))
        elif (type == "AR"):
            length = eval(infile.readline())
            width = eval(infile.readline())
            rectangleArea = AR(length,width)
            print(format("Area of a Square/Rectangle","30s"),format(rectangleArea,"15.2f"))
        elif (type == "VC"):
            radius = eval(infile.readline())
            height= eval(infile.readline())
            cylinderVolume = VC(radius,height)
            print(format("Area of a Square/Rectangle","30s"),format(cylinderVolume,"15.2f"))
        elif (type == "VR"):
            length = eval(infile.readline())
            width = eval(infile.readline())
            height = eval(infile.readline())
            rectangularPrismVolume = VR(length,width,height)
            print(format("Area of a Square/Rectangle","30s"),format(rectangularPrismVolume,"15.2f"))
        elif (type == "VS"):
            radius = eval(infile.readline())
            sphereVolume = VS(radius)
            print(format("Area of a Square/Rectangle","30s"),format(sphereVolume,"15.2f"))
        # do the processing for all other types of calculations 
        elif (type == "SAC"):
            length = eval(infile.readline())
            cubeSurfaceArea = SAC(length)
            print(format("Area of a Square/Rectangle","30s"),format(cubeSurfaceArea,"15.2f"))
        elif (type == "SAS"):
            radius = eval(infile.readline())
            sphereSurfaceArea = SAS(radius)
            print(format("Area of a Square/Rectangle","30s"),format(sphereSurfaceArea,"15.2f"))
        # get calculation type, but wait on dimension(s)
        type = (infile.readline()).strip()


    # close the file when you exit the while loop 
    infile.close()
    
main() 
