# Program for Reading the data from the Keyboard and Wrote the File Dynamically
with open("Random.info", "a") as keybrd_data:
    print("Enter the Data for Writing to the File and Press '.' for Stop")
    print("-------------------------------------------------------------------")
    while (True):
        dynamic_data = input()
        if dynamic_data == ".":
            break
        else:
            keybrd_data.write(dynamic_data + "\n")
