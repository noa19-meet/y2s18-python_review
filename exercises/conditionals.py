# Write your solution for 1.2 here!
large=0
for i in range (1001):
    if i%6==2:
        if i**3%5==3:
            if i>large:
                large=i
print (large)

