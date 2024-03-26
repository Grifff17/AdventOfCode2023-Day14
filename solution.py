
directionsRotations = {
    "north":3,
    "east": 2,
    "south": 1,
    "west": 0
}

def solvepart1():
    data = fileRead("input.txt")
    platform = []
    for row in data:
        platform.append(list(row.strip()))

    newPlatform = slide(platform, "north")

    sum = 0
    for i in range(len(newPlatform)):
        for j in range(len(newPlatform[0])):
            if newPlatform[i][j] == "O":
                sum = sum + (len(newPlatform) - i)

    print(sum)
    
# slide all round rocks on platform in direction given
def slide(platform, direction):
    newPlatform = platform.copy()
    directionNum = directionsRotations[direction]
    for i in range(directionNum):
        newPlatform = rotate(newPlatform)

    for i in range(len(newPlatform)):
        for j in range(len(newPlatform[0])):
            if newPlatform[i][j] == "O":
                newPlatform[i][j] = "."
                for k in reversed(range(-1,j)):
                    if k == -1 or newPlatform[i][k] != ".":
                        newPlatform[i][k+1] = "O"
                        break
    
    for i in range(4-directionNum):
        newPlatform = rotate(newPlatform)

    return newPlatform

#rotate 2d list 90 degrees clockwise
def rotate(platform):
    output = list(zip(*platform[::-1]))
    output = [ list(row) for row in output ]
    return output

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()