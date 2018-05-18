file_object = open('./survey.csv', 'r')
data = []
dictionary = {}
district_data = []

for row in file_object.readlines():
    data.append(row.replace('\n', '').split(', '))

for i in range(1, len(data)):
    temp_dist = {}
    dup = data[i][0].split(',')
    if dup[0] not in district_data:
        district_data.append(dup[0])
        dictionary[dup[0]] = {"count" : 0, "male_count" : 0, "female_count" : 0}

    if dup[3] == 'male':
        dictionary[dup[0]]['male_count'] += 1
    else:
        dictionary[dup[0]]['female_count'] += 1
    
    dictionary[dup[0]]['count'] += 1

print("District \t Female \t Male \t Total")
female_total, male_total, total_total = 0, 0, 0
for key in dictionary:
    female_total += dictionary[key]['female_count']
    male_total += dictionary[key]['male_count']
    total_total += dictionary[key]['count']

    if len(key) < 10:
        print("{} \t\t {} \t\t {} \t {}".format(key, dictionary[key]['female_count'], dictionary[key]['male_count'], dictionary[key]['count']))
    else:
        print("{} \t {} \t\t {} \t {}".format(key, dictionary[key]['female_count'], dictionary[key]['male_count'], dictionary[key]['count']))

print("{} \t\t {} \t\t {} \t {}".format("Total", female_total, male_total, total_total))
