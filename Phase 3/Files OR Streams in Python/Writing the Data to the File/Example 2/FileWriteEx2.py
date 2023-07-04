# Program for Demonstrating Writing the data to the file
sctinfo = {10000: "Rossum", 20: "Ritche", 30: "Travis", 40: "Simon"}
with open("scit.info","a") as sciencetistinfo:
    sciencetistinfo.writelines(str(sctinfo) + "\n")

