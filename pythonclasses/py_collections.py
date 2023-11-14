# lists
# dictionary
# set
# tuple

cities = ["Nairobi", "Kigali", "Kinshasa", "Kisumu"]
scores = [56, 6, 45, 5, 45, 645, 7, 465, 7, 576, 5, 75, 76, 75,]

car = {
    "make": "Toyota",
    "model": "Probox",
    "year": 2017,
    "gear": "Manual",
    "color": "White",
    "owners":["Jane", "Cosmas","Miry"]
}
friends = {"Mike", "Karoo", "Kiprotich"} # removes duplicates

workers = ("Jane", "Jack", "Jim") # tuples can never be change programmatically



for key, value in car.items():
    print(key, value)
