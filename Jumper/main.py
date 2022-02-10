from Game.Directory import Director
running_state = True
while running_state:
    director = Director()
    director.start_game()


    while True:
        choice = input('\nWould you like to play again? Y/N ').upper()
        if choice == 'Y' or choice == 'YES':
            break
        elif choice == 'N' or choice == 'NO':
            running_state = False
            break
        else:
            print('\nEnter a valid input...')
