courses = ['History', 'Math', 'Physics']
courses_2 = ['Arts', 'Bio']

courses.extend(courses_2) # Extend is used to add items into list from another list 

print(courses)
print(courses_2)

for index,course in enumerate(courses,start=1): #enumerate is usefule for obtaining index of items in the list
    print(index,course)


course_str = ','.join(courses) #list-> comma seperated items
new_list = course_str.split(',')  #coma seperated items -> list
print(course_str)
print(new_list)