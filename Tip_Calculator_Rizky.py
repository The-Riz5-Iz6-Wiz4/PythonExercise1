#Input

Subtotal = float(input("Enter the subtotal: $"))
Gratuity = float(input("Enter the tip amount(as a %): "))

#Tip and Total

Tip = Subtotal*(Gratuity/100)
Total = Subtotal + Tip

#Formatting

FormatSubtotal = format( Subtotal, ",.2f")
FormatTip = format( Tip, ",.2f")
FormatTotal = format ( Total, ",.2f")

#FinalOutput

print(f"""Subtotal: ${FormatSubtotal}
Tip: ${FormatTip}
Total: ${FormatTotal}""")
