#defining a function:
def correctpassword(): 
  passWord = input(str("Please input your password: "))
  
  if passWord == againregisterPassword:
    print("Your account is authorised")
  else:
    print("Sorry you cannot participate since your account is not authorised")
    quit()


def passwordvalidation():
  if len(againregisterPassword) <= 6:
    print("Your password is too short. Please register again")
    quit()
  elif len(againregisterPassword) >= 20:
    print("Your password is too long. Please register again")
    quit()
  elif registerUsername == againregisterPassword:
    print("Please don't input the same username for your password")
    quit()
    
import random
import time
x = 0 

#global variable score:
score = 0

#This is a welcome message for the user
print("Welcome to the music quiz! You have to guess the name of what the song is. Good luck!")
print()
print()

print("–––––––––––Registration–––––––––––")
registerUsername = input(str("Please create a username: "))
print()
print("Please input a password that is atleast 6 characters long and does not exceed 20 characters")
print()
registerPassword = input(str("Please create a password: "))
againregisterPassword = input(str("Please re-enter password that you've created: "))


passwordvalidation()


if registerPassword == againregisterPassword:
  print()

  print("–––––––––––Login–––––––––––")
  userName = input(str("Please enter your registered username: "))

  correctpassword()

  print()
else:
  print("Your password does not match the created password")
  print()
  print("You'll have to register again")
  quit()

print()
print("–––––––––––Quiz–––––––––––")

#This is the section for guessing the song
print("When writing in the guess, make sure to write in the full name of the artist correctly, seperate the artist and song with a – and than write the name of the song")
print()
print()
print()

#opening external files
read = open("songlist.txt","r")
songs = read.readlines()
songlist = []

for i in range(len(songs)):
	songlist.append(songs[i].strip('\n')) 

while x == 0:
  choice = random.choice(songlist)
  artist, song = choice.split("-") 
  songs = song.split()
  letters = [word[0] for word in songs]
  
  for x in range(0,2): #the guess will only happen twice. If both times are wrong, the game will quit itself
    print(artist, "".join(letters))
    guess = (input("Guess the song! ")) 
    if guess == choice: 
      if x == 0:
        score = score + 3 #this allows the user to gain 3 points if they guessed correctly in the first go
        break
      if x == 1:
        score = score + 1 #this allows the user to gain 3 points if they guessed correctly in the second go
        break
  
  print("Your current score is ", score) #this will print the updated score
  print()
  time.sleep(2) #allow to take 2 second break before something else appears
  

#creating a leaderboard:
leaderboard = open("leaderboard.txt", "r+")
leaderboard.write(userName + ' - ' + '{}'.format(score))
leaderboard = open("leaderboard.txt", "r+")
leaderboardlist = leaderboard.readlines()
print(leaderboardlist)
leaderboard.close()
