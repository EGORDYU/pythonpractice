print("Welcome to python kid")
print("      --..,_                     _,.--.\n"
      "         `'.'.                .'`__ o  `;__.\n"
      "            '.'.            .'.'`  '---'`  `\n"
      "             '.`'--....--'`.'\n"
      "               `'--....--'`\n")

print("This is a project of creativity in the jungle")
print("Basically you can get hard gapped by mid or top at any time. Choose wisely.")

start = input("Where do you want to start? Blue, Red or Chickens?\n")

if start == "Blue":
    print("You are too weak to fight the kindred lvl 2 invade, you died. 💀")
if start == "Chickens":
    print("You get a fast level two and have good reclear potential!")
    scuttle = input("You arrive at the scuttle, but your bot lane is dying! Do you (gank) or (take) the scuttle?\n")
    if scuttle == "take":
        print("Xin Zhao was waiting in the bush and kills you, and your botlane dies. Your adc quits the game. 💀")
    elif scuttle == "gank":
        print("Succesful gank but your botlane still flames you and you lose a part of you soul... 💀")
if start == "Red":
    print("By far the best way to start you will be ahead this game!")
    invade = input("You are diana and amumu invades you, what do you do? (kill or run)")
    if invade == "kill":
        print("Good choice, amumu is one of the weakest early game junglers and their jungler is rarted. Free win.")
    elif invade == "run":
        print("You run away but you're hard gapped by mid and top they both rotate to cut you off and you die + your midlaner and toplaner lose their whole waves. 💀")