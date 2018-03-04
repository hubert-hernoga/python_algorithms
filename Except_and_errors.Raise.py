heroes = ["Harry", "Ron", "Hermione"]

def get_heroes(x):
  try:
      index = int(x)
      return(heroes[index])

  except IndexError:
      raise ValueError("argument jest za duży!")


#print(get_heroes("aaa"))

try:
    print(get_heroes(6))
except ValueError as e:
    print(type(e), str(e))

#print(get_heroes({}))
