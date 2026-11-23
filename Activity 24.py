# List
fruits = ["longgan", "lipute", "tyesa", "kaldito",
          "santol", "atis", "mabolo", "pili"]

# Dictionary
fruits_d = {
    "bilog": "longgan",
    "maasim": "lipute",
    "kadiri": "tyesa",
    "libre": "kaldito",
    "kinatas": "santol",
    "nabuhangin": "atis",
    "mabuhok": "mabolo",
    "okay lng siya": "pili"
}

# Accessing a list
print(fruits[7])

# Accessing a dictionary
print(fruits_d["okay lng siya"])

# Traversing a dictionary
for x, y in fruits_d.items():
    print("key is", x, "-- value is", y)