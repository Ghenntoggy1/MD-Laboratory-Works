# 1. Courses
def paircourses(a, b):
    adjac[a].append(b)


total_courses = int(input("Input number of courses: "))
adjac = []
for c in range(total_courses):
    adjac.append([])
# print(adjac)

number_pairs = int(input('Input number of prerequisites: '))

for np in range(number_pairs):
    print("PAIR", np + 1, ':')
    course_wanted = int(input(f'Input wanted course(between 0 and {total_courses - 1}): '))
    course_needed = int(input(f'Input needed course(between 0 and {total_courses - 1}): '))
    paircourses(course_wanted, course_needed)
# print(adjac)

indegrees = []
for c in range(total_courses):
    indegrees.append(0)
# print(indegrees)

for c in range(total_courses):
    for adj_el in adjac[c]:
        indegrees[adj_el] += 1
# print(indegrees)

storage = []
for c in range(total_courses):
    if indegrees[c] == 0:
        storage.append(c)
# print(storage)

counter = 0
while storage:
    p = storage.pop(0)
    counter += 1
    for adj_el in adjac[p]:
        indegrees[adj_el] -= 1
        if indegrees[adj_el] == 0:
            storage.append(adj_el)
if counter != total_courses:
    print("CAN NOT FINISH ALL COURSES :(")
else:
    print('CAN FINISH ALL COURSES :)')






# while flag:
#     course_wanted = int(input('Input wanted course: '))
#     course_needed = int(input('Input needed course: '))
#     paircourses(course_wanted, course_needed)
#     user = input("Continue? Y/N \n")
#     if user == 'Y':
#         user = True
#     else:
#         user = False
#     flag = user