#  create a python script to dump the top level readme file with inside contents #4 
import os
# travese all the folders
# copy the README.md files into the outer README.md file.

with open('README.md', 'w') as outfile:
    for folders in os.listdir('./'):
        if os.path.isfile(f'./{folders}/README.md'):
            with open(f'./{folders}/README.md') as infile:
                # print(infile.read())
                outfile.write('**'+folders+'**\n')
                outfile.write(infile.read())
                outfile.write("\n\n****\n\n")

        
           



