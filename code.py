import interface
import numpy as np
import threading



def dupliquer(lists):
    ech = []
    for i in lists:
        if i in ech:
            return i
        ech.append(i)
    return 0

def etudiants_critiques(lists, et):
    positions = []
    for i in range(len(lists)):
        if lists[i] == et:
            positions.append('e'+str(i+1))
    return positions

def etablissements_critiques(lists, et):
    positions = []
    for i in range(len(lists)):
        if lists[i] == et:
            positions.append('s'+str(i+1))
    return positions

    

effectifs = 0
etudiants = []
etablissements = []
pref_etudiants = {}
pref_etablissements = {}
choix_etu = {}
choix_eta = {}
capacite = []
trace_etu = {}
trace_eta = {}



saisi = input("Saisissez 1 si vous voulez des préférences aléatoires.\nSaisissez 2 si vous voulez le tester sur votre jeux de données.\n")
if saisi == '1':
	effectifs = input("Entrer le nombre d'etudiants : ")
	effectifs = int(effectifs)
	for i in range(1, effectifs+1):
		etudiants.append('e' + str(i))
		etablissements.append('s' + str(i))

	for et in etudiants:
		pref_etudiants[et] = []
		while len(pref_etudiants[et]) < effectifs:
			val = np.random.choice(etablissements)
			if val not in pref_etudiants[et]:
				pref_etudiants[et].append(val)

	for et in etablissements:
		pref_etablissements[et] = []
		while len(pref_etablissements[et]) < effectifs:
			val = np.random.choice(etudiants)
			if val not in pref_etablissements[et]:
				pref_etablissements[et].append(val)

elif saisi == '2':
	chemin = input("Entrer le chemin du fichier .py : ")
	try:
	    variables = {}
	    with open(chemin, "r") as fichier:
	        code = fichier.read()
	        exec(code, {}, variables)
	    effectifs = variables.get("effectifs")
	    capacite = variables.get("capacite")
	    etudiants = variables.get("etudiants")
	    etablissements = variables.get("etablissements")
	    pref_etudiants = variables.get("pref_etudiants")
	    pref_etablissements = variables.get("pref_etablissements")
	except Exception as e:
	    print("Une erreur s'est produite lors de l'exécution du code du fichier :", e)
	    exit()

else:
	print('Merci de votre confiance.')
	exit()



print("Preference des étudiants.")
for et in etudiants:
	print(et, ':', pref_etudiants[et])
	choix_etu[et] = []
	choix_etu[et] = pref_etudiants[et].copy()
print("Preference des établissements.")
for et in etablissements:
	capacite.append(1)
	choix_eta[et] = []
	choix_eta[et] = pref_etablissements[et].copy()
	print(et, ':', pref_etablissements[et])



print("\nAlgorithme du mariage stable en fonction des etablissements.")
count = 0
while True:
	voeux = []
	for et in etudiants:
		voeux.append(choix_etu[et][0])
	trace_etu[count] = voeux.copy()
	count+=1

	et_dup = dupliquer(voeux)
	if et_dup == 0:
		break;
	positions = etudiants_critiques(voeux, et_dup)

	for pref_et in pref_etablissements[et_dup]:
		if pref_et in positions:
			for p in positions:
				if pref_et != p:
					for i in range(len(choix_etu[p])-1):
						choix_etu[p][i] = choix_etu[p][i+1]
			break;

for index, tr in enumerate(trace_etu):
	i = 0
	a = ''
	print('Etape '+str(index+1))
	for etu, eta in zip(etudiants, etablissements):
		a = etu+' :'
		for pref_et in pref_etudiants[etu]:
			if pref_et == trace_etu[tr][i]:
				a = a+'['+pref_et+']'
			else:
				a = a+' '+pref_et+' '
		j = 0
		lists = []
		a = a+'   -  '
		a = a+' '+eta+' :'
		for t in trace_etu[tr]:
			if eta == t:
				lists.append('e'+str(j+1))
			j+=1
		for pref_et in pref_etablissements[eta]:
			if pref_et in lists:
				a = a+'['+pref_et+']'
			else:
				a = a+' '+pref_et+' '
		print(a)
		a=''
		i+=1


