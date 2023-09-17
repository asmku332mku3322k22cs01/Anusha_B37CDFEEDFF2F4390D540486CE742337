"""_Implement a class called player that reprenst a cricket player.
The player class should have a method called play() which prints "The  player is playing cricket.
Derive two classes, batsman and bowler,from the player class.
override the play() method in each derived class to print "The batsman is batting" and the "The bowler is bowling", respectively
write a program to create objects of both the batsman and bowler classes and call the play() method for each object."""


#define the base class player
class player:
  def play(self):
   print("The player is playing cricket.")
    
#define the derived class batsman
class batsman(player):
  def play(self):
    print("The batsman is sitting.")

#define the derived class bowler
class bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create objects of batsman and bowler class
batsman= batsman()
bowler=bowler()

#call the play() method for each object
batsman.play()
bowler.play()





