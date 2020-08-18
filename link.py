import csv, random, webbrowser

BIG_LIST_FILE = "list.csv"
action = input("What would you like to do? ")

if action == "add":
    url = input("URL: ")
    tags = input("tags: ").strip()
    with open(BIG_LIST_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([url, tags, ""])
    exit(1)

if action == "read":
    ran = input("random? ")
    if ran:
        with open(BIG_LIST_FILE, newline="") as csvfile:
            file = list(csv.reader(csvfile))[1:]
            random_url = random.choice(file)[0]
        print(random_url)
        ok = input("good? ")
        if positive(ok):
            webbrowser.open_new_tab(random_url)
    search = input("search for something: ").lower()
    with open(BIG_LIST_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        matches = [
            row["url"] for row in reader if search in row["tags"] and not row["read"]
        ]
    print(matches)
    i = int(input("index: "))
    if i < len(matches):
        webbrowser.open_new_tab(matches[i])


def positive(var):
    var = var.lower()
    return var == "yes" or var == "y"
