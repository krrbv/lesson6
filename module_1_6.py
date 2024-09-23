my_dict = {"Name": "Kristina", "Year of birth": 2002, "Phone number": 88005553535}
print(my_dict)
print(my_dict["Name"])
print(my_dict.get("Address"))
my_dict.update({"Country": "Russia",
                "City": "Saint Petersburg"})
print(my_dict)
a = my_dict.pop("Year of birth")
print(a)
print(my_dict)

my_set = {1, 2, 4, 4, 55, 55, "School", "apple", "apple", (7, 89, 69)}
print(my_set)
my_set.add(9)
my_set.add("banana")
my_set.discard((7, 89, 69))
print(my_set)