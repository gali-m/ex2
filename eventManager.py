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
    if not isinstance(id,int) or len(str(id)) != 8:
        return False
    
    # name checks
    words = name.split(" ")
    for word in words:
        if word.isalpha() == False:
            return False
    
    # age checks
    if not isinstance(age,int) or age < 16 or age > 120:
        return False
    
    # birth year checks
    if not isinstance(birth_year,int) or 2020 - age != birth_year:
        return False
    
    # semester checks
    if not isinstance(semester,int) or semester < 1:
        return False

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
    list=[]

    src_file = open(orig_file_path,'r')

    for line in src_file:
        # get this submission values
        id, name, age, birth_year, semester = line.split(",")
        id = int(id.strip())
        name = cleanName(name)
        age = age.strip()
        birth_year = birth_year.strip()
        semester = semester.strip()

        if isValid(id, name, age, birth_year, semester):
            tmp_list = [id, name, age, birth_year, semester]

            # check if there is already a submission with this id
            for student in list:
                if student[0] == id:
                    # remove previous student submission
                    list.remove(student)

            # add the latest submission to the list
            list.append(tmp_list)

    src_file.close()
    # sort by id
    list.sort()

    dest_file = open(orig_file_path,'w')
    # write the list to the output file
    for student in list:
        dest_file.write(" ,".join([student[0], +student[1], student[2], student[3], student[4]]))
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

    temp_file = "temp_file.txt"
    all_students = [] 

    fileCorrect(in_file_path, temp_file)

    tmp_f = open(temp_file, "w")

    for line in tmp_f:
        id, name, age, year, semester = line.split(" ,")
        all_students.append([age, id, name, year, semester])

    tmp_f.close()

    return all_students

# print the youngest students from list to file 
# order by the age and if equal age by id
#   out_file_path: file path of the output file
#   num_student_print: num of students to print
#   all_students: list of all students in order [[age, id, name, year, semester],[age, id, name, year, semester],..]
def printYoungestStudentsToFile(out_file_path, num_student_print, all_students):

    f = open(out_file_path, "r")

    for i in range(num_student_print):
        id = all_students[i][1]
        name = all_students[i][2]
        age = all_students[i][0]
        year = all_students[i][3]
        semester = all_students[i][4]

        new_line = " ,".join([id, name, age, year, semester])
        new_line += "\n"

        f.write(new_line)   

    f.close()

# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    pass
    #TODO 3.1.2

    if k < 0:
        return -1

    all_students = allStudentsList(in_file_path)

    all_students.sort()

    num_student_print = max(all_students, k)

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

    if semester > 1:
        return -1

    all_students = allStudentsList(in_file_path)

    return getAgeAvgFromList(all_students, semester)


    
#### PART 2 ####
# Use SWIG :)

#TODO 3.2.1 is creating the interface file eventManager.i

# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    pass
    #TODO 3.2.2
    
    
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
