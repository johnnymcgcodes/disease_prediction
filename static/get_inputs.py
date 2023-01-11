input_array = [0]*21


def get_inputs():
    # HighBP, HighChol, CholCheck, BMI, Smoker = 0, 0, 0, 0, 0
    # Stroke, HeartD, PhysActivity, Fruits, Veggies = 0, 0, 0, 0, 0
    # HvyAlcoholConsump, AnyHealthcare, NoDoctor, GenHlth, MentHlth = 0, 0, 0, 0, 0
    # PhysHlth, DiffWalk, Sex, Age, Education, Income = 0, 0, 0, 0, 0, 0

    while True:
        try:
            print("High Blood Pressure?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[0] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue


    while True:
        try:
            print("High Cholesterol?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[1] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Have you had Cholesterol checked in 5 years")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[2] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Enter BMI")
            entry = int(input("Enter an integer between 10 and 60"))
            if not 10.0 <= entry <= 60.0:
                raise ValueError()
            input_array[3] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer between 10 and 60 only...")
            continue

    while True:
        try:
            print("Are you a smoker?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[4] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Have you had a stroke before")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[5] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Have you had heart disease or a heart attack before?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[6] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Do you engage in weekly physical activity or more?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[7] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue


    while True:
        try:
            print("Do you eat fruits at least once a week?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[8] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Do you eat veggies at least once a week?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[9] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Are you a heavy drinker ?")
            print("adult men: more than 14 drinks per week )")
            print("adult women: more than 7 drinks per week )")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[10] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue
    while True:
        try:
            print("Do you have any healthcare at all?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[11] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Do you not have care or a doctor because you can't afford one?")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[12] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Enter overall health ranking")
            print("1 being completely healthy-excellent")
            print("5 having the poorest health")
            entry = int(input("Enter an integer between 1 and 5"))
            if not 1.0 <= entry <= 5.0:
                raise ValueError()
            input_array[13] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer between 1 and 5 only...")
            continue

    while True:
        try:
            print("Enter amount of days each month where mental health was challenging")
            print("0 being no challenging days")
            print("30 being all days were challenging")
            entry = int(input("Enter an integer between 0 and 30"))
            if not 0.0 <= entry <= 30.0:
                raise ValueError()
            input_array[14] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer between 0 and 30 only...")
            continue

    while True:
        try:
            print("Enter amount of days each month where physical health was challenging")
            print("0 being no challenging days")
            print("30 being all days were challenging")
            entry = int(input("Enter an integer between 0 and 30"))
            if not 0.0 <= entry <= 30.0:
                raise ValueError()
            input_array[15] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer between 0 and 30 only...")
            continue

    while True:
        try:
            print("Do you have difficulty walking")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[16] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Please enter 0 for female, 1 for male")
            entry = int(input("Enter an integer 1 for yes, 0 for no: "))
            if not 0.0 <= entry <= 1.0:
                raise ValueError()
            input_array[17] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer 1 or 0 only...")
            continue

    while True:
        try:
            print("Please enter age")
            entry = int(input("Enter an integer between 18 and 100"))
            age = 18
            if entry < 25:
                age = 1
            elif 25 <= entry < 30:
                age = 2
            elif 30 <= entry < 35:
                age = 3
            elif 35 <= entry < 40:
                age = 4
            elif 40 <= entry < 45:
                age = 5
            elif 45 <= entry < 50:
                age = 6
            elif 50 <= entry < 55:
                age = 7
            elif 55 <= entry < 60:
                age = 8
            elif 60 <= entry < 65:
                age = 9
            elif 65 <= entry < 70:
                age = 10
            elif 70 <= entry:
                age = 11

            if not 18.0 <= entry <= 130.0:
                raise ValueError()
            input_array[18] = age
            print("entry:", entry)
            break
        except ValueError:
            print("Please input integer between 18 and 120 only...")
            continue

    while True:
        try:
            print("Please enter education level")
            print("1: Never attended school")
            print("2: Finished grade school.")
            print("3: Attended high school, but did not finish.")
            print("4: Finished high school.")
            print("5: Attended college, but did not finish.")
            print("6: Finished 4 year college degree or more")

            entry = int(input("Enter an integer between 1 and 6:"))
            if not 1.0 <= entry <= 6.0:
                raise ValueError()
            input_array[19] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input an integer between 1 and 6 only")
            continue

    while True:
        try:
            print("Please enter income level")
            print("1: Less than 10,000, enter 1")
            print("2: Between $10,000 and less than $20,000, enter 2")
            print("3: Between $20,000 and less than $30,000, enter 3")
            print("4: Between $30,000 and less than $40,000, enter 4")
            print("5: Between $40,000 and less than $50,000, enter 5")
            print("6: Between $50,000 and less than $60,000, , enter 6")
            print("7: Between $60,000 and less than $75,000, , enter 7")
            print("8: $75,000 or more, enter 8")

            entry = int(input("Enter an integer between 1 and 8:"))
            if not 1.0 <= entry <= 8.0:
                raise ValueError()
            input_array[20] = entry
            print("entry:", entry)
            break
        except ValueError:
            print("Please input an integer between 1 and 8 only")
            continue
    print(input_array)
    return input_array


get_inputs()
