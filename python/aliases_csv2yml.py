import csv
with open('../csv/nhra-regular-season.csv', 'rb') as csv_input:
    csv_array = csv.reader(csv_input)
    next(csv_array)
    for row in csv_array:
        print '-' + '\n' + '\t' + 'name: ' + row[0]
        print '\t' 'series: ' + row[1]
        print '\t' 'track: ' + row[2]
        # print '\t' 'postseason: true'
        print '\t' 'aliases:'        
        aliases = row[3].split('\n')
        for row in aliases:
          print '\t\t' + row