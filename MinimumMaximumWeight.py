from collections import Counter
import csv

def getMean(totalweight, totalentries):
    mean = totalweight / totalentries
    print(f"Mean (Average) is -> {mean:2f}")

def getMedian(totalentries, sorteddata):
    if totalentries % 2 == 0:
        median1 = float(sorteddata[totalentries//2])
        median2 = float(sorteddata[totalentries//2 - 1])
        median = (median1 + median2) / 2
    else:
        median = float(sorteddata[totalentries//2])
    print(f"Median is -> {median:2f}")

def getMode(sorted_data):
    data = Counter(sorted_data)
    modeDataForRange = {
                            "75-85": 0,
                            "85-95": 0,
                            "95-105": 0,
                            "105-115": 0,
                            "115-125": 0,
                            "125-135": 0,
                            "135-145": 0,
                            "145-155": 0,
                            "155-165": 0,
                            "165-175": 0
                        }
    for weight,occurence in data.items():
        if 75 < weight < 85:
            modeDataForRange["75-85"] += occurence
        elif 85 < weight < 95:
            modeDataForRange["85-95"] += occurence
        elif 95 < weight < 105:
            modeDataForRange["95-105"] += occurence
        elif 105 < weight < 115:
            modeDataForRange["105-115"] += occurence
        elif 115 < weight < 125:
            modeDataForRange["115-125"] += occurence
        elif 125 < weight < 135:
            modeDataForRange["125-135"] += occurence
        elif 135 < weight < 145:
            modeDataForRange["135-145"] += occurence
        elif 145 < weight < 155:
            modeDataForRange["145-155"] += occurence
        elif 155 < weight < 165:
            modeDataForRange["155-165"] += occurence
        elif 165 < weight < 175:
            modeDataForRange["165-175"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in modeDataForRange.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode:2f}")

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

totalweight = 0
totalentries = len(file_data)
sorteddata = []

for person_data in file_data:
    totalweight += float(person_data[2])
    sorteddata.append(float(person_data[2]))

sorteddata.sort()
getMean(totalweight, totalentries)
getMedian(totalentries, sorteddata)
getMode(sorteddata)
