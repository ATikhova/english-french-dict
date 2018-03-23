e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
f2e = {}
for a, b in e2f.items():
	f2e[b] = a
print(f2e)

print(f2e['chien'])

print(set(e2f))
