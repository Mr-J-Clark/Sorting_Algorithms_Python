print ("sorting algorithms.... selection and bubble!")
print ("here we go")
unsorted = [23, 87, 56, 12, 78, 45, 90, 34, 67, 89, 41, 72, 54, 15, 63, 98, 22, 11, 77, 36]
sorted = []
print (f"unsorted list: {unsorted}")

while len(unsorted) > 0:
    lowest = unsorted[0]
    for value in unsorted:
        if value < lowest:
            lowest = value
    sorted.append(lowest)
    unsorted.remove(lowest)

print (sorted)









#
# #selection sort
# for j in range (len(unsorted)):
#     lowest = unsorted[0]  # always state the 1st is the lowest
#     for i in range (len(unsorted)):
#         # find lowest
#         if unsorted[i] < lowest:
#             lowest = unsorted[i]
#     unsorted.remove(lowest)  #remove the lowest value
#     sorted.append(lowest) #adding to the new list.
# print (f"the lowest is {sorted} after the 1st pass")
#


