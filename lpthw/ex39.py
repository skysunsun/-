# create a mapping of state to abbreviation
states = {'oregon': 'OR','florida': 'FL','california': 'CA','new york': 'NY','michigan': 'MI'}

#create a basic set of states and some cities in them
cities = {
    'CA': 'san francisco',
    'MI': 'detroit',#不要忘记加逗号
    'FL': 'jacksonville',
    }
#add some more city
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

print('-' * 10)
print("michigan's abbreviation is: ", states['michigan'])
print("florida's abbreviation is: ", states['florida'])

# do it by using the state then cities dict
print('-' * 10)
print("michigan has: ",cities[states['michigan']])
print("florida has: ",cities[states['florida']])

#print every state abbreviation
print('-' * 10)
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by state that might not be There
state = states.get('Texas')

if not state:
    print("sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
