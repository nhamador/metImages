from urllib.request import urlopen
import json
writer = open("paintImg.txt", 'w')
with open('paint.txt') as topo_file:
    for line in topo_file:
        try:
            url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + line;
            response = urlopen(url)
            data_json = json.loads(response.read())
            imgUrl = data_json["primaryImage"];
            if imgUrl != "":
                writer.write(line);
            print(data_json["primaryImage"]);
        except:
            print("That URL was not found");
    print("exiting :-)")
