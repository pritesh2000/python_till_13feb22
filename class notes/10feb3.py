# Organizing your code in Modules & Packages
# Mummy = import
# papa = pip install
"""
import important_functions

print(important_functions.factorial(6))
"""
"""
import important_functions as imp
import numpy as np
# import pandas as pd
import speech_recognition as sr

print(imp.avg(5,10,12))
"""
"""
from important_functions import factorial as fc, avg

fc(5)
avg(10,12)
"""
"""
from important_functions import *

print(perfectCheck(28))
print(__name__)
"""
"""
import random as rd

# random.randint(1, 100)
rd.randint(1, 100)
"""
"""
from random import randint

randint(1, 100)
"""

# Creating our own package
# import myPackage      This does  not work

# import myPackage.important_functions as imp
# or
# from myPackage.important_functions import factorial as fact

# from myPackage.subPackage import recursive_function as rf

# from myPackage.subPackage.recursive_function import recursive_factorial as rf

# Tomorrow's Class: OOP in Python, Exception Handling, File Handling