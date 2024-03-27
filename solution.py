
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

def solvepart2():
    #read data
    data = fileRead("input.txt")
    platform = []
    for row in data:
        platform.append(list(row.strip()))

    #perform spins until a cycle is found
    foundCycles = {}
    i = 0
    while not tuple(platform) in foundCycles.values():
        foundCycles[i] = tuple(platform)
        platform = spinCycle(platform)
        i = i + 1
    
    #calculate state at 1 billionth cycle
    loopStart = list(foundCycles.keys())[list(foundCycles.values()).index(tuple(platform))]
    loopEnd = i
    endPos = (1000000000-loopStart)%(loopEnd-loopStart) + loopStart
    endPlatform = foundCycles[endPos]

    #get north load at 1 billionth cycle
    sum = 0
    for i in range(len(endPlatform)):
        for j in range(len(endPlatform[0])):
            if endPlatform[i][j] == "O":
                sum = sum + (len(endPlatform) - i)

    print(sum)


#perform one spin cycle
def spinCycle(platform):
    for i in range(4):
        platform = slideRotate(platform)
    return platform

# rotate platform clockwise then slide east
def slideRotate(platform):
    newPlatform = platform.copy()
    newPlatform = rotate(newPlatform)

    for i in range(len(newPlatform)):
        for j in reversed(range(len(newPlatform[0]))):
            if newPlatform[i][j] == "O":
                newPlatform[i][j] = "."
                for k in range(j,len(newPlatform[0])+1):
                    if k == len(newPlatform[0]) or newPlatform[i][k] != ".":
                        newPlatform[i][k-1] = "O"
                        break

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

solvepart2()