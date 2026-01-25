# ============================================
# Chapter 5: Madlibs Game
# ============================================

# %%
#TODO: User Input - We ask the user for different types of words
adjective1 = input("enter an adjective (description): ")
noun1 = input("enter a noun (person, animal, thing): ")
adjective2 = input("enter another adjective (description): ")
verb1 = input("enter a verb ending with 'ing' (current tense): ")
adjective3 = input("enter a third adjective (description): ")

#TODO: Story Template - We create a story using the user's words
# - use (f-strings) to insert the user's words into our story
print(f"today i went to a {adjective1} zoo.")
print(f"in an exhibit, i saw {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

# %%

#NOTE: 
# (f-strings) are a way to format strings in Python by embedding expressions inside string literals, using curly braces {}.
# They are prefixed with the letter 'f' or 'F' before the opening quotation mark.
