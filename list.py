#Making a list
users = ['val', 'bob', 'mia', 'ron', 'ned' ]
first_user = users[0]
second_user = users[1]
newest_user = users[-1]

print(f'The second user is' +  users[1])
users[0] = 'valerie'
users[-2] = 'ronald'
print('Our users are' + str(users))

#Starting with an empty list
users_1 = []
users_1.append("val")
print(users_1)
users_1.append("bob")
users_1.append("mia")
print(users_1)
users_1.insert(0, 'joe')
users_1.insert(3, 'bea')
print(users_1)

#Removing elements
del users_1[-1]
print(users_1)
users_1.remove("val")
print(users_1)

#POP
most_recent_user = users_1.pop(0)
#print(most_recent_user) ეს ნაწილი ცოტა გაუგებარია

first_user = users.pop(0)
print(first_user)

#List lenghts
num_users = len(users)
print ("We have" + str(num_users) + " users.")

#Sorting
users.sort()
users.sort(reverse=True)
print(sorted(users))
print(sorted(users, reverse=True))
users.reverse()
#აქ დამატებითად რაღაც ნიშნის მიხედვით სორტირება შეიძლება?

#Looping
for user in users:
    print(user)

for user in users:
    print("Welcome," + user + "!")
print("Welcome, we're glad to see you all!")


#RANGE
#for number in range(1001):
    #print(number)

#for number in range(1, 1001):
    #print(number)


#Statistics
numbers = list(range(1, 100))

ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)
print(youngest, oldest, total_years)

finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
first_three = finishers[:3]
middle_three = finishers[1:4]
last_three = finishers[-3:]
print(first_three, last_three)

#Copying
copy_of_finishers = finishers[:]
print(copy_of_finishers)

squares = []
for x in range(1, 11):
    square = x**2
    squares.append(square)
    #ეს კოდი შლის step-ებად?
    print(squares)

squares_1 = [x**2 for x in range(1, 11)]
print(squares_1)

names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)

#TUPLES
dimensions = (800, 600)
for dimension in dimensions:
    print(dimension)
print(dimensions)

#Visualising
dogs = []
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')

for dog in dogs:
    print('Hello ' + dog + '!')
print('I love these dogs')

print("\nThese were my first two dogs")
old_dogs = dogs[:2]
for old_dog in old_dogs:
    print(old_dog)

del dogs[0]
dogs.remove('peso')
print(dogs)
