modes=("Add", "Sub", "Mul", "Div")
option= select("What would you like to do?", options=modes)


click("1710759697502.png")
wait("1710759714687.png")
type("cal"+Key.ENTER)
try:
    SCREEN.wait("1707533589374-1.png")
except FindFailed:
    print("Image not found!")
    
click(Pattern("1707533589374-2.png").similar(0.35).targetOffset(-43,-3))
if option == modes[0]:
    
    click(Pattern("1707533589374.png").similar(0.31).targetOffset(119,46))
    
elif option == modes[1]:

     click(Pattern("1707533589374.png").similar(0.31).targetOffset(118,0))


elif option == modes[2]:

     click(Pattern("1707533589374.png").similar(0.40).targetOffset(116,-54))


else:

     click(Pattern("1707533589374.png").similar(0.39).targetOffset(116,-108))



click(Pattern("1707533589374.png").similar(0.28).targetOffset(-42,0))

click(Pattern("1707533589374.png").similar(0.33).targetOffset(114,108))
wait(10)
