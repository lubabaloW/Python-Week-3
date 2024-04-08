import csv



class Group: #CLASSES
  def __init__(self, group, week, topic, mark):
    self.group = group #OPERATORS
    self.week = week
    self.topic = topic
    self.mark = mark

print(".........................................")
group = input("Enter your group name :")
week = int(input("Enter the python learning week :"))
mark = int(input("Enter you mark for weekly presentation(1-5) :"))
topic = input("What topic are you focusing on :")

membersMarks = [] #DATA STRUCTURES
for x in range(0, 5):
  individualMark = input("Enter mark for member number " + str(x + 1) + ": ")
  membersMarks.append(individualMark)

print(".........................................")
groupDetails = Group(group, week, topic, mark) #OBJECTS

def register():
  with open("users.csv", mode="a", newline="") as f:
    writer = csv.writer(f,delimiter=",")
    email = input("Please enter email:  ")
    password = input("Please enter email:  ")
    password2 = input("Please confirm your email:  ")
  if password == password2:
      writer.writerow([email, password])
      print("Registration is successful!")
  else:
      Print("Please try again")

def login():
  email =  input("Please enter email:  ")
  password = input("Please enter your password:  ")
  with open ("user.csv", mode="r") as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
      if row ==[email, password]:
        print("You logged in!")
        return True
  print("Please try again")
  return False

register()
login()

def response(mark): #FUNCTIONS
  if mark == 5: #CONTROL FLOW
    print("Your mark is the best. Well done!")
  elif mark == 4:
    print("Your mark is great and their is room for some improvements. ")
  elif mark == 3:
    print("Your mark is good but their is still room for improvements. ")
  elif mark == 2:
    print("Your mark is below average but you got the main points across. ")
  elif mark == 1:
    print("Your mark garbage get good. ")

print("Welcome " + groupDetails.group + " you are in week " + str(groupDetails.week) + " and learning " + groupDetails.topic +".")
print("You guys scored a code " + str(groupDetails.mark) + " on your presentation.")
response(groupDetails.mark)
print(".........................................")
print("Individual Marks")
print(".........................................")

count = 0
for x in membersMarks:
  count+=1
  print("Mark for member number " + str(count) + ": Code :" + str(x) + ".")

