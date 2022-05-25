# Dictionaries have pairs in KEY : VALUE
# Key is unique
# Data don't ordered

person = {
    "Name": "Ford Prefect",
    "Gender": "Male",
    "Occupation": "Researcher",
    "Home planet": "Betelgeuse Seven"
}

print(person)  # {'Name': 'Ford Prefect', 'Gender': 'Male', 'Occupation': 'Researcher', 'Home planet': 'Betelgeuse Seven'}

print(person["Name"])  # Ford Prefect

person["Age"] = 33  # add key - Age with value - 33

print(person)  # {'Name': 'Ford Prefect', 'Gender': 'Male', 'Occupation': 'Researcher', 'Home planet': 'Betelgeuse Seven', 'Age': 33}


# KEYS IN DICTIONARIES MUST BE INITIALISED
# WHEN KEY IS NOT INIT - KEYERROR

# to init key you can use if/not in
print(person)  # {'Name': 'Ford Prefect', 'Gender': 'Male', 'Occupation': 'Researcher', 'Home planet': 'Betelgeuse Seven', 'Age': 33}
if "City" not in person:
    person["City"] = "Moscow"

print(person)  # {'Name': 'Ford Prefect', 'Gender': 'Male', 'Occupation': 'Researcher', 'Home planet': 'Betelgeuse Seven', 'Age': 33, 'City': 'Moscow'}

# or use method -setdefault()
print(person)  # {'Name': 'Ford Prefect', 'Gender': 'Male', 'Occupation': 'Researcher', 'Home planet': 'Betelgeuse Seven', 'Age': 33, 'City': 'Moscow'}
person.setdefault("Country", "Russia")
print(person)  # {'Name': 'Ford Prefect', 'Gender': 'Male', 'Occupation': 'Researcher', 'Home planet': 'Betelgeuse Seven', 'Age': 33, 'City': 'Moscow', 'Country': 'Russia'}