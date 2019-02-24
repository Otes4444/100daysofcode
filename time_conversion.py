# A python program for time conversion into hours,minutes and seconds.
time = int(input("Enter time in seconds: "))
hours = time // 3600
seconds = time % 3600
minutes = seconds // 60
seconds = seconds % 60
print("when you input %d in seconds time, you get %dhours:%dminutes:%dseconds." % ( time, hours, minutes, seconds))
