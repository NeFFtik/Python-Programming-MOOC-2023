# def largest_number():
#     with open("numbers.txt") as new_file:
#         number_list = []
#         for number in new_file:
#             number = number.replace("\n", "")
#             number_list.append(int(number))
    
#     return (max(number_list))

# print(largest_number())

# def read_fruits():
#     with open("fruits.csv") as new_file:
#         fruits = {}
#         for fruit in new_file:
#             fruit = fruit.replace("\n", "")
#             items = fruit.split(";")
#             name_of_fruit = items[0]
#             price_of_fruit = items[1]
#             fruits[name_of_fruit] = price_of_fruit
#         return fruits
    
# print(read_fruits())

# def matrix_sum():
#     items = []
#     with open("matrix.txt") as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             numbers = line.split(",")
            
#             for item in numbers:
#                 items.append(int(item))

#     return sum(items)
    



# def matrix_max():
#     items = []
#     with open("matrix.txt") as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             numbers = line.split(",")
            
#             for item in numbers:
#                 items.append(int(item))

#     return max(items)


# def row_sums():
#     list_of_items = []
    
#     with open("matrix.txt") as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             numbers = line.split(",")
#             items = []

#             for item in numbers:
#                 items.append(int(item))
#                 rows = []

#                 if len(items) == len(numbers):
#                     list_of_items += [items]
                     
#                     for row in range(len(list_of_items)):
#                         rows += [sum(list_of_items[row])]
                
#     return(rows)
    
# print(matrix_sum())
# print(matrix_max())
# print(row_sums())


# student_info = input("Student information: ")
# exercise_data = input("Exercises completed: ")
# exam_points = input("Exam points: ")
# items = {}

# with open (student_info) as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         names = line.split(";")
#         id = names[0]
#         name = names[1]
#         surname = names[2]
#         items[id] = (f"{name} {surname}")

# exercises = {}

# with open (exercise_data) as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         completed_exercises = line.split(";")
#         if completed_exercises[0] == "id":
#             continue
#         id = completed_exercises[0]
#         exercises[id] = completed_exercises[1:]


# exams_points = {}
# with open (exam_points) as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         exams = line.split(";")
#         if exams[0] == "id":
#             continue
#         id = exams[0]
#         exams_points[id] = exams[1:]



# exercises_points = {}
# grade = {}

# grade_ranges =[
#     (range(0,15), 0),
#     (range(15,18), 1),
#     (range(18,21), 2),
#     (range(21,24), 3),
#     (range(24,28), 4),
#     (range(28,100), 5)
# ]
# print(f"{"name":30} {"exec_nbr.":10} {"exec_pts.":10} {"exam_pts.":10} {"tot_pts.":10} grade")

# for id, name in items.items():
#     if id in exercises and id in exams_points:
#         exercises_points[id] = ((sum(int(number) for number in exercises[id])* 10) // 40) 
#         grade[id] = exercises_points[id] + (sum(int(number) for number in exams_points[id]))

#         exec_nbr = (sum(int(number) for number in exercises[id]))
#         exec_pts = exercises_points[id]
#         exm_pts = grade[id] - exercises_points[id] 
#         total_points = exec_pts + exm_pts


#         def get_grade(total_points):
#             for points_range, result in grade_ranges:
#                 if total_points in points_range:
#                     return result
                
#         final_grade = get_grade(total_points)
#         print(f"{name:30} {exec_nbr:<10} {exec_pts:<10} {exm_pts:<10} {grade[id]:<10} {final_grade}")
        
# words = []       
# with open ("wordlist.txt") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         line = line.lower()
#         words.append(line.strip())

# sentence = input("Write text: ")
# sentence_words = []
# word = sentence.split(" ")
# sentence_words.append(word)

# result = []
# for word in range(len(sentence_words[0])):
#     if sentence_words[0][word].lower() in words:
#         result.append(sentence_words[0][word])
#     elif sentence_words[0][word] not in words:
#         result.append("*" + sentence_words[0][word] + "*")



