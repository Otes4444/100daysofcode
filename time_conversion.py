# A python program for time conversion into hours,minutes and seconds.
time = float(input("Enter time in seconds: "))
hours = time / 3600
seconds = hours % 3600
minutes = time // 60
seconds = minutes % 60
print("when you input %d in seconds time, you get %dhours:%dminutes:%dseconds." % (time, hours, minutes, seconds))
