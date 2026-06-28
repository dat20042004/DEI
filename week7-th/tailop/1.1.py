# Thực hành 1.1:
# Array List

thislist = ["hanoi", "saigon", "danang", "nhatrang", "cantho"]
print(thislist)

thislist.insert(2, "cantho")     # insert
print(thislist)
thislist.insert(3, "Hue")
print(thislist)

thislist = ["hanoi", "saigon", "danang", "nhatrang"]
thislist.pop(2)                  # pop

thislist = ["hanoi", "saigon", "danang", "nhatrang", "cantho"]
thislist.sort()
print(thislist)

thislist = [100, 15, 50, 65, 82, 23]
thislist.sort()                  # sort
print(thislist)

list1 = ['data analytics', 'data science', 'data structures and algorithms', 2020, 2021]
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("list1[1]: ", list1[1])
print("list2[2:8]: ", list2[2:8])
