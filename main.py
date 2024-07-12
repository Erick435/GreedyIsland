# ============================= INITIALIZE HEALTH ===========================================
player_health = 10


def is_alive():
        if player_health <= 0:
            try_again = input("\n\nYou Are Dead! Try again? (y/n)\n")
            if try_again == "y" or try_again == "Y":
                game_start()
            else:
                print("Thank you for playing...\n")

def game_start():
    print("\nAll passengers boarding flight 209 to Tokyo,Japan, please begin boarding now, we will be leaving shortly.")
    print("\nYou get in line to board your flight and make it inside plane and find your seat, you place your luggage away and sit down.")
    print("\nThe plane begins it's engines and starts to take off")
    print('''
                ______
                _\ _~-\___
        =  = ==(____AA____D
                    \_____\___________________,-~~~~~~~`-.._
                    /     o O o o o o O O o o o o o o O o  |\_
                    `~-.__        ___..----..                  )
                        `---~~\___________/------------`````
                        =  ===(_________D
                        ''')

    print('''
\nAs the plane takes off, you decide to take a nap for a few hours since it will take quite some time to get there. 
You close your eyes and you begin to sleep
        
4 hours later...
        
You wake up, still a little drowsy, but you have the urge to use the bathroom. You look at the seat in front of you
and there's a screen on the seat that you can use. You check how much longer until you reach your destination, it's
still more than 4 hours.
        
Do you...

1) Get up to use the bathroom
2) Hold it and go back to sleep
        
        ''')

        # Decision 1
        
    wake_up_action = input()



    # ============================= GET UP TO USE THE BATHROOM =======================================
    if wake_up_action == 1:
        print('''
                You unbuckle your seatbelt, get up and walk towards the bathroom and get inside.
                Suddenly you feel a strong turbulence and you can feel the plane move abnormally
                to the left and the right. You try to hang on to something but fail and hit your head on
                the corner of of a locked cabinet.
                
                - 2 health points (8 health points remaining)
                
                


            ''')
        
    player_health -= 10
    
    is_alive()
    
    
game_start()