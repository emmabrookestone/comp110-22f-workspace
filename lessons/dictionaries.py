"""Demonstrations of dictionary capabilities."""


#Decalring the type of a dictionary
schools: dict[str, int]

#Initialize to an empty dictionary
schools = dict()

#Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

#print a dictionary literal representation
print(schools)

#Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary
#By its key
#schools.pop("Duke")

#test for the existence of a key
is_duke_present : bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

#Also can test like this
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")


# Update / reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

#demonstration of dictionary literals

#example of the empty dictionary literal
schools = {} #same as dict()
print(schools)

#altnernatively initialize key-valu pairs
schools = {"UNC": 19400, 
"Duke": 6717, 
"NCSU": 2650
}
print(schools)
#can also do like this schools = {"UNC": 19400, "Duke": 6717, "NCSU": 2650}


#what happens when a key does not exist
print(schools["UNCC"])