import csv

wantedMedium = "Oil on canvas"

with open('MetObjects.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',') # good point by @paco
    for row in reader:
        try:
            for field in row:
                print(field);
                print("lol");
                # if field == username:
                #    print "is in file"
        except:
            print("Undefined Found")

