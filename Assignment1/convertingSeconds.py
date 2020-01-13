#!/bin/python3
def ConvertSeconds(seconds):
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    print(hour,'hours,',minute,'minutes,',seconds,'seconds')

ConvertSeconds(10000)
    
