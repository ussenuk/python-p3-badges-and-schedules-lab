def badge_maker(name):
    name_of_person = f'Hello, my name is {name}.'
    return name_of_person

def batch_badge_creator(names):
    list_name = []
    for name in names:
        list_name.append(f'Hello, my name is {name}.')
        # print (list_name)
    return list_name

# using enumerate 
# def assign_rooms(names):
#     list_name =[]
#     rooms = [1,2,3,4,5,6,7,8]
#     if len(names) > len(rooms):
#             return "There is no enough room for the users"
#     for index, name in enumerate(names):
#         list_name.append(f"Hello, {name}! You'll be assigned to room {rooms[index]}!") 
#     return list_name

# using the for loop
def assign_rooms(names):
    list_name =[]
    rooms = [1,2,3,4,5,6,7,8]
    for i in range(len(names)):
        if i < len(rooms):
              list_name.append(f"Hello, {names[i]}! You'll be assigned to room {rooms[i]}!")
        else:
             return "There are no enough rooms for the users"
    return list_name
              

# # using while 
# def assign_rooms(names):
#     list_name = []
#     rooms = [1,2,3,4,5,6,7,8]
#     i = 0
#     while i < len(names):
#         if i < len(rooms):
#             list_name.append(f'Hello, {names[i]}! You\'ll be assigned to room {rooms[i]}!')
#             i += 1
#         else:
#             return "There are not enough rooms for all speakers."
#     return list_name

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assignment in assign_rooms(names):
        print(assignment)
