import Algorithmia
import json

# The domain to crawl and number of links deep
# More here: https://algorithmia.com/algorithms/web/SiteMap
input = ["https://algorithmia.com",1]

# Replace YOUR API KEY with you free Algorithmia key
# https://algorithmia.com/signup
client = Algorithmia.client('simbxVBtbu5dT7f0lna7o7/Hr8L1')

# Here we call the Site Map algorithm
res = client.algo('web/SiteMap/0.1.7').pipe(input)

siteMap = res.result

links = []
output = []

# Iterate through the key-value pairs from the site map graph
# adding every URL to the links array
for keyLink in siteMap:
    links.append(keyLink)
    for valLink in siteMap[keyLink]:
        links.append(valLink)

# Remove duplicate links from the links array 
links = list(set(links))

# Iterate through the links calling Analyze URL on each 
# Then add the object to the output array
# More here: https://algorithmia.com/algorithms/web/AnalyzeURL
for l in links:
    analyze = client.algo('web/AnalyzeURL/0.2.14').pipe(l)
    output.append(analyze.result)

#saving in a json file
with open('metadata.json', 'w') as f:
	json.dumps(output, f, indent=4)


# Clean up JSON and print the result
#print json.dumps(output, indent=4)

# Run: python sitemap2analyzeUrl.py