import PySimpleGUI as sg


largeur = 900
longeur = 900


def aff_pref_etudiants(etudiants, pref_etudiants):
	aff = [[sg.T('Préférences des etudiants', font=('Times New Roman', 12, 'italic'))]]
	for et in etudiants:
		a = [sg.Button(et, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(10, 0))]
		for pref_et in pref_etudiants[et]:
			a.append(sg.Button(pref_et, button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
		aff.append(a)
	return aff

def aff_pref_etablissements(etablissements, pref_etablissements):
	aff = [[sg.T('Préférences des etablissements', font=('Times New Roman', 12, 'italic'))]]
	for et in etablissements:
		a = [sg.Button(et, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(10, 0))]
		for pref_et in pref_etablissements[et]:
			a.append(sg.Button(pref_et, button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
		aff.append(a)
	return aff

def aff_capacite(etablissements, capacite):
	aff = [[sg.T('Capacité des etablissements', font=('Times New Roman', 12, 'italic'))]]
	for et, ca in zip(etablissements, capacite):
		a = [sg.Button(et, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(10, 0))]
		a.append(sg.Button(str(ca), button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
		aff.append(a)
	return aff

def aff_algo_etablissements(etudiants, pref_etudiants, etablissements, pref_etablissements, trace):
	aff = []
	for index, tr in enumerate(trace):
		i = 0
		aff.append([sg.T('Etape '+str(index+1), font=('Times New Roman', 12, 'italic'))])
		for etu, eta in zip(etudiants, etablissements):
			a = [sg.Button(etu, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(10, 0))]
			for pref_et in pref_etudiants[etu]:
				if pref_et == trace[tr][i]:
					a.append(sg.Button(pref_et, button_color=('black', '#BBFB7D'), font='Helvetica 10', pad=(0, 0)))
				else:
					a.append(sg.Button(pref_et, button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))

			j = 0
			lists = []
			a.append(sg.T('  -', font=('Times New Roman', 12, 'italic')))
			a.append(sg.Button(eta, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(10, 0)))
			for t in trace[tr]:
				if eta == t:
					lists.append('e'+str(j+1))
				j+=1
			for pref_et in pref_etablissements[eta]:
				if pref_et in lists:
					a.append(sg.Button(pref_et, button_color=('black', '#BBFB7D'), font='Helvetica 10', pad=(0, 0)))
				else:
					a.append(sg.Button(pref_et, button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))

			aff.append(a)
			i+=1
	return aff

def aff_algo_etudiants(etudiants, pref_etudiants, etablissements, pref_etablissements, trace):
	aff = []
	for index, tr in enumerate(trace):
		i = 0
		aff.append([sg.T('Etape '+str(index+1), font=('Times New Roman', 12, 'italic'))])
		for etu, eta in zip(etudiants, etablissements):
			j = 0
			lists = []
			a = [sg.Button(etu, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(10, 0))]
			for t in trace[tr]:
				if etu == t:
					lists.append('s'+str(j+1))
				j+=1
			for pref_et in pref_etudiants[etu]:
				if pref_et in lists:
					a.append(sg.Button(pref_et, button_color=('black', '#BBFB7D'), font='Helvetica 10', pad=(0, 0)))
				else:
					a.append(sg.Button(pref_et, button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))

			a.append(sg.T('  -', font=('Times New Roman', 12, 'italic')))
			a.append(sg.Button(eta, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(10, 0)))
			for pref_et in pref_etablissements[eta]:
				if pref_et == trace[tr][i]:
					a.append(sg.Button(pref_et, button_color=('black', '#BBFB7D'), font='Helvetica 10', pad=(0, 0)))
				else:
					a.append(sg.Button(pref_et, button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
			aff.append(a)
			i+=1
	return aff

def aff_resultat(trace, etudiants):
	i = 0 
	a = []
	for et in etudiants:
		a.append(sg.Button(et, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0)))
		a.append(sg.Button(str(trace[len(trace)-1][i]), button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
		a.append(sg.T('  ', font=('Times New Roman', 12, 'italic')))
		i+=1
	return [a]

def aff_resultat(trace, etablissements):
	i = 0 
	a = []
	for et in etablissements:
		a.append(sg.Button(et, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0)))
		a.append(sg.Button(str(trace[len(trace)-1][i]), button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
		a.append(sg.T('  ', font=('Times New Roman', 12, 'italic')))
		i+=1
	return [a]

def aff_satis_etudiants1(trace, etudiants, pref_etudiants):
	a = ''
	total = 0
	aff = [[sg.T('Etudiants', font=('Times New Roman', 12, 'italic'))]]
	for i, et in enumerate(etudiants):
		choix = trace[len(trace)-1][i]
		index = len(pref_etudiants[et])
		for pref_et in pref_etudiants[et]:
			if pref_et == choix:
				pourc = round((index / len(pref_etudiants[et])) * 100, 2)
				a = [sg.Button(et, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0))]
				a.append(sg.Button(str(pourc)+' %', button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
				aff.append(a)
				total += pourc
				break;
			index-=1
	a = [sg.Button('Total : ', button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0))]
	a.append(sg.Button(str(round(total / len(pref_etudiants), 2))+' %', button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
	aff.append(a)
	return aff

def aff_satis_etablissements1(trace, etablissements, pref_etablissements):
	a = ''
	total = 0
	aff = [[sg.T('Etablissements', font=('Times New Roman', 12, 'italic'))]]
	for i, tr in enumerate(trace[len(trace)-1]):
		choix = 'e'+str(i+1)
		index = len(pref_etablissements[tr])
		for pref_et in pref_etablissements[tr]:
			if pref_et == choix:
				pourc = round((index / len(pref_etablissements[tr])) * 100, 2)
				a = [sg.Button(tr, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0))]
				a.append(sg.Button(str(pourc)+' %', button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
				aff.append(a)
				total += pourc
				break;
			index-=1
	a = [sg.Button('Total : ', button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0))]
	a.append(sg.Button(str(round(total / len(pref_etablissements), 2))+' %', button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
	aff.append(a)
	return aff

def aff_satis_etudiants2(trace, etudiants, pref_etudiants):
	a = ''
	total = 0
	aff = [[sg.T('Etudiants', font=('Times New Roman', 12, 'italic'))]]
	for i, tr in enumerate(trace[len(trace)-1]):
		choix = 's'+str(i+1)
		index = len(pref_etudiants[tr])
		for pref_et in pref_etudiants[tr]:
			if pref_et == choix:
				pourc = round((index / len(pref_etudiants[tr])) * 100, 2)
				a = [sg.Button(tr, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0))]
				a.append(sg.Button(str(pourc)+' %', button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
				aff.append(a)
				total += pourc
				break;
			index-=1
	a = [sg.Button('Total : ', button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0))]
	a.append(sg.Button(str(round(total / len(pref_etudiants), 2))+' %', button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
	aff.append(a)
	return aff

def aff_satis_etablissements2(trace, etablissements, pref_etablissements):
	a = ''
	total = 0
	aff = [[sg.T('Etablissements', font=('Times New Roman', 12, 'italic'))]]
	for i, et in enumerate(etablissements):
		choix = trace[len(trace)-1][i]
		index = len(pref_etablissements[et])
		for pref_et in pref_etablissements[et]:
			if pref_et == choix:
				pourc = round((index / len(pref_etablissements[et])) * 100, 2)
				a = [sg.Button(et, button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0))]
				a.append(sg.Button(str(pourc)+' %', button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
				aff.append(a)
				total += pourc
				break;
			index-=1
	a = [sg.Button('Total : ', button_color=('black', '#66A8CF'), font='Helvetica 10', pad=(0, 0))]
	a.append(sg.Button(str(round(total / len(pref_etablissements), 2))+' %', button_color=('black', 'white'), font='Helvetica 10', pad=(0, 0)))
	aff.append(a)
	return aff

def interface(etudiants, pref_etudiants, etablissements, pref_etablissements, capacite, trace_etu, trace_eta):
	sg.theme('DarkBlue')

	affichage = [
        [sg.Column(layout=[
        	[sg.T("Génération des préférences aléatoires des étudiants et des établissements", justification='center', font=('Verdana', 11, 'bold underline'))],
	        [sg.Col(aff_pref_etudiants(etudiants, pref_etudiants)), sg.VerticalSeparator(), sg.Col(aff_pref_etablissements(etablissements, pref_etablissements)), sg.VerticalSeparator(), sg.Col(aff_capacite(etablissements, capacite))],
	        [sg.HorizontalSeparator(pad=(100, 5))],
	        [sg.T("Algorithme du mariage stable en fonction des etablissements", justification='center', font=('Verdana', 11, 'bold underline'))],
	        [sg.Col(aff_algo_etablissements(etudiants, pref_etudiants, etablissements, pref_etablissements, trace_etu))],
	        [sg.HorizontalSeparator(pad=(100, 5))],
	        [sg.T("Résultats", justification='center', font=('Verdana', 11, 'bold underline'))],
	        [sg.Col(aff_resultat(trace_etu, etudiants))],
	        [sg.HorizontalSeparator(pad=(100, 5))],
	        [sg.T("Satisfactions", justification='center', font=('Verdana', 11, 'bold underline'))],
	        [sg.Col(aff_satis_etudiants1(trace_etu, etudiants, pref_etudiants)), sg.VerticalSeparator(), sg.Col(aff_satis_etablissements1(trace_etu, etablissements, pref_etablissements))],
	    	[sg.HorizontalSeparator(pad=(100, 5))],
	    	[sg.HorizontalSeparator(pad=(30, 5))],
	    	[sg.HorizontalSeparator(pad=(100, 5))],
	    	[sg.T("Algorithme du mariage stable en fonction des etudiants", justification='center', font=('Verdana', 11, 'bold underline'))],
	        [sg.Col(aff_algo_etudiants(etudiants, pref_etudiants, etablissements, pref_etablissements, trace_eta))],
	        [sg.HorizontalSeparator(pad=(100, 5))],
	        [sg.T("Résultats", justification='center', font=('Verdana', 11, 'bold underline'))],
	        [sg.Col(aff_resultat(trace_eta, etablissements))],
	        [sg.HorizontalSeparator(pad=(100, 5))],
	        [sg.T("Satisfactions", justification='center', font=('Verdana', 11, 'bold underline'))],
	        [sg.Col(aff_satis_etudiants2(trace_eta, etudiants, pref_etudiants)), sg.VerticalSeparator(), sg.Col(aff_satis_etablissements2(trace_eta, etablissements, pref_etablissements))],
	    	[sg.HorizontalSeparator(pad=(100, 5))],
	        [sg.T("Satisfactions en fonction des etablissements", justification='center', font=('Verdana', 11, 'bold underline'))],
	        [sg.Col(aff_satis_etudiants1(trace_etu, etudiants, pref_etudiants)), sg.VerticalSeparator(), sg.Col(aff_satis_etablissements1(trace_etu, etablissements, pref_etablissements))],
	    ], scrollable=True, vertical_scroll_only=True, size=(None, longeur))]]

	window = sg.Window('Outil D\'integration', affichage, size=(largeur, longeur), element_justification='c', resizable=True, finalize=True)

	while True:
	    event, values = window.read()
	    if event == sg.WIN_CLOSED or event == "Exit":
	        break
	    
	window.close()



