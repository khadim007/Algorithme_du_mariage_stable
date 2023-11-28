effectifs = 5
capacite = [1,1,1,1,1]
etudiants = ['e1', 'e2', 'e3', 'e4', 'e5']
etablissements = ['s1', 's2', 's3', 's4', 's5']
pref_etudiants = {
    'e1': ['s5', 's1', 's2', 's4', 's3'],
    'e2': ['s3', 's1', 's5', 's4', 's2'],
    'e3': ['s5', 's3', 's1', 's2', 's4'],
    'e4': ['s3', 's4', 's2', 's1', 's5'],
    'e5': ['s5', 's3', 's1', 's4', 's2']
}
pref_etablissements = {
    's1': ['e5', 'e1', 'e4', 'e2', 'e3'],
    's2': ['e3', 'e2', 'e4', 'e1', 'e5'],
    's3': ['e4', 'e1', 'e2', 'e3', 'e5'],
    's4': ['e2', 'e4', 'e3', 'e5', 'e1'],
    's5': ['e5', 'e2', 'e3', 'e1', 'e4']
}