import random
while(True):
 temp=random.randint(10,99)
 humid=random.randint(10,99)

 print("current temperature:",temp)
 print("current humidity:", humid, "%")
 temp_ref=37
 humid_ref=35
 if temp>temp_ref and humid<humid_ref:
  print("Sound Alarm")
 else:
  print ("Sound off")
 break
