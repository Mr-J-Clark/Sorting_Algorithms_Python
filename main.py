print ("sorting algorithms.... selection and bubble!")
print ("here we go")
unsorted =  [23, 87, 56, 12, 78, 45, 90, 34, 67, 89, 41, 72, 54, 15, 63, 98, 22, 11, 77, 36]

sorted = []
print (f"unsorted list: {unsorted}")

# selection sort into new list
# while len(unsorted) > 0:
#     lowest = unsorted[0]
#     for value in unsorted:
#         if value < lowest:
#             lowest = value
#     sorted.append(lowest)unsorted = [23, 87, 56, 12, 78, 45, 90, 34, 67, 89, 41, 72, 54, 15, 63, 98, 22, 11, 77, 36]
#     unsorted.remove(lowest)
# print (sorted)

#bubble sort.
count = 0
for j in range (len(unsorted)): #looping multiple passes
    count += 1

    for i in range (len(unsorted)-1): # each pass
        if unsorted[i] > unsorted [i+1]: # if the current item is > the next
            temp = unsorted[i] #make a place-holder for the current item so we don't "lose it"
            unsorted[i] = unsorted [i+1] # the current value is replaced with the next
            unsorted [i+1] = temp # the next is overwritten with the temp (that we didn't lose)
            count += 1
        count += 1



print (unsorted)
print (f"normal bubble sort = {count}")

#bubble sort MORE EFFICIENT.

unsorted =  [23, 87, 56, 12, 78, 45, 90, 34, 67, 89, 41, 72, 54, 15, 63, 98, 22, 11, 77, 36]

print ("bubble sort MORE EFFICIENT.")
count = 0

for j in range (len(unsorted)): #looping multiple passe
    sorted = True
    count += 1
    for i in range (len(unsorted)-1): # each pass

        if unsorted[i] > unsorted [i+1]: # if the current item is > the next
            temp = unsorted[i] #make a place-holder for the current item so we don't "lose it"
            unsorted[i] = unsorted [i+1] # the current value is replaced with the next
            unsorted [i+1] = temp # the next is overwritten with the temp (that we didn't lose)
            sorted = False
            count += 1

    if sorted == True:
        break

print (f"efficient = {count}")
print (unsorted)

print (f"efficient = {count}")
print (unsorted)







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


