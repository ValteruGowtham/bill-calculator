size=input("size of the pizza S,M,L:")
pepper=input("pepper you want s or n:")
chesse=input("chesse you want y:")
bill=0
if (size=="S"):
    bill += 200
if (size=="M"):
    bill += 220
if (size=="L"):
    bill += 250
if pepper =="s":
    if (size=="S"):
        bill += 15
    elif (size=="M" or size=="L"):
        bill += 25
if (chesse=="y"):
    bill+=10
print(bill)

        
