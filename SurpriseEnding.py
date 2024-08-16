def surpriseEnding():    
    with open('GuestList.txt', 'r') as file:
        attendees = file.readlines()
        numberOfAttendees = len(attendees)
    
    print(f'''
  ...     _M_
 /( )\    ( )
/ / \ \  / : \\
~~\%/~~  \|:|/
 /   \    |||
/,,,,,\   ||| 
          
Wow, Meg and Mike, congratulations on your special day, lets see, you had so many loving people at your wedding, a total of {numberOfAttendees} people!
That truly is amazing that so many people could be here on your special day!         
    ''')