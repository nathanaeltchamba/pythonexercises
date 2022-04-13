places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

places = list(filter(lambda location: location.strip(), places))


print(places)

# = [Argentina, San Diego, Boston, New York]


# HINT: LOOK FOR A STRING METHOD THAT REMOVES WHITESPACE
