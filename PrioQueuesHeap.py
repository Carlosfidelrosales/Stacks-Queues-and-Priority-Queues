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
#  Python determines that person1 should go before person2 based on their last names since they share the same first name, but Python doesn’t look at their ages because the ordering is already known. The age becomes important in the second comparison between person2 and person3, who happen to have the same first and last names.
person1 = ("Juan", "Bata", 60)
person2 = ("Juan", "Dela Cruz", 60)
person3 = ("Juan", "Dela Cruz", 35)

print("----------------------------------------------------------------------------------------")
print(person1 < person2)
print(person2 < person3)
print("----------------------------------------------------------------------------------------")

