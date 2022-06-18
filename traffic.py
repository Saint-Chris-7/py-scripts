nairobi={"ns":"green","ew":"red"}
nakuru={"ns":"red","ew":"green"}

def spotlight(lights):
    for key in lights.keys():
        if lights[key]=="green":
            lights[key]= "yellow"
        elif lights[key]== "yellow":
            lights[key]= "red"
        elif lights[key]== "red":
            lights[key]= "green"
    assert 'red' in lights.values(), 'Neither light is red! ' + str(lights)

spotlight(nairobi)

    