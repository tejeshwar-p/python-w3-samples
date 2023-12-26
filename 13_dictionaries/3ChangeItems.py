# Change the value of a specific item by referring to its key name
mango_dict = {
    "generic name": "Mango",
    "scientific name": "Mangifera Indica",
    "color": "green"
}
print(mango_dict)  # Before
mango_dict["color"] = "red"
print(mango_dict)  # After
print()

# The update() method will update the dictionary with the items from the given argument
mango_dict.update({"color": "yellow"})
print(mango_dict)
print()


