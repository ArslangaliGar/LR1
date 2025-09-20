scores = {"Ivan": 70 , "Drakosha": 73, "Mishania": 52}
scores["Ghost"] = 90
scores["Mishania"] = 58
x = scores.get("Fake")
y = scores.get("Drakosha")
scores.pop("Ivan")
print(scores,x,y)
