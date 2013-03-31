import urllib2

wiki_url = "http://en.wikipedia.org/w/api.php?format=xml&action=query&prop=revisions&rvprop=content&titles=Honda_200"

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
# These rules are for Nascar Sprint Cup
tail_removed = head_removed[0:index2]
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

# This is added for Nascar Camping
final_string = final_string.replace("BR&gt;", "") 

# This is added for IndyCar
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

print final_string
