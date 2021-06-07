scores = {}
result_f = open("Practice1.txt")
for line in result_f:
    (name,score) = line.split()
    scores[score] = name
result_f.close()

print("Top scores were: ")
for each_score in scores.keys():
    print('Suffer ' + scores[each_score] + ' scored ' + each_score)

scores = {}
result_f = open("Practice1.txt")
for line in result_f:
    (name,score) = line.split()
    scores[score] = name
result_f.close()

print("Top scores were: ")
for each_score in sorted(scores.keys(), reverse = True):
    print('Suffer ' + scores[each_score] + ' scored ' + each_score)