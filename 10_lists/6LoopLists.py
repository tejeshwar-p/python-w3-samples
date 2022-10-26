# We can loop through the list items by using for loop
weather_list = ["sunny", "chilly", "raining", "thunderstorm", "drizzle"]
for weather in weather_list:
    print(weather)
print()

# Loop through the index numbers
for i in range(len(weather_list)):
    print(weather_list[i])
print()

# Using a while loop
i = 0
while i < len(weather_list):
    print(weather_list[i])
    i += 1
print()

# Looping using list comprehension
# This offers short syntax
[print(x) for x in weather_list]