# print(" ".join(result))

# def search_by_name(filename: str, word: str):
#     items = []
#     recipes = {}
#     number_of_recipes = 1
#     recipes[number_of_recipes] = []

#     with open(filename) as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             line = line.strip()
#             items.append([line])
#         for item in range(len(items)):
#                 recipes[number_of_recipes] += items[item]
#                 if items[item] == [""]:
#                     number_of_recipes += 1
#                     recipes[number_of_recipes] = []
#     founded = []
#     for recipe in range(1, len(recipes) + 1):
      
#       for ingredient in range(len(recipes[recipe])):
#             if word in recipes[recipe][ingredient]:
#                 founded.append(recipes[recipe][0])
#             continue

#     return founded


# def search_by_time(filename: str, prep_time: int):
#     items = []
#     recipes = {}
#     number_of_recipes = 1
#     recipes[number_of_recipes] = []

#     with open(filename) as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             line = line.strip()
#             items.append([line])
#         for item in range(len(items)):
#                 recipes[number_of_recipes] += items[item]
#                 if items[item] == [""]:
#                     number_of_recipes += 1
#                     recipes[number_of_recipes] = []
#     founded = {}
    
#     for recipe in range(1, len(recipes) + 1):
#             recipe_time = int(recipes[recipe][1])
#             if prep_time >= recipe_time:
#                 name = recipes[recipe][0]
                
#                 founded[name] = []
#                 founded[name] = int(recipes[recipe][1])
#     return_values = []
#     for recipe in founded:
#         return_values.append(f"{recipe}, preparation time {founded[recipe]} min")
    
#     return return_values


# def search_by_ingredient(filename: str, ingredient: str):
#     items = []
#     recipes = {}
#     number_of_recipes = 1
#     recipes[number_of_recipes] = []

#     with open(filename) as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             line = line.strip()
#             items.append([line])
#         for item in range(len(items)):
#                 recipes[number_of_recipes] += items[item]
#                 if items[item] == [""]:
#                     number_of_recipes += 1
#                     recipes[number_of_recipes] = []
#     founded = {}
#     for recipe in range(1, len(recipes) + 1):
      
#       for materials in range(len(recipes[recipe])):
#             if ingredient in recipes[recipe][materials]:
#                 name = recipes[recipe][0]
#                 founded[name] = []
#                 founded[name] = int(recipes[recipe][1])
#             continue
#     return_values = []
#     for recipe in founded:
#         return_values.append(f"{recipe}, preparation time {founded[recipe]} min")

#     return return_values



# found_recipes = search_by_ingredient("recipes1.txt", "salt")

# for recipe in found_recipes:
#     print(recipe)

# def get_station_data(filename: str):
#     stations = {} 
    
#     with open(filename) as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             items = line.split(";")
#             name = items[3]
#             longitude = items[0]
#             latitude = (items[1])
#             if items[3] == "name":
#                 continue
#             stations[name] = (float(longitude), float(latitude))
            
#     return stations



# def distance(stations: dict, station1: str, station2: str):
#     import math
    
#     x_km = (stations[station1][0] - stations[station2][0]) * 55.26
#     y_km = (stations[station1][1] - stations[station2][1]) * 111.2
#     distance_km = math.sqrt(x_km**2 + y_km**2)

#     return distance_km



# def greatest_distance(stations: dict):
#     greatest_distance_value = 0
#     result = ()
#     name = list(stations.keys())
    
#     for station in range(len(stations)):
#         station1 = name[station]
        
#         for station in range(len(stations)):
#             station2 = name[station]
#             if station1 == station2:
#                 continue
#             greatest_distance_value_new = distance(stations, station1, station2)
#             if greatest_distance_value_new > greatest_distance_value:
#                 greatest_distance_value = greatest_distance_value_new
#                 result = station1, station2, greatest_distance_value
#     return result



# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)

# 6.2

