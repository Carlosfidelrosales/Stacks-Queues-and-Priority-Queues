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

