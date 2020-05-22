import csv

with open('eggs.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # writer.writerow(['data', 'result', 'code'])
    # for i in range(10):
    #     writer.writerow([i, i * 100, str(bin(i))])

    test = [
            {"Name": "Dominator", "skill": 100, "gold": 99999},
            {"Name": "Looser", "skill": 1, "gold": 5000}
    ]

    writer.writerow(['Name', 'skill', 'gold'])
    for key in test:
        print(test)
        # writer.writerow(test)