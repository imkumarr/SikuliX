running = True

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1,KeyModifier.CTRL, runHotkey)

click("1707533293515.png")
wait("1707533312462.png")
type("cal"+Key.ENTER)

try:
    SCREEN.wait("1707533589374-3.png")
except FindFailed:
    print("Image not found!")


while exists("1707533589374-1.png")and running:
    click(Pattern("1707533589374-2.png").similar(0.35).targetOffset(117,53))
    click(Pattern("1707533589374-2.png").similar(0.35).targetOffset(-119,53))
    
click(Pattern("1707533589374-2.png").similar(0.35).targetOffset(118,110))