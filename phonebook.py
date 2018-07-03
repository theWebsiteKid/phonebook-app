menu = '''
Electronic Phone Book
=====================
1. Look up an entry
2. Create an entry
3. Delete an entry
4. List all entries
5. Quit
'''

phonebook = {
    'Igor': '4045551111',
    'Roy': '4045552222',
    'Chance': '4045553333'
}

def run_phonebook():
    print menu
    option = raw_input('What do you want to do (1-5)?: ')
    if option in menu_options:
        menu_option = menu_options[option]
        print menu_option()
    else:
        print 'Invalid selection, try again'
    return option != '5'

def find_contact():
    name = raw_input('Enter name: ')
    if name in phonebook:
        return phonebook[name]
    else:
        return 'no entries found'

def make_contact():
    name = raw_input('Enter name: ')
    phone = raw_input('Enter phone #: ')
    phonebook[name] = phone
    print "Added %s" % phonebook[name]
    return phonebook

def delete_contact():
    name = raw_input('Enter name: ')
    print "Deleted %s" % phonebook[name]
    del phonebook[name]
    return phonebook

def list_contacts():
    print "All contacts:"
    return phonebook

def goodbye():
    return 'Later alligator!'

menu_options = {
    '1': find_contact,
    '2': make_contact,
    '3': delete_contact,
    '4': list_contacts,
    '5': goodbye
}

keep_running = True
while keep_running:
    keep_running = run_phonebook()