# Working with dictionaries for a club information display
from pyscript import display, document


def English(e):
    document.getElementById('club_information').innerHTML = "" # Clearing field

    English = {
    'Club Name': 'English Club',
    'Description': 'is a club that helps students improve their English skills',
    'Meeting time': '3:00 PM - 4:00 PM',
    'Location': 'Room 701',
    'Club Moderator': 'Ms. Smith',
    'Number of Members': 25
 
        } # Dictionary for English Club
        
    message = (f"The {English['Club Name']} {English['Description']}. "
               f"Our moderator is {English['Club Moderator']}, and "
               f"the meeting time is {English['Meeting time']} at {English['Location']}. "
               f"We stand at {English['Number of Members']} members.") # message template
    display(message, target='club_information') #Displaying to first output


def Math(e):
    document.getElementById('club_information').innerHTML = "" # Clearing field

    Math = {
    'Club Name': 'Math Club',
    'Description': 'is a club that guides students to learn advanced Math',
    'Meeting time': '2:00 PM - 3:30 PM',
    'Location': 'Room 705',
    'Club Moderator': 'Ms. DJ',
    'Number of Members': 5

        } # Dictionary for Math Club
    
    message = (f"The {Math['Club Name']} {Math['Description']}. "
               f"Our moderator is {Math['Club Moderator']}, and "
               f"the meeting time is {Math['Meeting time']} at {Math['Location']}. "
               f"We stand at {Math['Number of Members']} members.") # message template
    display(message, target='club_information') # Displaying output


def SocSci(e):
    document.getElementById('club_information').innerHTML = "" # Clearing field

    socsci = {
        'Club Name': 'Social Sciences Club',
        'Description': 'is a club that teaches students about social issues',
        'Meeting time': '2:00 PM - 4:00 PM',
        'Location': 'Room 405',
        'Club Moderator': 'Ms. Tanny',
        'Number of Members': 30

        }  # Dictionary for SocSci Club

    message = (f"The {socsci['Club Name']} {socsci['Description']}. "
               f"Our moderator is {socsci['Club Moderator']}, and "
               f"the meeting time is {socsci['Meeting time']} at {socsci['Location']}. "
               f"We stand at {socsci['Number of Members']} members.") #Message Format
    display(message, target='club_information') #For Display

def Literature(e):
    document.getElementById('club_information').innerHTML = "" # Clearing field

    literature = {
        'Club Name': 'Literature Club',
        'Description': 'is a club that exposes students to diverse types of literature',
        'Meeting time': '2:15 PM - 4:30 PM',
        'Location': 'the Library',
        'Club Moderator': 'Mr. Gervy',
        'Number of Members': 32

        }  # Dictionary for Basketball Varsity

    message = (f"The {literature['Club Name']} {literature['Description']}. "
               f"Our moderator is {literature['Club Moderator']}, and "
               f"the meeting time is {literature['Meeting time']} at {literature['Location']}. "
               f"We stand at {literature['Number of Members']} members.") #Message Format
    display(message, target='club_information') #For Display



