import urllib.request as ur
import json

gameid = input("Enter game id:2830e05d-7358-4f26-bcd9-4122c0b0dfe5_1682691182108 ")
url = "https://play.kahoot.it/rest/kahoots/" + gameid
q = json.loads(ur.urlopen(url).read())["questions"]
colours = ["red", "blue", "yellow", "green"]

for index, slide in enumerate(q):
    if slide.get("type") == "quiz":
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"]:
                colours_list = colours[:2][::-1] if len(slide.get("choices")) == 2 else colours
                print("Question number: {}\n{}\n{}\n".format(
                    index + 1, slide["choices"][i].get("answer"), colours_list[i]))
