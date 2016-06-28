####################### Magswitch Applications Assistant #######################
#
# Written by Tyler Thune
#
# Project Start Date: June 14, 2016
#
"""This program aims to implement a series of functions and calculations
commonly used by Magswitch Applications Engineers in order to increase the
efficiency of each Engineer and eventually be usable by customers in order to
help them spec their own solutions."""

################################################################################

############################### Global Constants ###############################
"""Defines additional global constants necessary throughout calculations"""

g = 9.81 #Defines the acceleration due to gravity in m/s^2

################################################################################

################### Holding Force Interpolation Calculations ###################
"""Since we do not currently have a unified equation of holding force for the
Magswitch tool set the current strategy is to interpolate between closest
available data points.
The below interpolator is intended for use on flat material. Additional
functionality will need to be added for round material
Empirical data will be required to generate the values"""

def HoldingForce (unit, t, airgap):
# HFNA = Holding Force No Airgap
# tlow = Thickness of material thinner than t, chooses closest 0 airgap point
# thigh = Thickness of material thicker than t, chooses closest 0 airgap point
# HFlow = Holding Force on thinner material (tlow)
# HFhigh = Holding Force on thicker material (thigh)
 
    HFNA = HFlow + ((t-tlow)*(HFhigh-HFlow))/(thigh-tlow)
    CInterp = HFNA/HFlow

# HFairgap = Holding Force at specified airgap
# HFthin = Holding Force at thinner airgap
# HFthick = Holding Force at thicker airgap
# AGthin = Smaller airgap
# AGthick = Larger airgap
# HF = End Holding Force per unit

    if airgap > 0:
        HFairgap = HFthin + ((airgap-AGthin)*(HFthick-HFthin))/(AGthick-AGthin)
        CAirgap = HFairgap/HFthin

    else:
        CAirgap = 1

    HF = CInterp*CAirgap*HFlow*MagEff #MagEff from look up table

################################################################################

############################ Deflection Calculations ###########################
"""This subset of code is used to calculate the deflection of any given sheet
and predict if there will be a "pry-off" condition that will cause failure"""

def DeflectCalcs (l, w, t, nodes, x1, x2):
    Fw = 1 # just for now
    I = (w*(t^3))/12 #Defines the Area Moment of Inertia for a simple rectangular cross section in m^4"""
    q = Fw/l         #Defines the Force of Weight (Fw) per unit length in N/m
    print("using something from another file!")

#Bases initial estimate on holding force requirements
    """if shear == N:
        for HF <= (4*Fw):
            #iterate up number of units until HF > 4x Fw
            #record unit count
            #use Unit count >= (Part Weight x SF)/HF if necessary
        if shear == Y:
         for HF <= (10*Fw)
            #iterate up number of units until HF > 4x Fw
            #record unit count
            #use Unit count >= (Part Weight x SF)/HF if necessary"""
    """if unitcount == 1:
        x1 = l/2
        x3 = w/2
        #check deflection calcs and other flags - 2 new functions"""
    

################################################################################


def main():

#################################### Inputs ####################################
	"""This section defines the user inputs. The end goal is to have only the
	geometryand material inputs. Ideally this will have common geometries as
	options.Presently designed only to handle flat sheet calculations."""
	
	length = input("Enter sheet length")
	width = input("Enter sheet width")
	thickness = input("Enter sheet thickness")
	material = input("Enter a material grade name")# This will need to be a selection field that pulls details from a database"""
	shear = input("Will the part be handled in shear? (Y/N)")
	destack = input("Will the tool need destacking capability? (Y/N)") #only flat
	
	#Pulled from material database in future iterations - can be relocated
	E = 210*10^9  #Defines the modulus of elasticity of for a given steel in Pa(N/m^2)- currently based on JIS SS400"""
	rho = 7900    #Defines the density of a given steel in kg/m^3 - Currently based on JIS SS400"""
	MagEff = 0.95 #Defines the magnetic holding force efficiency of a given material when compared to 1018 Mild Steel - currently based on JIS SS400"""
	
################################################################################
	
############################## General Calculations ############################
	
	#Defines the dimensions in terms of meters rather than mm
	l = length/1000
	w = width/1000
	t = thickness/1000
	
	#Calculates volume (m^3), mass (kg), and weight (N) of parts
	Volume = l*w*t
	Mass = Volume*rho
	Fw = Mass*g
	
	#Determines usable tool set if destack is required - Needs data
	    #if destack == Y:
	       #Clever bit of code that eliminates all tools that do not destack
	        #Eventually will need to figure out how to handle de-stacking pole shoes
	    #if destack == N
	        #include all tools
	    
	
################################################################################

############################## Force Calculations ############################

    

if __name__ == "__main__":
    main()