print('\nRésultats')
for index, et in enumerate(etudiants):
	print(et," --> ",trace_etu[count-1][index])


print('\nSatisfactions des Etudiants')
total = 0
for i, et in enumerate(etudiants):
	choix = trace_etu[len(trace_etu)-1][i]
	index = len(pref_etudiants[et])
	for pref_et in pref_etudiants[et]:
		if pref_et == choix:
			pourc = round((index / len(pref_etudiants[et])) * 100, 2)
			print(et+' : '+str(pourc)+'%')
			total += pourc
			break;
		index-=1
print('Total : '+str(round(total / len(pref_etudiants), 2))+'%')


print('\nSatisfactions des etablissements')
total = 0
for i, tr in enumerate(trace_etu[len(trace_etu)-1]):
	choix = 'e'+str(i+1)
	index = len(pref_etablissements[tr])
	for pref_et in pref_etablissements[tr]:
		if pref_et == choix:
			pourc = round((index / len(pref_etablissements[tr])) * 100, 2)
			print(tr+' : '+str(pourc)+'%')
			total += pourc
			break;
		index-=1
print('Total : '+str(round(total / len(pref_etablissements), 2))+'%')




print("\nAlgorithme du mariage stable en fonction des etudiants.")
count = 0
while True:
	voeux = []
	for et in etablissements:
		voeux.append(choix_eta[et][0])
	trace_eta[count] = voeux.copy()
	count+=1

	et_dup = dupliquer(voeux)
	if et_dup == 0:
		break;
	positions = etablissements_critiques(voeux, et_dup)

	for pref_et in pref_etudiants[et_dup]:
		if pref_et in positions:
			for p in positions:
				if pref_et != p:
					for i in range(len(choix_eta[p])-1):
						choix_eta[p][i] = choix_eta[p][i+1]
			break;


for index, tr in enumerate(trace_eta):
	i = 0
	a = ''
	print('Etape '+str(index+1))
	for etu, eta in zip(etudiants, etablissements):
		j = 0
		lists = []
		a = etu+' :'
		for t in trace_eta[tr]:
			if etu == t:
				lists.append('s'+str(j+1))
			j+=1
		for pref_et in pref_etudiants[etu]:
			if pref_et in lists:
				a = a+'['+pref_et+']'
			else:
				a = a+' '+pref_et+' '
		a = a+'   -  '
		a = a+' '+eta+' :'
		for pref_et in pref_etablissements[eta]:
			if pref_et == trace_eta[tr][i]:
				a = a+'['+pref_et+']'
			else:
				a = a+' '+pref_et+' '
		print(a)
		a=''
		i+=1


print('\nRésultats')
for index, et in enumerate(etablissements):
	print(et," --> ",trace_eta[count-1][index])


print('\nSatisfactions des Etudiants')
total = 0
for i, tr in enumerate(trace_eta[len(trace_eta)-1]):
	choix = 's'+str(i+1)
	index = len(pref_etudiants[tr])
	for pref_et in pref_etudiants[tr]:
		if pref_et == choix:
			pourc = round((index / len(pref_etudiants[tr])) * 100, 2)
			print(tr+' : '+str(pourc)+'%')
			total += pourc
			break;
		index-=1
print('Total : '+str(round(total / len(pref_etudiants), 2))+'%')


print('\nSatisfactions des etablissements')
total = 0
for i, et in enumerate(etablissements):
	choix = trace_eta[len(trace_eta)-1][i]
	index = len(pref_etablissements[et])
	for pref_et in pref_etablissements[et]:
		if pref_et == choix:
			pourc = round((index / len(pref_etablissements[et])) * 100, 2)
			print(et+' : '+str(pourc)+'%')
			total += pourc
			break;
		index-=1
print('Total : '+str(round(total / len(pref_etablissements), 2))+'%')

interface.interface(etudiants, pref_etudiants, etablissements, pref_etablissements, capacite, trace_etu, trace_eta)