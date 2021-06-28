
highest_score = 0
#open function
# result_f = file handle
result_f = open("../../AppData/Roaming/JetBrains/PyCharmCE2021.1/scratches/Practice.txt", 'r')
for line in result_f:
    (name, score) = line.split()
    # split function extracts the scores from the file
    if float(score) > highest_score:
        highest_score = float(score)
result_f.close()
print("The highest score was:")
print(highest_score)

scores = {}
result_f = open("../../AppData/Roaming/JetBrains/PyCharmCE2021.1/scratches/Practice.txt")
for line in result_f:
    (name, score) = line.split()
    scores[score] = name
result_f.close()
print("The top score were:")
for each_score in scores.keys():
    # iterating over each of the rows using for loop
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)

#persitent - stored in the Disk storage
# array is collection of variables