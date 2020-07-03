def conversion():
    qualification = str(input("Are you converting to inches or cm? in/cm "))
    measurement = int(input("Please enter your measurement: "))
    if qualification == "in":
        return measurement / 2.54
    elif qualification == "cm":
        return measurement * 2.54
    else:
        print("Please try again")
print(conversion())