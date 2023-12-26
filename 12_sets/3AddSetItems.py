# Use add() method to add items to set
music_genre_set = {"classical", "rock", "pop", "jazz"}
music_genre_set.add("blues")
print(music_genre_set)
print()

# To add items from another set into the current set, use the update() method
water_bodies_set = {"pond", "lake", "river"}
big_water_bodies_set = {"sea", "ocean"}
water_bodies_set.update(big_water_bodies_set)
print(water_bodies_set)
print()

# The object in update() method does not have to be a set,
# it can be any iterable object (tuples, list, dictionaries etc)
other_water_bodies_list = ["swimming pool", "hotwater spring"]
water_bodies_set.update(other_water_bodies_list)
print(water_bodies_set)
print()
