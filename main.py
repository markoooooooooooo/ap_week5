# refactoring means to
# restructure code without
# changing its external behavior
# This helps improve code readability
# and maintainability.
from problem_set1 import problem1
from advanced_slicing import advanced_slice
#call the functions
problem1() # this is an abstract representation of the function




# c. Reverse the entire string using slicing.

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"



# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."



# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.




alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[7:10])
print(alphabet[0:13:2])
print(alphabet[::-1])






motto = ["Make", "haste", "slowly."]
joined_motto = ' '.join(motto)
split_on_a = joined_motto.split('a')

sentence = "Life is what happens when you are busy making other plans."
replaced_busy = sentence.replace("busy", "distracted")
replaced_plans = sentence.replace("plans", "mistakes")

word = "Iteration"
repeated_word = word * 7

quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
has_moonlight = "moonlight" in quote2

phrase = "Supercalifragilisticexpialidocious"
num_chars = len(phrase)
count_i = phrase.count('i')
