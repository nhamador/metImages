from types import SimpleNamespace
from urllib.request import urlopen
import json
f = open("output.txt", 'w')
for x in range (1,860874):
    try:
        url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(x);
        response = urlopen(url)
        data_json = json.loads(response.read())
        imgUrl = data_json["primaryImage"];
        if imgUrl != "":
            f.write(str(x)+"\n");
        print(data_json["primaryImage"]);
    except:
        print("That URL was not found");

  ##  f.write(data + "\n")