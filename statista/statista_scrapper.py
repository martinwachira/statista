
#python script to gather metadata files from a site using a site map by martin-wcr

#How to Run this Script
#1. Install python 3 on your machine
#2. Install pip (python library to download dependencies). Command -> python install pip
#3. Install virtual environement using pip to avoid getting every dependency manually. Command -> pip install virtualenv
#4. Create virtual environement using. Command -> virtualenv env
#5. Manouvre to the path folder where you created your virtual environment->env folder->script folder then run your code from this path e.g python.exe "path-to-the-python-file\yourcode.py"
# THAT IS IT! BINGO

#EXPECTED RESULT
#1. In your terminal you are supposed to see prompt "...saving metadata"
#2. Metadata json file saved in your path

import Algorithmia
import json
import os


#HERE YOU CAN CHANGE THE URL OF THE PAGE YOU WANT TO GATHER DATA FROM

#input = ["https://www.statista.com",1]
input=["https://www.statista.com/statistics/266136/global-market-share-held-by-smartphone-operating-systems/",1]

client = Algorithmia.client('simvqhtc2cpBpS52Iw+6yed5VfK1')

res = client.algo('web/SiteMap/0.1.7').pipe(input)

siteMap = res.result

#print (siteMap)

links = []
output = []

#looping through each link on the page
for keyLink in siteMap:
    links.append(keyLink)
    for valLink in siteMap[keyLink]:
        links.append(valLink)

links = list(set(links))

for l in links:
    analyze = client.algo('web/AnalyzeURL/0.2.14').pipe(l)
    output.append(analyze.result)

#metadata = {**src_metadata, **info_metadata}

#metadata file name
meta_dir = os.path.join('metadata_smartphone-operating-systems.json')
print('...saving metadata')
with open(meta_dir, 'w') as meta_file:
    json.dump(output, meta_file)

#time.sleep(2)

#print (json.dumps(output, indent=4))