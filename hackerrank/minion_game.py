# Hackerrank Problem
# Minion Game

# Game Rules
#   Both players are given the same string.
#   Both players have to make substrings using the letters of the string.
#   Stuart has to make words (substrings) starting with consonants.
#   Kevin has to make words (substrings) starting with vowels.
#   The game ends when both players have made all possible substrings.
#
# Scoring
#   A player gets +1 point for each occurrence of the substring in the string.
#
# For Example:
#   String  = BANANA
#   Kevin's vowel beginning word = ANA
#   Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Example:
#   Word: BANANA
#   Result: Stuart 12

VOWELS = 'AEIOU'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'


def minion_game(string):
    # get scores for each player
    kevin = get_score(string, VOWELS)
    stuart = get_score(string, CONSONANTS)
    # determine winner
    if kevin > stuart:
        return f"Kevin {str(kevin)}"
    elif stuart > kevin:
        return f"Stuart {str(stuart)}"
    else:
        return "Draw"


def get_score(string, letters):
    # return score of Minion Game for string and letter set
    score = 0
    for i in range(len(string)):
        if string[i] in letters:
            score += len(string) - i
    return score


# --- TEST CASES ---
print('--- Running Test Case 1...')
result = minion_game('BANANA')
assert result == 'Stuart 12'
print('  --- Pass')

print('--- Running Test Case 2...')
result = minion_game('ZZZZZZZZZZZ')
assert result == 'Stuart 66'
print('  --- Pass')

print('--- Running Test Case 3...')
result = minion_game('EEEEEEEEEE')
assert result == 'Kevin 55'
print('  --- Pass')

s = input('Please input a word to play The Minion Game: ')
print(minion_game(s))
