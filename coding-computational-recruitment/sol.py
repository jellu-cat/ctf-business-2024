def parse_txt_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(lines[2])
        headers = [header.strip()
                   for header in lines[2].split()]
        # print(headers)
        for line in lines[4:-1]:
            values = [value.strip() for value in line.split()]
            # print(values)
            person = {headers[i]: values[i]
                      for i in range(len(headers))}
            # print(person)
            data.append(person)
    return data

file_path = './data.txt'
people = parse_txt_file(file_path)
scores = people.copy()

print(people[0])

skill_weights = [0.2, 0.3, 0.1, 0.05, 0.05, 0.3]

for i in range(len(people)):
    h = int(people[i]['Health'])
    a = int(people[i]['Agility'])
    c = int(people[i]['Charisma'])
    k = int(people[i]['Knowledge'])
    e = int(people[i]['Energy'])
    r = int(people[i]['Resourcefulness'])

    h = h * skill_weights[0]
    h = round(6 * h) + 10

    a = a * skill_weights[1]
    a = round(6 * a) + 10

    c = c * skill_weights[2]
    c = round(6 * c) + 10

    k = k * skill_weights[3]
    k = round(6 * k) + 10

    e = e * skill_weights[4]
    e = round(6 * e) + 10

    r = r * skill_weights[5]
    r = round (6 * r) + 10

    overall = round(5 * ((h * 0.18) +
                    (a * 0.20) +
                    (c * 0.21) +
                    (k * 0.08) +
                    (e * 0.17) +
                    (r * 0.16)))
    people[i]['overall'] = overall

candidates = sorted(people, key=lambda d: d['overall'], reverse=True)

print()
for i in range(14):
    print(candidates[i]['First_Name'], ' ',
          candidates[i]['Last_Name'],
          ' - ', candidates[i]['overall'], ', ', end='', sep="")
print()
