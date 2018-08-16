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
