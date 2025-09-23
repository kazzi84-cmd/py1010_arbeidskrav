
"""
Created on Thu Sep  4 16:00:25 2025

@author: karin aalmo (kazzi84@hotmail.com)

En sammenlikning av årlige kostnader mellom elbil og bensinbil.

"""
#%% Kjørelengde

ÅBB = 10000   # Årlig bilbruk målt i antall kjørte kilometer



#%% Forsikring

FEB = 5000   # Årlig forsikringssum for elbil i NOK
FBB = 7500   # Årlig forsikringssum for bensinbil i NOK



#%% Trafikkforsikringsavgift

TFA = 8.38*365   # Årlig trafikkforsikringsavgift for både elbil og bensinbil



#%% Drivstoffkostnader

DEB = ÅBB*0.2*2.0   # Årlige drivstoffkostnader elbil.

DBB = ÅBB*1.0   # Årlige drivstoffkostnader bensinbil.



#%% Bomavgift

BEB = ÅBB*0.1   # Årlig bomavgift elbil.

BBB = ÅBB*0.3   # Årlig bomavgift bensinbil.



#%% Sammendrag

elbil = FEB + TFA + DEB + BEB

bensinbil = FBB + TFA + DBB + BBB

print ("De årlige utgiftene til forsikring, drivstoff",
       "og bomavgift for en elbil er", elbil, "kr.")

print ("De årlige utgiftene til forsikring, drivstoff",
       "og bomavgift for en bensinbil er", bensinbil, "kr.")

if elbil > bensinbil:
    dif = elbil - bensinbil
    print("Det koster", dif, "kr mer i året å ha elbil enn med bensinbil")
else:
    dif = bensinbil - elbil
    print("Det koster", dif, "kr mer i året å ha bensinbil enn med elbil")


