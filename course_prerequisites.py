def courses_to_take(course_to_prereqs):
    pass

courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']