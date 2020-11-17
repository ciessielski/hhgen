import os

pwd

files = os.listdir("./hhgen/txt/")

lines_seen = set() # holds lines already seen
with open("./hhgen/cleaned.txt", "w") as outfile:
    for file in files:
        with open(f"./hhgen/txt/{file}") as infile:
            for line in infile:
                if '[' in line:
                    pass
                else:
            	    if line not in lines_seen: # check if line is not duplicate
            	        outfile.write(line)
            	        lines_seen.add(line)
