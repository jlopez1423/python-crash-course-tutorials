#3-4: create a list of people
#list that includes at least 3 people
guest_list = ['Serena', 'Ginger', 'Newton', 'Melany']
print("Hello " + guest_list[0] + " please come to dinner.")
print("Hello " + guest_list[1] + " please come to dinner.")
print("Hello " + guest_list[2] + " please come to dinner.")
print("Hello " + guest_list[3] + " please come to dinner.")

#3-5: Changing guest list
missing_guest = guest_list[2]
guest_list[2] = 'Petunia'
print("Hello " + guest_list[0] + " please come to dinner.")
print("Hello " + guest_list[1] + " please come to dinner.")
print("Hello " + guest_list[2] + " please come to dinner.")
print("Hello " + guest_list[3] + " please come to dinner.")
print("The person who can't make it is " + missing_guest.title() + ".")

#3-6:more guests:
#add a print statement informing people that bigger table has been found
guest_list = ['Serena', 'Ginger', 'Newton', 'Melany']
print("Found a bigger table")
guest_list.insert(0, 'Billy')
guest_list.insert(2, 'Bob')
guest_list.append('Goat')
print("Hello " + guest_list[0] + " please come to dinner.")
print("Hello " + guest_list[1] + " please come to dinner.")
print("Hello " + guest_list[2] + " please come to dinner.")
print("Hello " + guest_list[3] + " please come to dinner.")
print("Hello " + guest_list[4] + " please come to dinner.")
print("Hello " + guest_list[5] + " please come to dinner.")
print("Hello " + guest_list[6] + " please come to dinner.")

#3-7 Shrinking Guest List
print("I can only invite two people")

popped = guest_list.pop()
print(popped + " you are no longer invited")
popped = guest_list.pop()
print(popped + " you are no longer invited")
popped = guest_list.pop()
print(popped + " you are no longer invited")
popped = guest_list.pop()
print(popped + " you are no longer invited")

print(guest_list[0] + " you are still invited")
print(guest_list[1] + " you are still invited")

del guest_list[0]
del guest_list[0]
del guest_list[0]

print(guest_list)