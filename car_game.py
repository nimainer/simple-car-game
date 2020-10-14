print("""
start - if you want to start the car
stop - if you want to stop the car
quit - if your wanna leave the game
help - if you forget the command's
""")

while True:
    command = (input("what do you want to do: ")).lower()

    if command == 'start':
        print("car started" )
    elif command == 'stop':
        print("car stopped")
    elif command == 'help':
        print("""
start - if you want to start the car
top - if you want to stop the car
quit - if your wanna leave the game
help - if you forget the command's
        """)

    elif command == 'quit':
        exit()
