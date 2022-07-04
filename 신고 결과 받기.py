report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# report = list(set(report))
list = []
#a는 신고자, b는 신고 당한자
for i in range(len(report)):
    a, b = report[i].split()
    list.append(a)
    list.append(b)

print(list)