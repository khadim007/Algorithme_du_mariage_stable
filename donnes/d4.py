effectifs = 4
capacite = [1,1,1,1]
etudiants = ['e1', 'e2', 'e3', 'e4']
etablissements = ['s1', 's2', 's3', 's4']
pref_etudiants = {
    'e1': ['s4', 's1', 's3', 's2'],
    'e2': ['s1', 's4', 's2', 's3'],
    'e3': ['s1', 's3', 's2', 's4'],
    'e4': ['s3', 's1', 's2', 's4']
}
pref_etablissements = {
    's1': ['e2', 'e1', 'e4', 'e3'],
    's2': ['e2', 'e1', 'e3', 'e4'],
    's3': ['e3', 'e4', 'e2', 'e1'],
    's4': ['e4', 'e3', 'e1', 'e2']
}