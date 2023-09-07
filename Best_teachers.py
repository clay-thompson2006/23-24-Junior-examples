def Teacher_question() :
    Teacher1 = input("please enter your favorite teacher. ")
   

   
    Teacher2 = input("please enter your next favorite teacher. ")
   

   
    #print(Teacher1)
   
    #print(Teacher2)
   

   
    if Teacher1 == "sekol" and Teacher2 == "bionci" :
   
        print(f"you are correct both {Teacher1} and {Teacher2} Are great")
   
    elif Teacher1 != "sekol" and Teacher2 == "sekol":
   
        print("answer is wrong")
   
    elif Teacher1 == "wright" or Teacher2 == "wright":
        print("-5000 points from your grade")