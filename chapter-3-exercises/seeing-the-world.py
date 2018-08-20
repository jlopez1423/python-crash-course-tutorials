########################################################################
#                                                                     ##
# 3-8: Think of at least five laces in the world you'd like to visit  ##
#                                                                     ##
########################################################################

#store the locations in a list
locations = ['Sweeden', 'Norway', 'Costa Rica', 'Canada', 'Alaska']

#print list
print(locations)

#use sorted to print alphabatized list without modifying it
print(sorted(locations))

#Show that it's still in correct order
print(locations)

#Use sorted to reverse order
locations.reverse()
print(locations)
locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

########################################################################
#                                                                     ##
#                       3-9: Dinner Guests:                           ##
#                                                                     ##
########################################################################

#Print a message that says how many guests you're expecting for dinner
guest_list = ['Serena', 'Ginger', 'Newton', 'Melany']
print("We have " + str(len(guest_list)) + " guests showing up.")