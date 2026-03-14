#fee calculator

def calculate_fee(course,marks):
    if course == "AI":
        fee = 50000
    elif course == "web":
        fee = 30000
    elif course == "Data science":
        fee = 30000
    else:
        return none #Invalid course
    #discount condition
    if marks > 90:
        fee -= 5000
    return fee

def main():
    course = input("Enter course:")
    marks = int(input("Enter marks:"))

    fee = calculate_fee(course,marks)

    if fee is None:
        print("Invalid course selected")
    else:
        print("Final fee:",fee)

main()
