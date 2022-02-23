def enter_choise():
    """ Show list of choices ant return number of choice"""
#    print()
    print('\nFor view dates enter 1')
    print('For view all notes enter 2')
    print('For view all dates with separated notes enter 3')
    print('For add new note enter 4')
    print('For delete all notes of date enter 5')
    print('For delete note by number of selected date enter 6')
    print('To exit enter 0')
    return input("Enter you choice: ")
notes = {'01-01-2023' : [{"num" : 1,
                         "task" : "Great all with NY",
                         "prior" : "4"},
                        {"num" : 2,
                        "task" : "Open new calendar",
                        "prior" : "2"} ,
                        {"num": 3,
                         "task" : "Sleep to 11 a.m",
                         "prior": "1"}],
         '31-08-2023' : [{"num" : 1,
                         "task" : "Prepare to 1st September",
                         "prior" : "5"}],
         '24-12-2023' : [{"num" : 1,
                         "task" : "Prepare presents",
                         "prior" : "5"},
                        {"num" : 2,
                         "task" : "Buy newyear tree",
                         "prior" : "3"},
                        {"num": 3,
                         "task" : "Test, test",
                         "prior" : "3"}]}


choice = enter_choise()
while choice != '0':

    if choice == '1':
        for n in notes.keys():
          print(n)

    elif choice == '2':
        for n in notes.keys():
            for tasks in notes[n]:
                print (tasks["task"])

    elif choice == '3':
        for n in notes.keys():
            print(f"\n{n}")
            for tasks in notes[n]:
                print (f'Task {tasks ["num"]} : {tasks["task"]}')

    elif choice == '4':
        date = input('Enter date: ')
        new_note = input('Enter your note: ')
        priority = input('Enter priority: ')
        if date in notes.keys():
            notes[date].append({"num" : len(notes[date]), "task" : new_note, "prior" : priority})
        else:
            notes[date] = list()
            notes[date].append({"num" : len(notes[date]),"task" : new_note, "prior" : priority})

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
                notes[date].pop(number_note-1)
        else:
            print(f'Cannot found date: {date}')
    else:
        pass
    choice = enter_choise()
print('Good bye!')