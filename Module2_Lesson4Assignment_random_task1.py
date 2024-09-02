# Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

# importing random dunction to generate and select randomly

import random

moods= ["Happy", "Sad", "Energetic", "Calm", "Grateful", "Curious", "Introspective"]
days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# range will create guidlines to execute random moods for different days. F string for easier readability and to be more specific for defining random moods for random days.
for i in range(len(days)):
    mood = random.choice(moods)
    print(f"{days[i]}: {mood}")

