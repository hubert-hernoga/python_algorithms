heroes = ["Harry", "Ron", "Hermione"]

while True:
  try:
      x = input("Wprowadz index: ")
      index = int(x)
      print(heroes[index])
      break

  except ValueError:
      print("Ups! To nie jest liczba, spróbuj ponownie.")

  #except IndexError:
    #print("W tablicy heroes nie ma elementu o tym indeksie!")

#Ostatni kod printuje Nam błąd mówiący o tym, że nie ma takiego indeksu w tablicy
