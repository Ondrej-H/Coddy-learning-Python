# task:
'''
In a competitive gaming tournament, players participate in different matches. Your task is to analyze player participation across three matches using Python sets.

You'll be given three sets of players:

match1: Players who participated in Match 1
match2: Players who participated in Match 2
match3: Players who participated in Match 3
Your task is to:

Find players who participated in all three matches
Identify players who participated in exactly two matches
Determine players who participated in only one match
Count the total number of unique players in the tournament
Find players who participated in Match 1 but not in Match 2 or Match 3
Print the results in the following format:

Use sorted(list(set_name)) to display players in alphabetical order
Print the exact output format shown in the example
'''

# Example input:
'''
{"Alice", "Bob", "Charlie", "Diana"}
{"Charlie", "Diana", "Eve", "Frank"}
{"Alice", "Diana", "Frank", "George"}
'''

# Example output:
'''
Players in all matches: ['Diana']
Players in exactly two matches: ['Alice', 'Charlie', 'Frank']
Players in only one match: ['Bob', 'Eve', 'George']
Total unique players: 7
Players in Match 1 only: ['Bob']
'''

# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# Coddy solution - better
# 1. Find players who participated in all three matches
players_in_all_matches = match1 & match2 & match3

# 2. Find players who participated in exactly two matches
players_in_two_matches = (
    (match1 & match2) | (match1 & match3) | (match2 & match3)
) - players_in_all_matches

# 3. Find players who participated in only one match
players_in_one_match = (
    (match1 - match2 - match3)
    | (match2 - match1 - match3)
    | (match3 - match1 - match2)
)

# 4. Count total unique players
total_unique_players = len(match1 | match2 | match3)

# 5. Find players in Match 1 only
players_in_match1_only = match1 - match2 - match3

# Print results in the specified format
print("Players in all matches:", sorted(list(players_in_all_matches)))
print("Players in exactly two matches:", sorted(list(players_in_two_matches)))
print("Players in only one match:", sorted(list(players_in_one_match)))
print("Total unique players:", total_unique_players)
print("Players in Match 1 only:", sorted(list(players_in_match1_only)))


# my solution
# 1. Find players who participated in all three matches
in_all_matches = sorted(list(match1 & match2 & match3))

# 2. Find players who participated in exactly two matches
in_two_matches = sorted(list(((match1 & match2) | (match1 & match3) | (match2 & match3)) - (match1 & match2 & match3)))

# 3. Find players who participated in only one match
only_one_match = sorted(list((match1 - match2 - match3) | (match2 - match1 - match3) | (match3 - match2 - match1)))

# 4. Count total unique players
total_players = len(match1 | match2 | match3)

# 5. Find players in Match 1 only
match1_only = sorted(list(match1 - match2 - match3))

# Print results in the specified format
print(f"Players in all matches: {in_all_matches}")
print(f"Players in exactly two matches: {in_two_matches}")
print(f"Players in only one match: {only_one_match}")
print(f"Total unique players: {total_players}")
print(f"Players in Match 1 only: {match1_only}")



