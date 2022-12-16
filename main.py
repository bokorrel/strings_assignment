# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Players that scored
player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'

# Goals
goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when, according to the format:
# <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = player_1 + ' ' + str(goal_0) + ', ' + player_2 + ' ' + str(goal_1)
print(scorers)

# Use f-strings or the +-operator to create a single string with information about who scored when in the format:
# <scorer_name> scored in the <when_they_scored>nd minute
# <scorer_name> scored in the <when_they_scored>th minute
report = f"{player_1} scored in the {str(goal_0)}nd minute\n{player_2} scored in the {str(goal_1)}th minute"
print(report)

# hoose a player that played in the soccer match and store his name as a string in the variable player.
player = 'Frank Rijkaard'

# use slicing and the find-method (help) to isolate and store the player's first name.
first_name = player[0:5]
print(first_name)

# use find, slicing and len to isolate and store the length of their last name.
last_name_len = len(player[6:14])
print(last_name_len)

# isolate and store the player's name in this format: G. von Examplestein
name_short = player[0] + '. ' + player[6:14]
print(name_short)

# this is what the crowd chants when it looks like your player is going to score a goal 
# their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name.
# Because Gut has 3 letters in his name, we repeat his name 3 times. 
# Make sure the last character of this string is not a space! For our example player: Gut! Gut! Gut!
chant = (first_name + '! ') * (len(first_name)-1) + first_name + '!'
print(chant)

# Make super-sure the last character of chant is not a space by using the inequality operator (!=). 
# This variable needs to be a boolean, not a string. You can create the value for this variable by comparing 
# the last character of chant with a space character. 
good_chant = chant[-1] != ' '
print(good_chant)