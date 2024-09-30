#!/usr/bin/env python3
import threading

def print_out_name():
    print("Name: Kyle")
    print("Student Number: 2226771")
threading.Thread(target=print_out_name).start()
# 30/09/2024
# Create a thread to print out name and student number.py
# 30/09/2024
# Kyle Pendleton
# This will create a thread to print out my name and student number