#!/usr/bin/python

#pin1 --> start pin
#pin2 --> auxiliary pin
#pin3 --> destination pin

def move(pin1,pin3):
  print("{}->{}".format(pin1,pin3))

def hanoi(n,pin1,pin2,pin3):
    if n==0:
      pass
    else:
      hanoi(n-1,pin1,pin3,pin2)
      move(pin1,pin3)
      hanoi(n-1,pin2,pin1,pin3)

quantPin = int(input("How many disks do you want to solve?"))
hanoi(quantPin,1,2,3)