# name = input("Whom should i sign this to:")
# where = input("Where shall i save it:")
# with open(where , "w") as my_file:
#     my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
# with open(where) as read_file:
#         text = []
#         for line in read_file:
#             text.append(line)
#             print(*text)

# function = int(input("Function:"))
# if function == 0:
#     print("Bye now!")

# if function == 2 and len("diary.txt") == 0:
#     with open("diary.txt") as new_file:   
#         print("Entries:")
#         for line in new_file:
#             print(line)

# if function == 2 and len("diary.txt") > 1:
#     with open("diary.txt") as new_file:
#         print("Entries:")
#         for line in new_file:
#             line = line.replace("\n", "")
#             print(line)




# if function == 1 and len("diary.txt") == 0:
#     diary_entry = input("Diary entry:")
#     with open("diary.txt", "w") as new_file:
#         new_file.write(f"{diary_entry}\n")
#         print("Diary saved")

# if function == 1 and len("diary.txt") > 0:
#     diary_entry = input("Diary entry:")
#     with open("diary.txt", "a") as new_file:
#         new_file.write(f"{diary_entry}\n")
#         print("Diary saved")

# def filter_solutions():
#     import os
#     if os.path.exists("correct.csv") == True:
#         os.remove("correct.csv")
#         os.remove("incorrect.csv")

#     with open("solutions.csv") as new_file:
#         solutions = []
#         for line in new_file:
#             line = line.replace("\n" , "")
#             line = line.split(";")
#             solutions += line[:]

#         for index in range(1, len(solutions) - 1, 3):
#             problem = solutions[index]
#             if "+" in problem:
#                 splited = problem.split("+")
#                 result = int(splited[0]) + int(splited[1])

#                 if result == int(solutions[index + 1]):
#                     with open("correct.csv", "a") as new_file:
#                         correct = solutions[index - 1], solutions[index], solutions[index + 1]
#                         new_file.write(f"{correct} \n")

#                 else:
#                     result != int(solutions[index + 1])
#                     with open("incorrect.csv", "a") as new_file:
#                         incorrect = solutions[index - 1], solutions[index], solutions[index + 1]
#                         new_file.write(f"{incorrect}\n")

#             else:
#                 splited = problem.split("-")
#                 result = int(splited[0]) - int(splited[1])

#                 if result == int(solutions[index + 1]):
#                     with open("correct.csv", "a") as new_file:
#                         correct = solutions[index - 1], solutions[index], solutions[index + 1]
#                         new_file.write(f"{correct} \n")
        
#                 else:
#                     result != int(solutions[index + 1])
#                     with open("incorrect.csv", "a") as new_file:
#                         incorrect = solutions[index - 1], solutions[index], solutions[index + 1]
#                         new_file.write(f"{incorrect}\n")

# filter_solutions()

# def store_personal_data(person: tuple):
#     with open("people.csv", "a") as new_file:
#         new_file.write(f"\n{person[0]};{str(person[1])};{str(person[2])}")
        

# store_personal_data(("Paul Paulson", 27, 1735.5))


def find_words(search_term: str):

    prefix = False
    suffix = False
    wild = False
    

    if search_term.startswith("*"):
        search_term = search_term[1:]
        prefix = True
    
    elif search_term.endswith("*"):
        search_term = search_term[:-1]
        suffix = True
    
    elif "." in search_term:
        if search_term[0] == ".":
            search_term = search_term[1:]
        search_term = search_term.split(".")
        start = search_term[0]
        end = search_term[1] 
        wild = True

    with open("words.txt") as new_file:
        finded = []
        for line in new_file:
            line = line.strip()

            if prefix and line.endswith(search_term):
                finded.append(line)

            elif suffix and line.startswith(search_term):
                finded.append(line)

            elif wild and start in line and end in line:
                finded.append(line)

            else:
                if not prefix and not suffix and not wild and search_term in line:
                    finded.append(line)

    return finded

print(find_words(".a.e"))

