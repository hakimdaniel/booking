import os
from os import system as s
import platform

c = "clear" if os.name == "posix" else "cls"

menu = '''
Program (hakim)

1. choose room
2. show availability
3. book now
4. cancel
'''
# availability

room = { "Makmal 2.7": True, "Makmal 1.2": True, "Meeting room": False, "Library": True, "TV room": False, "Surau": True, "Big Hall": False }

def show():
	x = list(room.keys())
	for i in x:
		print(f"- {i} ({'Available' if room[i] else 'Not Available'})")

print("Booking Classroom Stasab")

def main():
  choosed = []

  def clearBook():
      if choosed:
          for i in choosed:
              room[i] = True
          choosed.clear()
          print("Your choice was canceled.")
      else:
          print("Nothing to cancel here.")
      show()

  while True:
      print(menu)
      chs = int(input(">> "))
    
      if chs == 1:
          s(c)
          print("Choose room")
          show()
          book = input("Name room: ")
        
          if book in room:
              if len(choosed) >= 2:
                  print("Book more room in another session")
              else:
                  if room[book]:  
                      room[book] = False
                      choosed.append(book)
                      print(f"Book ({book}) successful!")
                      print(f"{book} chosen by you")
                  else:
                      print("Room not Available right now, choose another room to book!")
          else:
              print("No room with your input")
            
      elif chs == 2:
          s(c)
          show()
      elif chs == 3:
          s(c)
          print("Your booking information saved in system.")
      elif chs == 4:
          s(c)
          clearBook()
      else:
          s(c)
          continue

if __name__ == "__main__":
	main()
