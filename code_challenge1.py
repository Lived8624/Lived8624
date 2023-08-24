# Code Challenge 1
# Python - Code Challenge 1 01
# Make a list of your favourite Movies, the list should have minimum 8
# elements.
# Print a specified list after removing the 5th element.
# Insert your favourite movie director name at the 4th index position of
# the list and print out the list elements.
# List out the 4th element in the list.
# Add additional item to the current list and display the list.

print("1)")
Fav=[" The Dark Knight ","Anniyan","Ghajani","Deadpool","identity","cid moosa","Kallyana raman","Spider-Man: No Way Home"]
print("List of My favorite Movies =",Fav)
print("2)")
Fav.pop(4)
print("list after removing the 5th element =",Fav)
print("3)")
Fav.insert(4,"christopher nolan")

print("List After Adding favourite movie director name at the 4th index position =",Fav)
print("4)")
print("The 4th element in the list is = ",Fav[3] )

print("5)")
Fav.append("The Pursuit of Happiness")

print("After adding additional item to the current list =", Fav)