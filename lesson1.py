def enter_choise():
    print()
    print('For view dates enter 1')
    print('For view all notes enter 2')
    print('For view all dates with separated notes enter 3')
    print('For add new note enter 4')
    print('For delete all notes of date enter 5')
    print('For delete note by number of selected date enter 6')
    print('To exit enter 0')

notes = {'01.01.2023' : ["Great all with NY",
                         "Open new calendar",
                         "Sleep to 11 a.m"],
         '31.08.2023' : ["Prepare to 1st September"],
         '24.12.2023' : ["Prepare presents",
                         "Buy newyear tree",
                         "Test, test"]}

choice = '1'
enter_choise()
while choice != '0':
    choice = input("Enter you choice: ")
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
                print(f"{notes[n].index(r)} : {r}")
            print()
    elif choice == '4':
        date = input('Enter date: ')
        new_note = input('Enter your note: ')
        if date in notes.keys():
            notes[date].append(new_note)
        else:
            notes[date] = list()
            notes[date].append(new_note)
    elif choice == '5':
        date = input('Enter date for delete: ')
        if date in notes.keys():
            del notes[date]
            print(f"All notes for date: {date} deleted")
        else:
            print(f'Cannot found date: {date}')
    elif choice == '6':
        date = input('Enter date for delete: ')
        if date in notes.keys():
            number_note = int(input("Please enter number (can see by option '3') note for deleting: "))
            if date in notes.keys() and number_note < len(notes[date]) and number_note >= 0 :
                notes[date].pop(number_note)
        else:
            print(f'Cannot found date: {date}')
    else:
        pass
    enter_choise()
print('Good bye!')