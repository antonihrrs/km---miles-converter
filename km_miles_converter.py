

def km_to_miles():
  ask_km = float(input("Enter Km : "))
  conv_to_miles = ask_km * 1.609
  print(f"{ask_km} Km is {conv_to_miles} miles")

def miles_to_km():
  ask_miles = float(input("Enter miles : "))
  conv_to_km = ask_miles / 1.609
  print(f"{ask_miles} miles is {conv_to_km} Km")



while True:
  ask_user = input("What do you want to convert :\nKm to miles ?\nMiles to Km ?\n").lower()
  if ask_user == "km to miles":
    km_to_miles()
    break
  elif ask_user == "miles to km":
    miles_to_km()
    break



