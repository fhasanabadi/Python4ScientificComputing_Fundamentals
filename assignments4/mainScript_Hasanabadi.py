import os
os.chdir("C:\Users\LENOVO\Desktop\Codes")

import assignment5 as X1
#define the material library 
U_walls=0
U_door=0
wall_joint_material=["outsidesurface","gypsumwallboard","woodfiber","woodbevellapped","insidesurface","commonbrick"]
wall_parallel_material=["glassfiberinsulation","woodstud"]
ratio=0.7
Material_Library={"outsidesurface":{"Rvalue":0.03},"glassfiberinsulation":{"Rvalue":0.7,"length":25},
"gypsumwallboard":{"Rvalue":0.079,"length":13},"woodstud":{"Rvalue":0.63},"woodfiber":{"Rvalue":0.23,"length":13},
"woodbevellapped":{"Rvalue":0.14},"insidesurface":{"Rvalue":0.12},"commonbrick":{"Rvalue":0.12},"Wood":{"Rvalue":0.22*50/25,"length":25},"asphalt":{
"Rvalue":0.077},"mineralinsulation":{"Rvalue":0.66}}
door=["insidesurface","outsidesurface","Wood"]
roof=["insidesurface","outsidesurface","woodfiber","asphalt","glassfiberinsulation","gypsumwallboard","Wood"]

#calling the functions

U_walls=X1.wallCalc_withParallel(wall_joint_material,wall_parallel_material,ratio,Material_Library)
U_door=X1.wallCalc_onlyInSeries(door,Material_Library)
U_roof=X1.wallCalc_onlyInSeries(roof,Material_Library)

#define the area and temperature for heat calculation
deltaT,area_wall,area_roof,area_door=20+4.8,105.8,200,2.2

opaque_surfaces={"wall":{"u":U_walls,"a":area_wall},"door":{"u":U_door,"a":area_door},"roof":{"u":U_roof,"a":area_roof}}

for i in opaque_surfaces:
    H=opaque_surfaces[i]["u"]*opaque_surfaces[i]["a"]*deltaT
    print ("The Heating Load of the "+i+" is "+str(H)+" W")


