notes = {'01.01.2023' : ["Great all with NY",
                         "Open new calendar",
                         "Sleep to 11 a.m"],
         '31.08.2023' : ["Prepare to 1st September"],
         '24.12.2023' : ["Prepare presents",
                         "Buy newyear tree",
                         "Test, test"]}
# print (notes['01.01.2023'])
choice = '1'
print('For view dates enter 1')
print('For view all notes enter 2')
print('For view all dates with separated notes enter 3')
print('For add new note enter 4')
print('For delete all notes of date enter 5')
while choice != '0':
    choice = input("Enter you choice:")
    if choice == '1':
        for n in notes.keys():
          print(n)
    elif choice == '2':
        for n in notes.keys():
          print(notes[n])
    elif choice == '3':
        for n in notes.keys():
            print(n)
            for r in notes[n]:
                print(r)
            print()
    elif choice == '4':
        date = input('Enter date:')
        new_note = input('Enter your note:')
        if date in notes.keys():
            notes[date].append(new_note)
        else:
            notes[date] = list()
            notes[date].append(new_note)
    elif choice == '5':
        date = input('Enter date for delete:')
        if date in notes.keys():
            del notes[date]
        else:
            pass
    else:
        pass
print('Good bye!')