# color values are requested from the user

red = int(input("What is the value of red: "))
blue = int(input("what is the value of blue: "))
green = int(input("what is the value of green: "))

#rgbtoHex function is defined taking in the argument color

def rgbToHex(color):
    
    # the maximum and minimum color are returned
    
    return max(0, min(color, 255))

# hex is assigned a string using string formatting that turns the rgb into hex color codes, 
# the rgb function is also called on each of the values


hex = "{:01x}{:01x}{:01x}".format(rgbToHex(red), rgbToHex(green), rgbToHex(blue))

# the hex color is then converted to all uppercase
hex = hex.upper()

# if red, green, and blue is equal to 0 then an extra 3 zeros will be added
if red == 0 and green == 0 and blue == 0:
    hex = hex + "000"

# the hex color code is now printed as an f string using the variable hex.
print(f"#{hex}")