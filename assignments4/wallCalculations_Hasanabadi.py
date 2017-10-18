def wallCalc_withParallel(L1,L2,ratio,Library):
    Utot=0
    Rfinal=0
    for i in L2:
        Rtot=0
        for x in L1:
            Rtot+=Library[x]["Rvalue"]
        if i=="glassfiberinsulation":
            Utot+=ratio/(Rtot+Library[i]["Rvalue"]*90/Library[i]["length"])
        elif i=="woodstud":
            Utot+=(1-ratio)/(Rtot+Library[i]["Rvalue"])
    
    return(Utot)
    
def wallCalc_onlyInSeries(L1,Library):
    Rtot=0
    for i in L1:            
            Rtot+=Library[i]["Rvalue"]
    Utot=1/Rtot
    return(Utot)
        
#materials and library
wall_joint_material=["outsidesurface","gypsumwallboard","woodfiber","woodbevellapped","insidesurface","commonbrick"]
wall_parallel_material=["glassfiberinsulation","woodstud"]
ratio=0.7
Material_Library={"outsidesurface":{"Rvalue":0.03},"glassfiberinsulation":{"Rvalue":0.7,"length":25},
"gypsumwallboard":{"Rvalue":0.079,"length":13},"woodstud":{"Rvalue":0.63},"woodfiber":{"Rvalue":0.23,"length":13},
"woodbevellapped":{"Rvalue":0.14},"insidesurface":{"Rvalue":0.12},"commonbrick":{"Rvalue":0.12},"Wood":{"Rvalue":0.22*50/25,"length":25},
"asphalt":{
"Rvalue":0.077},"mineralinsulation":{"Rvalue":0.66}}
door=["insidesurface","outsidesurface","Wood"]
roof=["insidesurface","outsidesurface","woodfiber","asphalt","mineralinsulation"]

x=wallCalc_onlyInSeries(roof,Material_Library)









