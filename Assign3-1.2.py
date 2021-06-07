line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"
s = {}
(s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(";")
print("ID: " + s['id'])
print("Name: " + s['name'])
print("Country: " + s['country'])
print("Average: " + s['average'])
print("Board type: " + s['board'])
print("Age: " + s['age'])
# on page 167
def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    for each_line in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(";")
        if id2find == int(s['id']):
            surfers_f.close()
            return(s)


lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id)
if surfer:
    print("ID: " + surfer['id'])
    print("Name: " + surfer['name'])
    print("Country: " + surfer['country'])
    print("Average: " + surfer['average'])
    print("Board type: " + surfer['board'])
    print("Age: " + surfer['age'])