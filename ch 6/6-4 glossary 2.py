programming_glossary = {
    '.lstrip()': "removes all left side spaces",
    'new_list = list[:]': "copies whole list",
    'print(list[5:20])': "prints out all indecies in the list from index 5 to 20",
    'del list[5]': "deletes value of index 5",
    '.upper()': "turns whole string into upper letters"
    }

for concept in programming_glossary:
    print(f"{concept} {programming_glossary[concept]}\n")

programming_glossary['.items()'] = 'selects all the things in a dictonary'
programming_glossary['.values()'] = 'selects the values of the dictonary'
programming_glossary['.keys()'] = 'selects the keys of the dictonary'
programming_glossary['set(dictonary)'] = 'turns the dictonary into a set'
programming_glossary['.rstrip()'] = 'removes all right hand spaces'

for concept in programming_glossary:
    print(f"{concept} {programming_glossary[concept]}\n")