#heappush - don’t follow alphabetical order.

from heapq import heappush

countries = []
heappush(countries, "Thailand")
heappush(countries, "Vietnam")
heappush(countries, "Philippines")
heappush(countries, "Brazil")
heappush(countries, "China")


print("----------------------------------------------------------------------------------------")
print("These are the following list of countries from the program for applying heappush method.")
print(countries)
print("----------------------------------------------------------------------------------------")

#heappop - always get the first one, while the remaining elements might shuffle a little bit
from heapq import heappop

print("----------------------------------------------------------------------------------------")
print("These are the following list of countries from the program for applying heappop method.")
print(heappop(countries))
print(heappop(countries))
print(countries)
print("----------------------------------------------------------------------------------------")

# Python's Tuple Comparison (First Name, Last Name and Age)
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print("----------------------------------------------------------------------------------------")
print(f"Person 1 < Person 2 is " person1 < person2)
print(person2 < person3)
print("----------------------------------------------------------------------------------------")
