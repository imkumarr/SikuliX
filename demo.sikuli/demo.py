running = True

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

click("1707533293515.png")
wait("1707533312462.png")
type("cal" + Key.ENTER)

try:
    wait("1707533589374-4.png", 12)
except FindFailed:
    print("Image not found within the specified timeout period.")

while exists("1707533589374-1.png") and running:
    try:
        click(Pattern(Pattern("1707533589374-2.png").targetOffset(118,53)).similar(0.35).targetOffset(117, 53))
        click(Pattern(Pattern("1707533589374-2.png").targetOffset(-119,51)).similar(0.35).targetOffset(-119, 53))
    except FindFailed:
        print("One of the images not found.")
        break
    
click(Pattern(Pattern("1707533589374-2.png").targetOffset(116,104)).similar(0.35).targetOffset(118, 110))
