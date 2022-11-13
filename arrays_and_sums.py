class ResultException(Exception):
    def __init__(self, result):
        self.result = result
 
def checkSum3(subSet, wanted, current):
    if wanted == current:
        raise ResultException(1)
    
    if(len(subSet) <= 0) or current > wanted:
        return
 
    temp = [x for x in subSet if x + current <= wanted]
 
    i = 1
    while( i <= len(temp)):
        checkSum3(temp[i:], wanted, current + temp[0])
        i += 1
 
    checkSum3(temp[1:], wanted, current)
 
    return
 
def getCheckSumResult(array, wanted):
    try:
        checkSum3(array, wanted, 0)
        return 0
    except ResultException as e:
        return e.result
 
def checkSumArray(array, size):
    results = []
    for j in range(size):
        temp = array.copy()
        temp.pop(j)
        if array[j] in temp or array[j] == 0:
            result = 1
        else:
            result = getCheckSumResult([x for x in temp if x < array[j]], array[j])
        results.append(result)
    
    resultsString = ' '.join(str(e) for e in results)
    print(resultsString)
 
 
 
ntestCases = int(input())
 
for i in range(ntestCases):
    size = int(input())
    array = list(map(int, input().split(' ')))
 
    checkSumArray(array, size)
