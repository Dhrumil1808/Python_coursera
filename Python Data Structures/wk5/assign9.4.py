name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()

for line in handle:
    if line.startswith("From "):
        emails[line.split(" ")[1]] = emails.get(line.split(" ")[1], 0) + 1

bigCount = 0
bigEmail = 0

for key,value in emails.items():
    if bigCount is None or value > bigCount:
        bigEmail = key
        bigCount = value

print bigEmail, bigCount