# str 可以當作清單來看待

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip().split(' '))

times = []
persons = []

for line in lines:
	time = line[0][:5]
	person = line[0][5:10]
	times.append(time)
	persons.append(person)

print(times)
print(persons)