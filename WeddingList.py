from SurpriseEnding import surpriseEnding

def main():
    welcomeBanner()
    while True:
        gatherGuestNames()

        ending = input('Wow, thats alot of you, are you ready for the big surprise? \n').lower()
        if ending == 'yes':
            break
        elif ending == 'no':
            gatherGuestNames()
            break

    surpriseEnding() 

def gatherGuestNames():
    
    with open('GuestList.txt', 'a') as file:
        while True:
            guestName = input('Please register your attendance: ').title()

            if guestName.lower() == 'exit':
                break

            file.write(guestName + '\n')
            print(f"Thank you {guestName}, you have been added to the list :)")


def welcomeBanner():
    print('''
Welcome to the wedding of the century! Today we celebrate
                      ___            _ _        
  /\/\   ___  __ _   ( _ )     /\/\ (_) | _____ 
 /    \ / _ \/ _` |  / _ \/\  /    \| | |/ / _ \\
/ /\/\ \  __/ (_| | | (_>  < / /\/\ \ |   <  __/
\/    \/\___|\__, |  \___/\/ \/    \/_|_|\_\___|
             |___/                              
          
Please join us by filling in your name and then there will be a super fun suprise at the end!         
          ''')

main()