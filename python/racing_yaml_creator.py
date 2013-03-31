# This script takes a CSV with the Wikipedia API url,
# grabs the race aliases from the Wikipedia content,
# and creates a YAML file

# Import CSV and convert it to a 2-D array
array = []
import csv
with open('nascar-nationwide-no-aliases.csv', 'rb') as csv_input:
    initial_csv = csv.reader(csv_input)
    next(initial_csv)
    for row in initial_csv:
      array.append(row)
      
# Getting the race event name aliases
import urllib2
for i in range (0, len(array)):
    
  # URL of the Wikipedia article content API
  # is stored in the 4th column of the CSV file
  wiki_url = array[i][3]

  # This is for postseason races
  # wiki_url = array[i][4]
  
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  infile = opener.open(wiki_url)
  scraped = infile.read()
  
  # I only want the text between the following strings
  first_string = "Previous names"
  last_string = "}}"  
  
  # This is for IndyCar
  # last_string = "Most"
  
  index1 = scraped.find(first_string) + len(first_string)

  # Removing all the crap in the front
  head_removed = scraped[index1:]
  index2 = head_removed.find(last_string)

  # Removing all the crap in the rear
  tail_removed = head_removed[0:index2]
  
  # "Normalization" rules; order is important!
  # These rules are for Nascar Sprint Cup 
  final_string = tail_removed.replace("&lt;", "")
  final_string = final_string.replace("'''", "")
  final_string = final_string.replace("[[", "")
  final_string = final_string.replace("]]", "")
  final_string = final_string.replace("p&gt;", "")
  final_string = final_string.replace(" br&gt; ", "")
  final_string = final_string.replace("br&gt; ", "")
  final_string = final_string.replace(" br&gt;", "")
  final_string = final_string.replace("br&gt;", "")  
  final_string = final_string.replace("br /&gt;", "")
  final_string = final_string.replace("br/&gt;", "")  
  final_string = final_string.replace("/small&gt;", "")
  final_string = final_string.replace("small&gt;", "")
  final_string = final_string.replace("&amp;", "&")
  final_string = final_string.replace("|\n", "")
  final_string = final_string.replace("| ", "")
  final_string = final_string.replace("  ", " ")   
  
  # Additional rules for Nascar Camping
  final_string = final_string.replace("BR&gt;", "") 
  
  # Additional rules for IndyCar
  final_string = final_string.replace("''", "")   
  final_string = final_string.replace("/u&gt;", " ")
  final_string = final_string.replace("u&gt;", "")    

  # Remove dates and parentheses
  while True:
    p_index1 = final_string.find("(")
    p_index2 = final_string.find(")") + 1
    final_string = final_string.replace(final_string[p_index1:p_index2], "\n")
    if final_string.find("(") == -1:
      break

  # Remove equals sign
  final_string = final_string.replace("=", "")

  # Remove extra lines
  final_string = final_string.replace("\n \n", "\n")
  final_string = final_string.rstrip("\n")
  final_string = final_string.replace("\n\n", "\n")
  final_string = final_string.replace("\n\n", "\n")
  final_string = final_string.replace("\n\n", "\n")

  # Remove any beginning and ending white space
  final_string = final_string.lstrip(" ")
  final_string = final_string.rstrip(" ")
  
  # Storing the aliases in the array
  array[i][3] = final_string
  
  # This is for postseason 
  # array[i][4] = final_string

# Outputting in YAML format
for row in array:
    print '-' + '\n' + '\t' + 'name: ' + row[0]
    print '\t' 'series: ' + row[1]
    print '\t' 'track: ' + row[2]
    print '\t' 'aliases:'
    aliases = row[3].split('\n')
    for row in aliases:
      print '\t\t' + row
      
# For postseason
# for row in array:
#     print '-' + '\n' + '\t' + 'name: ' + row[0]
#     print '\t' 'series: ' + row[1]
#     print '\t' 'track: ' + row[2]
#     print '\t' 'postseason: true'
#     print '\t' 'aliases:'
#     aliases = row[4].split('\n')
#     for row in aliases:
#       print '\t\t' + row
