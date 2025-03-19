print("Welcome to the The Bandname Generator!")

city = input("Whats the name of the city you grew up in?\n")
pet_name = input("whats your pet's name?\n")

# string concatenation...
print("Your band name could be " + city + " " + pet_name)

# variable injection, vis-a-vis: string interpolation...
band_name = f"your band name could be, {city} {pet_name}"

print(band_name)