#dictionary is like javascript object

programming_dictionary = {
    "Bug": "An error",
    "Function": "A piece of code you cna call over and over again",
    1: "A number hehe",
}

print(programming_dictionary["Bug"])
print(programming_dictionary[1])


programming_dictionary["Loop"] = "We go over and over"

print(programming_dictionary)


#Create empty
empty_dictionary = {}

#Wipe
# programming_dictionary = {}

#Edit
programming_dictionary["Bug"] = "Moth in da computer"

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



capitals = {"France": "Paris",
            "Germany": "Berlin",
            }

travel_log = {
    "France": {"cities visited":["Paris", "Lille","Dijon"],"total visits": 22},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log2 = [
    {
        "country":"France",
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    },
]