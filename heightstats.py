def min(values):
    _min = values[0]
    for val in values:
        if val < _min:
            _min = val

    return _min

    
def max(height):
    _max = height[0]
    for cm in height:
        if cm > _max:
            _max = cm
    return _max




def median(num):
    return num[2]


def median(num):
    num.sort()
    if len(num) % 2 == 1:
        return num[len(num)//2]
    else:
        return (num[len(num)//2-1] + num[len(num)//2])/2
    
def mode(num):
    frequency={}
    for number in num:
        frequency.setdefault(number,0)
        frequency[number]+=1
    highestFrequency=max(frequency.values())
    highestFreqIndex=[]
    for number, freq in frequency.items():
        if freq == highestFrequency:
            highestFreqIndex.append(number)
    return highestFreqIndex
    

def mode(num):
	frequency={}
	for number in num:
		frequency.setdefault(number,0)
		frequency[number]+=1
	highestFrequency=max(frequency.values())
	return highestFrequency

	highestFrequency=max(frequency.values())
	highestFreqLst=[]
	for number, freq in frequency.items():
		if freq == highestFrequency:
			highestFreqLst.append(number)
	return highestFreqLst
    
def max(height):
    _max = height[4]
    return _max
def max(height):
    _max = height[0]
    for cm in height:
        if cm > _max:
            _max = cm
    return _max