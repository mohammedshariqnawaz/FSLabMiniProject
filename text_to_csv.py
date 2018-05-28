import csv

with open('estatedetails.txt', 'r') as in_file:

    stripped = (line.strip() for line in in_file)
    lines = (line.split("|") for line in stripped if line)
    with open('log.csv', 'w') as out_file:
        writer=csv.writer(out_file, delimiter =' ',quotechar =',',quoting=csv.QUOTE_MINIMAL)

        # writer = csv.writer(out_file)
        for line in lines:
            writer.writerow(line[1].split())
            writer.writerow(line[3].split())
            writer.writerow(line[4].split())
# f=open('log.csv','wb') # opens file for writing (erases contents)
# csv.writer(f, delimiter =' ',quotechar =',',quoting=csv.QUOTE_MINIMAL)
