from Stage5 import stagewinner, pink, white, blue, purple
from friends import kyle, lee, aaron


rest_day_tomorrow = False
final_day_today = False

pinklist = pink.split("\n")
whitelist = white.split("\n")
bluelist = blue.split("\n")
purplelist = purple.split("\n")

out = """"""

players = [kyle, lee, aaron]
for player in players:
    score = 0
    for rider in player['pink']:
        for i in range(len(pinklist)):
            if rider in pinklist[i]:
                out += f"{player['player']} - pink - {rider} - {i+1}" + "\n"
                score += i+1
                break
        else:
            out += f"rider {rider} not found in pink list for {player['player']}" + "\n"
    for rider in player['white']:
        for i in range(len(whitelist)):
            if rider in whitelist[i]:
                out += f"{player['player']} - white - {rider} - {i+1}" + "\n"
                score += i+1
                break
        else:
            out += f"rider {rider} not found in white list for {player['player']}" + "\n"
    for rider in player['blue']:
        for i in range(len(bluelist)):
            if rider in bluelist[i]:
                out += f"{player['player']} - blue - {rider} - {i+1}" + "\n"
                score += i+1
                break
        else:
            out += f"{player['player']} - blue - {rider} - {len(bluelist) + 1}" + "\n"
            score += len(bluelist) + 1
    for rider in player['purple']:
        for i in range(len(purplelist)):
            if rider in purplelist[i]:
                out += f"{player['player']} - purple - {rider} - {i+1}" + "\n"
                score += i+1
                break
        else:
            out += f"{player['player']} - purple - {rider} - {len(purplelist) + 1}" + "\n"
            score += len(purplelist) + 1
    riders = set(player['pink'] + player['white'] + player['blue'] + player['purple'])
    if stagewinner in riders:
        out += f"{player['player']} had {stagewinner}" + "\n"
        score -= 5
    if rest_day_tomorrow:
        for rider in player['pink']:
            if rider in pinklist[0]:
                out += f"{player['player']} had {rider} in pink on the rest day" + "\n"
                score -= 15
                break
        for rider in player['white']:
            if rider in whitelist[0]:
                out += f"{player['player']} had {rider} in white on the rest day" + "\n"
                score -= 15
                break
        for rider in player['blue']:
            if rider in bluelist[0]:
                out += f"{player['player']} had {rider} in blue on the rest day" + "\n"
                score -= 15
                break
        for rider in player['purple']:
            if rider in purplelist[0]:
                out += f"{player['player']} had {rider} in purple on the rest day" + "\n"
                score -= 15
                break
    if final_day_today:
        for rider in player['pink']:
            if rider in pinklist[0]:
                out += f"{player['player']} had {rider} in pink at the final" + "\n"
                score -= 30
                break
        for rider in player['white']:
            if rider in whitelist[0]:
                out += f"{player['player']} had {rider} in white at the final" + "\n"
                score -= 30
                break
        for rider in player['blue']:
            if rider in bluelist[0]:
                out += f"{player['player']} had {rider} in blue at the final" + "\n"
                score -= 30
                break
        for rider in player['purple']:
            if rider in purplelist[0]:
                out += f"{player['player']} had {rider} in purple at the final" + "\n"
                score -= 30
                break
    out += f"{player['player']} - {score}" + "\n"
print(out)



