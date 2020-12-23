#### IMPORTS ####
import event_manager as EM

# gets submission values and checks if they are valid
#   id: student's id
#   name: student's name
#   age: student's age
#   birth_year: student's birth year
#   semester: student's semester
# 
# return - True if all parameters are valid,
#          False otherwise
def isValid(id, name, age, birth_year, semester):
    # id checks
    if id.startswith("0") or len(id) != 8:
        return False
    
    # name checks
    words = name.split(" ")
    for word in words:
        if word.isalpha() == False:
            return False
    
    # age checks
    if int(age) < 16 or int(age) > 120:
        return False
    
    # birth year checks
    if 2020 - int(age) != int(birth_year):
        return False
    
    # semester checks
    if int(semester) < 1:
        return False

    return True

# gets a name and returns the name with only one space between each word
#   name: student's name
# 
# return - the cleaned name
def cleanName(name):
    words = name.split(" ")
    return ' '.join(filter(str.split,words))


# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    students_list=[]

    src_file = open(orig_file_path,'r')

    for line in src_file:
        # get this submission values
        id, name, age, birth_year, semester = line.split(",")
        id = id.strip()
        name = cleanName(name)
        age = age.strip()
        birth_year = birth_year.strip()
        semester = semester.strip()

        if isValid(id, name, age, birth_year, semester):
            tmp_list = [id, name, age, birth_year, semester]

            # check if there is already a submission with this id
            for student in students_list:
                if student[0] == id:
                    # remove previous student submission
                    students_list.remove(student)

            # add the latest submission to the list
            students_list.append(tmp_list)

    src_file.close()
    # sort by id
    students_list.sort()

    dest_file = open(filtered_file_path,'w')
    # write the list to the output file
    for student in students_list:
        dest_file.write(", ".join([student[0], student[1], student[2], student[3], student[4]]))
        dest_file.write("\n")
        
    dest_file.close()


# get correct file of the input file
# and put all parameters's student in list
# and append is to all_student list 
#   in_file_path: The path to the unfiltered subscription file
# 
# return - list of all students
# like [[age, id, name, year, semester],[age, id, name, year, semester],..]
def allStudentsList(in_file_path):

    # import pdb; pdb.set_trace()

    temp_file = "temp_file.txt"
    all_students = [] 

    fileCorrect(in_file_path, temp_file)

    tmp_f = open(temp_file, "r")

    for line in tmp_f:
        id, name, age, year, semester = line.split(", ")
        all_students.append([int(age), int(id), name, int(year), int(semester.strip())])

    tmp_f.close()

    return all_students

# print the youngest students from list to file 
# order by the age and if equal age by id
#   out_file_path: file path of the output file
#   num_student_print: num of students to print
#   all_students: list of all students in order [[age, id, name, year, semester],[age, id, name, year, semester],..]
def printYoungestStudentsToFile(out_file_path, num_student_print, all_students):

    f = open(out_file_path, "w")

    for i in range(num_student_print):

        new_line = all_students[i][2] + "\n"

        f.write(new_line)

    f.close()

# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    pass
    #TODO 3.1.2

    if k <= 0:
        return -1

    all_students = allStudentsList(in_file_path)

    all_students.sort()

    num_student_print = min(len(all_students), k)

    printYoungestStudentsToFile(out_file_path, num_student_print, all_students)

    return num_student_print


# get the age avg of students in semester from list of students 
# 
#   all_students: list of all students in order [[age, id, name, year, semester],[age, id, name, year, semester],..]
#   semester: the semester to check on
def getAgeAvgFromList(all_students, semester):

    age_sum = 0
    num_student_in_semester = 0

    for student in all_students:
        if student[4] == semester:
            num_student_in_semester += 1
            age_sum += student[0]

    if num_student_in_semester == 0:
        return 0

    return age_sum / num_student_in_semester

    
# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    pass
    #TODO 3.1.2

    if semester < 1:
        return -1

    all_students = allStudentsList(in_file_path)

    return getAgeAvgFromList(all_students, semester)


    
#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    #  find the earliesst date
    min_date = events[0]["date"]

    for event in events:
        if EM.dateCompare(event["date"], min_date) < 0:
            min_date = event["date"]
    
    em = EM.createEventManager(min_date)
    for event in events:
        result = emAddEventByDate(em, event["name"], event["date"], event["id"])
        # if result != EM_RESULT:
        #     EM.destroyEventManager(em)
        #     return NULL
    
    EM.emPrintAllEvents(em, file_path)
    return em
    
def testPrintEventsList(file_path :str):
    events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
                    {"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
                                 {"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
                                     {"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
    em = printEventsList(events_lists,file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)

#### Main #### 
# feel free to add more tests and change that section. 
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        testPrintEventsList(sys.argv[1])
    print("pass")