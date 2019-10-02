print ("Exercise 1")
aircrafts = {
    "x": 567.888,
    "y": 895.11
}
print ("X -", aircrafts["x"], ", Y -", aircrafts["y"])
multipleAircrafts = [{"x": 123.345, "y": 234.567},
                     {"x": 23.345, "y": 24.567},
                     {"x": 13.345, "y": 23.567},
                     {"x": 129.345, "y": 237.567},
                     {"x": 193.345, "y": 239.567},
                     {"x": 123.366, "y": 236.67}]
for aircraft in multipleAircrafts:
    print ("X -", aircraft["x"], ", Y -", aircraft["y"])

