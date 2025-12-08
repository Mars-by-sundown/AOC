def part_1(inputs):
    rolls = 0
    [print(x) for x in inputs]
    n = len(inputs[0])
    m = len(inputs)
    numAdj = [[0]*n for x in range(0,m)]
    rollset = set()
    dirs = [[-1,-1], [0,-1], [1,-1],
            [-1,0],        [1,0],
            [-1,1],[0,1],[1,1]]
    for row in range(0,m):
        for col in range(0,n):
            if inputs[row][col] == "@":
                for each in dirs:
                    x = col + each[0]
                    y = row + each[1]
                    if (x >= 0) and (x < n) and (y >= 0) and (y < m):
                        if inputs[y][x] == '@':
                            # print(row,col,numAdj[row][col])
                            numAdj[row][col] += 1
                rollset.add((row,col))
    for each in numAdj:
        print(each)
    for each in rollset:
        if numAdj[each[0]][each[1]] < 4:
            rolls += 1


    return rolls



fl = open("testcase.txt","r")
inputs = [str(x).strip() for x in fl.readlines()]
print(part_1(inputs))