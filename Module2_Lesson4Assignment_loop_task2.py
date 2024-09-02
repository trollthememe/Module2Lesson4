#Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use #nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a #mood from a predefined list and print it. Use the random module again to randomly select the mood.

import random
moods = ["Happy", "Sad", "Energetic", "Calm", "Curious", "Grateful", "Introspective"]
time = ["Morning", "Afternoon", "Evening"]
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sumday"]
#since another variable is being added to task, another loop will be created to address this for time
for i in range(len(day)):
    for t in time:
        mood = random.choice(moods)
        print(f"{day[i]} {t}: {mood}")