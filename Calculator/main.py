# Working with tuples and calculations for a grade calculator
from pyscript import display, document

# Grades Form
def gradesform(e):
    document.getElementById("output").innerHTML = ""  # clearing the output field
    document.getElementById("output2").innerHTML = ""  # clearing the output field
    document.getElementById("output3").innerHTML = ""  # clearing the output field

    # Read inputs first
    English = float(document.getElementById("English_score").value or 0)
    Science = float(document.getElementById("Science_score").value or 0)
    Math = float(document.getElementById("Math_score").value or 0)
    WL = float(document.getElementById("WL_score").value or 0)
    AE = float(document.getElementById("AE_score").value or 0)
    ML = float(document.getElementById("ML_score").value or 0)

    Firstname = document.getElementById("name_F").value
    Lastname = document.getElementById("name_L").value

    # Subject Units and Scores
    Units = (5, 5, 5, 3, 1, 2)
    Subjects = (English, Science, Math, WL, AE, ML)

    # Calculate weighted scores using correct indexing
    English_fin = Subjects[0] * Units[0]
    Science_fin = Subjects[1] * Units[1]
    Math_fin = Subjects[2] * Units[2]
    WL_fin = Subjects[3] * Units[3]
    AE_fin = Subjects[4] * Units[4]
    ML_fin = Subjects[5] * Units[5]

    total = (English_fin + Science_fin + Math_fin + WL_fin + AE_fin + ML_fin) / sum(Units)

    # Validating if they completed the input field
    if not Firstname or not Lastname:
        display("Please fill out personal details", target="output")
        return

    if (English + Science + AE + Math + ML + WL) == 0:
        display("Fill grades in", target="output")
        return

    # Displays
    display(
        f"Hello, {Firstname} {Lastname}! Your total grade average is: {round(total, 2)}",
        target="output"
    )
    display(
        f"Here are your scores: Science: {Science}; English: {English}; Math: {Math}; World Literature: {WL}; Artistic Expression: {AE}; Media Literacy: {ML}",
        target="output2"
    )
    
    #if statement for pass or fail

    if round(total, 2) >= 75: #if statement
        display(f'You passed!', target='output3')
    else: # else statement
        display(f'You failed.', target='output3')
