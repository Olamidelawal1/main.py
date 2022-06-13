
from tkinter import scrolledtext
import traceback
from unicodedata import name


class Student:
      # [assignment] Skeleton class. Add your code here
      
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score =score
#classmethod
    def change_name(self,name):
        def change_age(self,age):
            def add_track(self,track):
                def get_score(self,score):
                    
                    self.name = name
                return self.name

            self.age = age
            return self.age

            self.track = track
            return self.track

            self.score = score
            return self.score

Bob = Student("Bob", int(26) , ["FE", "BE"], 20.90)
print("The name is " +Bob.name) 
print("The age is " +str(Bob.age))
print("The track is " +str(Bob.track))
print("The score is " +str(Bob.score))

Bob.change_name =("Peter")
Bob.change_age =(34)
Bob.add_track =("FE", "BE", "UI/UX")
Bob.get_score =(20.90)

print ("The new name is " +str(Bob.change_name))
print ("The new age is " +str(Bob.change_age))
print ("The new track is " +str(Bob.add_track))
print ("The new score is " +str(Bob.get_score))
