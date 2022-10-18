patternDict = {'1': 'test_folder1', '2': 'test_folder2', '3': 'test_folder4'}
print('vvidite cifru')
choise = int(input())

if choise == 1:
    print(patternDict['1'])
if choise == 2:
    print(patternDict['2'])
if choise == 3:
    print(patternDict['3'])
if choise == 4:
    None

a = {
    'Buildings': ['assets-env\Props\Buildings', 'MaterialSubstance'],
    'Landmark': ['assets-env\Props\Landmark', 'assets-env\SubstanceSharedPresets'],
    'Stuff': ['assets-env\Props\Misc', 'assets-env\SubstanceSharedPresets'],
    'Roads': ['assets-env\Props\Roads', 'assets-env\SubstanceSharedPresets'],
    'Rocks': ['assets-env\Props\Rocks', 'assets-env\SubstanceSharedPresets'],
    'Vehicles': ['assets-env\Props\Vehicles', 'assets-env\SubstanceSharedPresets'],
    'Materials': ['assets-env\MaterialLibrary', 'assets-env\MaterialSubstance', 'assets-env\SubstanceSharedPresets'],
    'Vegetation': ['assets-env\Vegetation'],
    'Tutorial': ['assets-env\Props\Misc\Tutorial'],
    'Houdini': ['assets-env\Houdini'],
    'Gameplay': ['assets-env\Gameplay']
}
