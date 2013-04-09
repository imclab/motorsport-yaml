# Motorsport data YAML's

Motorsport data YAML files created using Python to scrape and parse from the Wikipedia API.

## CSV files

These were created using this Chrome <a href="https://chrome.google.com/webstore/detail/scraper/mbigbapnjcgaffohmbkdlecaccepngjd" target="_blank">scraping extension</a> to find the proper XPaths for the relevant data from the following Wikipedia pages:

<a href="http://en.wikipedia.org/wiki/2013_F1" target="_blank">2013 Formula One season</a>
<br />
<a href="http://en.wikipedia.org/wiki/2013_IndyCar_Series_season" target="_blank">2013 IndyCar Series season</a>
<br />
<a href="http://en.wikipedia.org/wiki/2013_NASCAR_Sprint_Cup_Series" target="_blank">2013 NASCAR Sprint Cup Series</a>
<br />
<a href="http://en.wikipedia.org/wiki/2013_NASCAR_Nationwide_Series" target="_blank">2013 NASCAR Nationwide Series</a>
<br />
<a href="http://en.wikipedia.org/wiki/2013_NASCAR_Camping_World_Truck_Series" target="_blank">2013 NASCAR Camping World Truck Series</a>
<br />
<a href="http://en.wikipedia.org/wiki/2013_NHRA_Mello_Yello_Drag_Racing_Series" target="_blank">2013 NHRA Mello Yello Drag Racing Series</a>
<br />
<br />
After grabbing the appropriate Wikipeida URL's for the relevant race events, I then used them to generate the respective URL's from Wikipedia's <a href="http://www.mediawiki.org/wiki/API:Main_page" target="_blank">MediaWiki API</a>.

## Python scripts

<a href="https://github.com/serve-and-volley/motorsport-yaml/blob/master/python/race_alias_tester.py" target="_blank">race_alias_tester.py</a>
<br />
This is used to test the API URL's and to figure out the parsing rules to extract the race event aliases. This was a big pain in the ass since Wikipedia articles do not have uniform formatting.

<a href="https://github.com/serve-and-volley/motorsport-yaml/blob/master/python/racing_yaml_creator.py" target="_blank">racing_yaml_creator.py</a>
<br />
This is the main script that reads the CSV files, parses for the race event aliases from the Wikipedia API, and then creates the corresponding YAML file. Because Wikipedia data is not uniform, some minor cleaning up of the YAML files after they were created was necessary.

<a href="https://github.com/serve-and-volley/motorsport-yaml/blob/master/python/aliases_csv2yml.py" target="_blank">aliases_csv2yml.py</a>
<br />
This is the quick script that creates the YAML file from a CSV file that already contains the race event aliases, such as the case for Formula One.
