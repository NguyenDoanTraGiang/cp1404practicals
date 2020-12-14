COLOUR_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Beige": "#f5f5dc", "Black": "#000000",
                  "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "Brown": "#a52a2a", "CadetBlue": "#5f9ea0",
                  "Coral": "#ff7f50", "CornflowerBlue": "#6495ed", "DarkGreen": "#006400", "DarkOrange": "#ff8c00"}
print(COLOUR_TO_CODE)
colour_name = input("Enter a name of a color: ")
blank_name = False
while not blank_name:
    if colour_name in COLOUR_TO_CODE:
        print(COLOUR_TO_CODE[colour_name])
    elif colour_name == "":
        print("End of program")
        break
    else:
        print("Invalid color name")
    colour_name = input("Enter a name of a color: ")
