#### IMPORTS ####
import event_manager as EM

def isValid(id, name, age, birth_year, semester):
    if type(id) is not int or id < 10000000 or id > 99999999:
        return False
    
    if type(name) is not str:
        return False
    words = name.split(" ")
    for word in words:
        if word.isalpha() == False:
            return False
    
    if type(age) is not int or age < 16 or age > 120:
        return False
    
    if type(birth_year) is not int or 2020 - age != birth_year:
        return False
    
    if type(semester) is not int or semester < 1:
        return False


def cleanName(name):
    clean_name = ''
    words = name.split(" ")
    for i,word in enumerate(words):
        if i != 0:
            clean_name += ' '
        clean_name += word
    return clean_name


# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    list=[]

    src_file = open(orig_file_path,'r')

    for line in src_file:
        id, name, age, birth_year, semester = str.split(",")
        id = id.strip()
        name = cleanName(name)
        age = age.strip()
        birth_year = birth_year.strip()
        semester = semester.strip()

        if isValid(id, name, age, birth_year, semester):
            tmp_list = [id, name, age, birth_year, semester]
            for student in list:
                if student[0] == id:
                    list.remove(student)
            list.append(tmp_list)

    src_file.close()
    list.sort()

    dest_file = open(orig_file_path,'w')

    for student in list:
        dest_file.write(student[0] + " , " +student[1] + " , " + student[2] + " , " + student[3] + " , " + student[4])
        
    dest_file.close()

# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    pass
    #TODO 3.1.2
    
    
# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    pass
    #TODO 3.1.2
    

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
