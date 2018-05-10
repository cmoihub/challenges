# def analyze(N, P, Q):
#     """
#         i is a position in N, P & Q are integers, 
#         If N[i] is divisible by P then print "OUT", 
#         and if N[i] is divisible by Q then print "THINK"; 
#         if N[i] is divisible by both P and Q then concatenate OUT and THINK 
#         (hence, OUTTHINK), and if N[i] isn't divisible by any of P and Q 
#         then print the number in that index.
#     """
#     P_ = "out"
#     Q_ = "think"
#     for i in N:
#         value = ""
#         if (i % P) is 0:
#             value += P_
#         if (i % Q) is 0:
#             value += Q_
#         if (value != ""):
#             print (value)
#         else:
#             print(i)

# N = list(range(1,100))
# analyze(N, 3, 5)
# print()

# def compare_strings(first, second):
#     first_as_an_array = first.split(",")
#     second_as_an_array = second.split(",")
#     for i in second_as_an_array:
#         if i in first_as_an_array:
#             print(i)

# first = "obi,tobi,craig,ese"
# second = "obi,tobi"
# compare_strings(first, second)
# print()

# def fruit (inventory):
#     datawise = {}
#     print (datawise)
#     # pass

# apples = ['Apples sold on the farm', '214 out of 250 on April 1', '179 out of 250 on April 2', '230 out of 250 on April 3']
# oranges = ['Oranges sold on the farm', '0 out of 200 on April 1', '180 out of 250 on April 2', '200 out of 250 on April 3']
# mango = ['Mango sold on the farm', '100 out of 100 on April 1', '0 out of 200 on April 2', '50 out of 250 on April 3']
# inventory = [apples, oranges, mango]
# fruit(inventory)
# print()

# def add_up(array, target):
#     array = set(array)
#     array = list(array)
#     array = recursive_finder(array, target, [])
#     print(array)

# def recursive_finder(array, target, double_numbers):
#     """
#     fixed size array is given, target is 9, 
#     find 2 numbers of the array that add up to it
#     """
#     if len(array) is 0:
#         return double_numbers
#     focus = array.pop()
#     for i in array:
#         if (i + focus) is target:
#             double_numbers.append([focus, i])
#             array.remove(i)
#         else:
#             continue
#     recursive_finder(array, target, double_numbers)
#     return double_numbers

# array = [1,2,3,3,4,5,6,7,8, -1, 10, 9, 6,6 ]
# target = 9
# add_up(array, target)

# import sys

# def challenge2(line, count):
#     match = ""
#     count -= 1
#     if count is 0:
#         return match
#     lines = line.split("/n")
#     # return line
    
    
    
    
#     # return match

# for line in sys.stdin:
#     print(challenge2(line, 3))



import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip("\n"))
lines.pop()

"yyyy-mm-dd,total,item---"

def inventory(lines):
    """
        Format - date, total items sold for date, average quantity of all items 
        (to 2 decimal places), count of unique parts sold
        
    """
    data = []
    for array in lines:
        data.append(array.split(","))
    
    unique_dates = []
    for array in data:
        unique_dates.append(array[0])
    unique_dates = set(unique_dates)
    unique_dates = list(unique_dates)

    i = 0
    final = []
    last = analyze(i, data, unique_dates, final)
    
    print (last)

def analyze(i, data, dates, final):
    if (i >= len(dates)-1):
        return final
    date = dates[i]
    
    for array in data:
        if array[0] == date:
            final.append(array)
            
    i+=1
    print(i)
    analyze(i, data, dates, final)
        
inventory(lines)
    