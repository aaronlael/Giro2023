from Stage3 import stagewinner, pink, white, blue, purple
from friends import kyle, lee, aaron

pinklist = pink.split("\n")
whitelist = white.split("\n")
bluelist = blue.split("\n")
purplelist = purple.split("\n")

players = [kyle, lee, aaron]
for player in players:
    score = 0
    for rider in player['pink']:
        for i in range(len(pinklist)):
            if rider in pinklist[i]:
                print(f"{player['player']} - pink - {rider} - {i+1}")
                score += i+1
                break
        else:
            print(f"rider {rider} not found in pink list for {player['player']}")
    for rider in player['white']:
        for i in range(len(whitelist)):
            if rider in whitelist[i]:
                print(f"{player['player']} - white - {rider} - {i+1}")
                score += i+1
                break
        else:
            print(f"rider {rider} not found in white list for {player['player']}")
    for rider in player['blue']:
        for i in range(len(bluelist)):
            if rider in bluelist[i]:
                print(f"{player['player']} - blue - {rider} - {i+1}")
                score += i+1
                break
        else:
            print(f"{player['player']} - blue - {rider} - {len(bluelist) + 1}")
            score += len(bluelist) + 1
    for rider in player['blue']:
        for i in range(len(purplelist)):
            if rider in purplelist[i]:
                print(f"{player['player']} - purple - {rider} - {i+1}")
                score += i+1
                break
        else:
            print(f"{player['player']} - purple - {rider} - {len(purplelist) + 1}")
            score += len(purplelist) + 1
    riders = set(player['pink'] + player['white'] + player['blue'] + player['purple'])
    if stagewinner in riders:
        score -= 1
    print(f"{player['player']} - {score}")
    



