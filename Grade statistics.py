# Grade table 

fail  = range(0,15)
one   = range(15,18)
two   = range(18,21)
three = range(21,24)
four  = range(24,28)
five  = range(28,31)

# Empty variables for grade distrubution

fail_grade  = ""
one_grade   = ""
two_grade   = ""
three_grade = ""
four_grade  = ""
five_grade  = ""


input_counter = 0
fail_counter  = 0
points_sum    = 0

while True:
    points_input = (input("Exam points and exercises completed:"))
    
    if points_input == "" and input_counter > 0:
            points_average = points_sum / input_counter 
            pass_percentage = ((input_counter - fail_counter )/ input_counter) * 100

            statistic = f"Statistic: \nPoints average: {points_average} \nPass percentage: {pass_percentage}"  
            grade_distrubution = f"Grade distribution: \n 5:{five_grade} \n 4:{four_grade} \n 3:{three_grade} \n 2:{two_grade} \n 1:{one_grade} \n 0:{fail_grade} "
        
            print(statistic)
            print(grade_distrubution)
            break
    
    # Check if user enter no data

    if points_input == "":
        print("There is no data")
        break
    
    # Check if user enter only exams points or dont enter numberof completed exercises

    points_list_check = points_input.split(" ")
    if len(points_list_check) < 2 or points_list_check[1] == "":
        print("Please type in exams point and completed exercises")
        continue
    
    points_list = list(map(int, points_input.split(" ")))
    


    # Check if user enter real data

    if points_list[0] > 20 or  points_list[0] < 0:
        print("Please type your real exam points")
        continue
    if points_list[1] > 100 or  points_list[1] < 0:
        print("Please type your real completed exercises")
        continue
    
    
    # Update number of students

    input_counter += 1
    
    percentage = points_list[1] // 10
    exam = points_list[0]
    grade = (exam + percentage)
    points_sum += grade

    # Update students grade

    if grade in fail or exam < 10:
        fail_grade += "*"
        fail_counter += 1

    elif grade in one:
        one_grade += "*"
    
    elif grade in two:
        two_grade += "*"
    
    elif grade in three:
        three_grade += "*"
    
    elif grade in four:
        four_grade += "*"
    
    elif grade in five:
        five_grade += "*"