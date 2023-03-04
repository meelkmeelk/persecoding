start = input()

dance = "+&><"

start_index = dance.find(start)

print(dance[start_index:] + dance[:start_index] + dance[start_index:] + dance[:start_index])
