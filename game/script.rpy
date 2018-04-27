#INIT

image bg credits:
    "credit.png"
    size (1280,720)
image bg unavailable:
    "unavailable.png"
    size (1280,720)
image bg test:
    "testbg.png"
    size (1280,720)
define e = Character("Eileen")


#Game Start Menu
label start:
    
    menu yearSelect:
        "Which year's resources would you like to access?"
        
        "JC1":
            menu topic:
                "Which topic would you like to play the resources for?"
                
                "Environment":
                    call unavailable
                
                "Arts":
                    call arts
                    
                "Media":
                    call unavailable
                    
                "Ethics":
                    call unavailable
                    
                "Play all":
                    call environment
                    call arts
                    call media
                    call ethics
                    
                "Exit to Year Select":
                    call yearSelect
            
        "JC2":
            call unavailable
            
        "Credits":
            call credit
        
        "Quit to Home Screen":
            return


#Environment
label environment:
    
    return

#Arts
label arts:
    
    return
    
#Media
label media:
    
    return

#Ethics
label ethics:
    
    return

#Unavailable
label unavailable:
    
    show bg unavailable
    pause
    hide bg unavailable
    return
    
#Credits
label credit:
    
    show bg credits
    pause
    hide bg credits
    
    return
