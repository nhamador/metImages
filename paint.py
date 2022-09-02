import csv

wantedMedium = "Oil on canvas"

with open('MetObjects.csv', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',') # good point by @paco
    writer = open("paint.txt", 'w')
    for row in reader:
        try:
            for field in row:
               # print(field);
                if(field == "Oil on canvas"):
                    writer.write(str(row[4])+"\n");
                # if field == username:
                #    print "is in file"
        except:
            print("Undefined Found")

