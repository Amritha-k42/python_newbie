marks =[95, 89, 83, "dsa"]
print(marks)
print(marks[2])
print(marks[-1])
print(marks[0:3])
print(marks[1:3])
marks.append(99)
marks.insert(0, 99)
marks.insert(1,100)

for score in marks:
    print(score)
print("length is: " + str(len(marks)))