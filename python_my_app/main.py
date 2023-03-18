import logging
import os

import pendulum

now_in_paris = pendulum.now("Europe/Paris")
print(now_in_paris)

number = input("What is your favourite number?")
print("It is", number + 1)  # error: Unsupported operand types for + ("str" and "int")
