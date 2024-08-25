
travel_log = [
  {
    "country":"France",
   "cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12
  },
  {
    "country":"Germany", 
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"],"total_visits":5
  }
]


def add_new_country(country, visits, list_of_cities):
  new_country = {}
  new_country["country"] = country
  new_country["total_visits"] = visits
  new_country["cities"] = list_of_cities
  travel_log.append(new_country)



country = input("What is your country? ")
visits = int(input("How many times have you been there? "))
list_of_cities = eval(input("What cities have you been to? "))


add_new_country(country, visits, list_of_cities)
print(travel_log)


print(f"{country} has been visited {visits} times.")
print(f"{list_of_cities} have been visited {visits} times.")
