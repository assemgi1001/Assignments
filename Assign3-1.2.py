
def print_surfer(s):
    print("ID: " + s['id'])
    print("Name: " + s['name'])
    print("Country: " + s['country'])
    print("Average: " + s['average'])
    print("Board type: " + s['board'])
    print("Age: " + s['age'])
    return

def find_details(id2find,filename):
    surfers_f = open(filename)
    for each_line in surfers_f:
        s = {}
        type(s)
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = each_line.split(";")
        s['newkey'] ='xyz'
        print(s.items())
        if id2find == int(s['id']):
            surfers_f.close()
            return(s)

line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"
s = {}
(s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(";")
print_surfer(s)
# on page 167


lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id, "surfing_data.csv")
if surfer:
    print_surfer(surfer)