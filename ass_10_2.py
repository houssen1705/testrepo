count_hour = dict()
name = input("Enter file:")
handle = open("mbox-short.txt")

for line in handle:
    if not line.startswith("From "):
        continue
    new_split = line.strip().split()
    time = new_split[5]
    split_hour = time.split(":")
    hours = split_hour[0:1]
    for h in hours:
        count_hour[h] = count_hour.get(h, 0) + 1
my_list = list()
#use key and value and go through the dictionary
#and sort by key and value using ASC order
my_list =sorted((k,v)for k,v in count_hour.items())
#go through each item on the list and print the first and second character
for n in my_list:
    print(n[0], n[1])
