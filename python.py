
user_wants_workout = True
while user_wants_workout: 
        
    username = input("What's your fitness power song?: ")
    # print( "Welcome " + username + " how are you?" ) # Number 2 choice
    # print (f"Welcome {username} how are you?") # Recommended
    print(f"\nGet ready to pump up the volume and pump some iron to the beat of {username}!\n\nYour fitness journey just got a soundtrack, and we're here to help you lift to the beat.\n\nRemember, at Fitplan, we don't just break a sweat; we break records and bad dance moves! Let's groove our way to a fitter you!\n")
    age = int( input("Enter your age: "))
    if age > 15:
        print("\nCongratulations! You are old enough to unlock the secrets of the universe.") 
        print("\nJust kidding! You're not that old, but you're definitely wise beyond your years!")
    else:
        print("\nAh, you're still young! Enjoy this age while it lasts. It's the only time when you can eat all the candy and blame it on being a kid!")
    weight = int(input ("\nEnter your weight in LBS: "))
    fitness_level = int( input ("\nOn a scale from 1 to 3, with 3 being the most fit and 1 being the least fit: \n\nHow would you rate your fitness level?: ") )

    while fitness_level not in [ 1, 2, 3 ]:
        fitness_level = int( input ("Silly, please enter 1, 2 or 3. Don't mess up this time!!!!!!: " ) )


    # fitness_level = int( fitness_level ) #optional

    if fitness_level == 1:
        print("\nYou rated your fitness level as 1 (low).")
    elif fitness_level == 2:
        print("\nYou rated your fitness level as 2 (moderate).")
    elif fitness_level == 3:
        print("\nYou rated your fitness level as 3 (high).")
    # else:
    #     print("Error: Invalid input. Please enter a number between 1 and 3.")
        
    fitness_goal= int(input("\nWhat is your fitness goal using numbers 1, 2, and 3:\n\n1. Bulk\n2. Cut\n3. Endurance\n\nEnter your response: "))
    if fitness_goal == 1:
        print("\nAh, aiming to bulk up, I see! Get ready to turn heads at the beach.")
        print("\nThe most important thing is to stay consistent and have fun with your workouts!")
        bulk_amount = int(input("\nHow many pounds of Hulk-like power are you looking to unleash?: "))
        print(f"\n{bulk_amount} pounds of Hulk-like power!\n\nGet ready to transform from mild-mannered human to unstoppable force of nature.")
        bulk_precentage = (bulk_amount / weight) * 100 
        round_bulk_precentage = round(bulk_precentage, 2) 
        print(f"\nYou are looking to add {round_bulk_precentage} % of hulk muscle!")
        
        while round_bulk_precentage > 49:
                print("\nAh, the 'Incredible Hulk Transformation' class, you say? \n\nWhile we appreciate your enthusiasm for bulking up like a superhero, our app doesn't offer this. We recommend starting at a lower goal to start")
                round_bulk_precentage = int(input("\nHow many pounds of Hulk-like power are you looking to unleash?: "))
                
        if round_bulk_precentage < 21: 
            print("\nCongratulations! You have been recommended the 'Laid-back Legend' bulk course.\n\nThis is our low intensity workout plan.\n\nGet ready to sculpt your physique with the energy of a sloth on a Sunday afternoon - unhurried but absolutely effective!")
            print("\nDay 1 Legend Workout:\n\nBodyweight squats: 3 sets x 12 - 15 reps.\nPushups: 3 sets x 10 - 12 reps.\nDumbell Rows: 3 sets x 12 - 15 reps.\nDumbell Shoulder Press: 3 sets x 12 - 15 reps.") 
            print("\nDay 2 Legend Workout:\n\nRest or Light Cardio.\nEngage in light cardio such as biking, walking, or jogging. ")
            print("\nDay 3 Legend Workout:\n\nBody Weight Lunges: 3 sets x 12 - 15 reps.\nDumbell Bench Press: 3 sets x 12 - 15 reps.\nDumbell bicep curls 3 sets 12 - 15 reps.\nTricep Dips: 3 sets x 10 - 12 reps.")
            print("\nDay 4 Legend Workout:\n\nRest or Light Cardio.Engage in light cardio and mobility.")
            print("\nDay 5 Legend Workout:\n\nBodyweight Glute Bridges: 3 sets x 12 - 15 reps.\nDumbell Lateral Raises: 3 sets x 12-15 reps.\nPlank: 3 sets x 30-50 seconds hold.\nDumbell Hammer Curls: 3 sets x 12 - 15 reps.")
            print("\nRemember to progressively increase the weights as you get stronger, and ensure you're consuming enough calories and protein to support your bulking goals.")
            
                
            
        elif round_bulk_precentage < 36:
            print("\nCongratulations! You have been recommended the 'Casual Crusader' bulk course.\n\nThis is our medium intensity workout plan.\n\nYou'll achieve your goals with the intensity of a caffeinated sloth - purposeful yet unhurried.")    
            print("\nDay 1 Casual Crusader Workout:\n\nBarbell Bench Press: 4 sets x 8-10 reps.\nIncline Dumbbell Press: 3 sets x 10-12 reps.\nIncline Dumbbell Press: 3 sets x 10-12 reps.\nDumbbell Lateral Raises: 3 sets x 12-15 reps.\nTricep Dips: 4 sets x 10-12 reps.\nTricep Rope Pushdown: 3 sets x 12-15 reps.")
            print("\nDay 2 Casual Crusader Workout:\n\nSquats: 4 sets x 8-10 reps.\nDeadlifts: 3 sets x 8-10 reps.\nLeg Press: 3 sets x 10-12 reps.\nLunges: 3 sets x 12-15 reps per leg.\nLeg Curls: 3 sets x 12-15 reps.\nStanding Calf Raises: 4 sets x 15-20 reps.")
            print("\nDay 3 Casual Crusader Workout:\n\nRest or Active Recovery.")
            print("\nDay 4 Casual Crusader Workout:\n\nBarbell Rows: 4 sets x 8-10 reps.\nLat Pulldown: 3 sets x 10-12 reps.\nFace Pulls: 3 sets x 12-15 reps.\nBarbell or Dumbbell Curls: 4 sets x 10-12 reps.\nHammer Curls: 3 sets x 12-15 reps.\nSeated Rows: 3 sets x 10-12 reps.")
            print("\nDay 5 Casual Crusader Workout:\n\nSeated Dumbbell Press: 4 sets x 8-10 reps.\nDumbbell Lateral Raises: 3 sets x 12-15 reps.\nFront Plate Raises: 3 sets x 12-15 reps.\nShrugs: 4 sets x 10-12 reps.\nUpright Rows: 3 sets x 10-12 reps.")
            print("\nDay 6 Casual Crusader Workout:\n\nActive Recovery or Cardio.")
            print("\nRemember to progressively increase the weights as you get stronger, and ensure you're consuming enough calories and protein to support your bulking goals.")
        elif round_bulk_precentage < 49:
            print("\nCongratulations! You have been recommended the 'Beast Mode Brigade' bulk course.\n\nThis is our high intensity workout plan.\n\nIt's not just a workout; it's a battle.\n\nRemember pain is just weakness leaving the body!") 
            print("\nDay 1 Beast Mode Brigade Workout:\n\nBarbell Bench Press: 4 sets x 6-8 reps.\nIncline Dumbbell Press: 3 sets x 8-10 reps.\nWeighted Dips: 3 sets x 8-10 reps.\nStanding Military Press: 4 sets x 6-8 reps.\nLateral Raise Drop Sets: 3 sets x 12-15 reps (start heavy, drop weight, repeat).")
            print("\nDay 2 Beast Mode Brigade Workout:\n\nBack Squats: 4 sets x 6-8 reps.\nRomanian Deadlifts: 3 sets x 8-10 reps.\nFront Squats: 3 sets x 8-10 reps.\nWalking Lunges with Dumbbells: 3 sets x 12-15 reps per leg.\nLeg Press: 4 sets x 10-12 reps.") 
            print("\nDay 3 Beast Mode Brigade Workout:\n\nRest or Active Recovery.") 
            print("\nDay 4 Beast Mode Brigade Workout:\n\nDeadlifts: 4 sets x 6-8 reps.\nBent Over Barbell Rows: 3 sets x 8-10 reps.\nPull-Ups: 3 sets x 8-10 reps.\nBarbell Curl: 4 sets x 6-8 reps.\nAlternating Dumbbell Hammer Curls: 3 sets x 10-12 reps per arm.")
            print("\nDay 5 Beast Mode Brigade Workout:\n\nSeated Dumbbell Press: 4 sets x 6-8 reps.\nArnold Press: 3 sets x 8-10 reps.\nFace Pulls: 3 sets x 12-15 reps.\nDumbbell Shrugs: 4 sets x 10-12 reps.\nUpright Rows: 3 sets x 8-10 reps.")
            print("\nDay 6 Beast Mode Brigade Workout:\n\nActive Recovery or Cardio.")
            print("\nRemember to progressively increase the weights as you get stronger, and ensure you're consuming enough calories and protein to support your bulking goals.")

        else: 
            print("\nAh, the 'Incredible Hulk Transformation' class, you say?\n\nWhile we appreciate your enthusiasm for bulking up like a superhero, our app doesn't offer this. We recommend starting at a lower goal to start")
        


        
    elif fitness_goal == 2:
        print("\nGoing for the cut, huh? Get ready to shed those pounds and reveal those hidden muscles!")
        print("\nKeep working hard and stay motivated. You got this!")
        cut_amount = int(input("\nHow many pounds of excess fluff are we trimming today?: "))
        print(f"\nAiming to shed {cut_amount} pounds of excess fluff, eh?\n\nWith each pound, you're not just cutting; you're sculpting a work of art.\n\nSay goodbye to fluff and hello to fabulous!")
        cut_precentage = (cut_amount / weight) * 100  
        roundcut_precentage = round(cut_precentage, 2)
        print(f"\nYou are looking to lose {roundcut_precentage} % of fluff!")
        if roundcut_precentage < 21:
            print("Congratulations! You have been recommended the 'Easy Breezy Body Trim' cut course.\n\nThis is a low intensity workout plan.\n\n It's so easy your pet hamster could do it!")
            print("\nDay 1 Easy Breezy Body Trim Workout:\n\nnBrisk Walking or Light Jogging: 30 minutes.\nBodyweight Squats: 3 sets x 15 reps.\nPlank: 3 sets, hold for 30 seconds each.\nBicycle Crunches: 3 sets x 15 reps per side.\nStretching: 5 minutes.")
            print("\nDay 2 Easy Breezy Body Trim Workout:\n\nBodyweight Lunges: 3 sets x 12 reps per leg.\nPush-Ups: 3 sets x 10-12 reps.\nTricep Dips: 2 sets x 15 reps.\nYoga or Gentle Stretching: 15 minutes. ")
            print("\nDay 3 Easy Breezy Body Trim Workout:\n\nRest or Active Recovery.") 
            print("\nDay 4 Easy Breezy Body Trim Workout:\n\nCycling: 30 minutes.\nJumping Jacks: 3 sets x 30 seconds.\nPlank to Downward Dog: 3 sets x 10 reps.\nRussian Twists: 3 sets x 15 reps per side.\nLight Yoga Flow: 20 minutes.")
            print("\nDay 5 Easy Breezy Body Trim Workout:\n\nWall Sit: 3 sets, hold for 30 seconds each.\nBicep Curls with Light Dumbbells: 3 sets x 12 reps.\nSide Leg Raises: 3 sets x 15 reps per side.\nTricep Kickbacks (using light dumbbells or resistance bands): 2 sets x 15 reps.\nGentle Stretching 15 minutes.")
            print("\nDay 6 Easy Breezy Body Trim Workout:\n\nActive Recovery or Light Cardio.")
            print("\nThis low-intensity workout plan focuses on steady-state cardio, light resistance training, and flexibility exercises to promote weight loss without putting excessive stress on the body. Remember to combine this with a healthy, balanced diet for effective weight cutting. Adjust the intensity and duration based on your fitness level and progress over time.")
        elif roundcut_precentage < 36:
            print("Congratulations! You have been recommended the 'Spicey Shred Squad' cut course.\n\nThis is a medium intensity workout plan where spicey meets sweatiness!")
            print("\nDay 1 Spicey Shred Squad Workout:\n\nRunning or Jogging: 30 minutes.\nBodyweight Squats: 4 sets x 15 reps\nPlank: 3 sets, hold for 45 seconds each\nBicycle Crunches: 3 sets x 20 reps per side.\nJumping Lunges: 3 sets x 15 reps per leg.\nStretching: 5 minutes.")
            print("\nDay 2 Spicey Shred Squad Workout:\n\nGoblet Squats: 4 sets x 12 reps.\nPush-Ups: 3 sets x 12-15 reps.\nBent Over Rows (with light dumbbells): 3 sets x 12 reps\nTricep Dips: 3 sets x 15 reps.\nPlank to Side Plank: 3 sets x 10 reps per side.\nYoga or Gentle Stretching: 15 minutes.")
            print("\nDay 4 Spicey Shred Squad Workout:\n\nRest or Active Recovery.")
            print("\nDay 5 Spicey Shred Squad Workout:\n\nHigh-Intensity Interval Training (HIIT) - Sprinting or Cycling: 30 minutes.\nMountain Climbers: 3 sets x 30 seconds.\nRussian Twists with Medicine Ball: 3 sets x 20 reps per side.\nLeg Raises: 3 sets x 15 reps.\nSide Plank with Hip Dips: 3 sets x 12 reps per side.\nLight Yoga Flow: 20 minutes.")
            print("\nDay 6 Spicey Shred Squad Workout:\n\nActive Recovery or Light Cardio.")
            print("\nThis medium-intensity workout plan combines cardio, resistance training, and core exercises to support weight cutting while preserving muscle mass. Adjust the intensity and duration based on your fitness level and progress over time. Remember to maintain a balanced diet and stay hydrated to support your weight loss goals.")
        elif roundcut_precentage < 49:
            print("Congratulations! You have been recommended the ' Cheetah Chase Challenge' cut course.\n\nThis is a high intensity workout plan.\n\nThis workout plan is designed to make even the fastest creatures on Earth break a sweat!")
            print("\nDay 1 Cheetah Chase Challenge:\n\nBurpees: 4 sets x 15 reps.\nBox Jumps: 3 sets x 12 reps.\nMedicine Ball Slams: 3 sets x 15 reps\nKettlebell Swings: 4 sets x 20 reps.\nPlank to Renegade Rows: 3 sets x 12 reps.\nSprinting (or Jump Rope): 10 minutes.")
            print("\nDay 2 Cheetah Chase Challenge:\n\nPush-Ups: 4 sets x 15 reps.\nPull-Ups or Lat Pulldowns: 3 sets x 12 reps.\nDumbbell Thrusters: 3 sets x 15 reps.\nBattle Ropes: 4 sets x 30 seconds.\nHanging Leg Raises: 3 sets x 15 reps.\nRowing Machine: 10 minutes.")
            print("\nDay 3 Cheetah Chase Challenge:\n\nRest or Active Recovery.")
            print("\nDay 4 Cheetah Chase Challenge:\n\nJump Squats: 4 sets x 15 reps.\nBulgarian Split Squats: 3 sets x 12 reps per leg.\nExplosive Step-Ups: 3 sets x 15 reps per leg.\nHamstring Curls on Swiss Ball: 3 sets x 15 reps.\nJumping Lunges: 3 sets x 20 reps per leg.\nSprinting (or Jump Rope): 10 minutes.")
            print("\nDay 5 Cheetah Chase Challenge:\n\nDumbbell Clean and Press: 4 sets x 12 reps.\nRenegade Rows with Dumbbells: 3 sets x 15 reps.\nBox Jumps or Step-Ups: 3 sets x 15 reps.\nBattle Ropes: 4 sets x 30 seconds.\nPlank with Alternating Knee to Elbow: 3 sets x 15 reps per side.\nRowing Machine: 10 minutes.") 
            print("\nDay 6 Cheetah Chase Challenge:\n\n Active Recovery or Light Cardio.") 



    elif fitness_goal == 3:
        print ("\nEndurance, huh? You're not training, you're just preparing to outrun zombies during the apocalypse!\n\nRemember, in a zombie chase, it's not about being the fastest, just faster than your friends!")
        print("\nKeep pushing your limits and you'll achieve amazing results!")
        current_endurance_minutes = int(input("\nHow many minutes do you currently train for?:  "))
        goal_endurance_minutes = int(input("\nHow many minutes are you brave enough to endure in your endurance training session?: "))
        print(f"\n{goal_endurance_minutes} minutes of sheer endurance!\n\nPrepare to sweat buckets and breathe like Darth Vader.\n\nRemember, every drop of sweat is a step closer to becoming the superhero you were always meant to be.")
        precentage_endurance_goal = ( goal_endurance_minutes - current_endurance_minutes / current_endurance_minutes ) * 100
        round_precentage_goal = round (precentage_endurance_goal, 2) 
        print(f"\nYou are looking to increase your endurance by {round_precentage_goal}%!")
        if round_precentage_goal < 21:
            print("\nCongratulations!'Casual Cardio Cruise' a workout so laid-back that even your shadow might forget to keep up! Imagine jogging with the grace of a sleepy sloth and the determination of a snail in no rush.")
            print("\nDay 1 Casual Cardio Cruise Challenge:\n\nBrisk Walking: 30 minutes.\nStationary Bike: 20 minutes.\nBodyweight Squats: 3 sets x 15 reps.\nPush-Ups: 3 sets x 10-12 reps.\nPlank: 3 sets, hold for 30 seconds each.")
            print("\nDay 2 Casual Cardio Cruise Challenge:\n\nActive Recovery or Rest.")
            print("\nDay 3 Casual Cardio Cruise Challenge:\n\nLight Jogging or Running: 20 minutes.\nJumping Jacks: 3 sets x 30 seconds.\nLunges: 3 sets x 12 reps per leg.\nDumbbell Rows (or Bodyweight Rows): 3 sets x 12 reps.\nRussian Twists: 3 sets x 15 reps per side. ")
            print("\nDay 4 Casual Cardio Cruise Challenge:\n\nCycling (Indoor or Outdoor): 30 minutes.\nBodyweight Step-Ups: 3 sets x 15 reps per leg.\nTricep Dips: 3 sets x 12-15 reps.\nLeg Raises: 3 sets x 15 reps.\nSide Plank: 3 sets, hold for 20 seconds each side. ")
            print("\nDay 5 Casual Cardio Cruise Challenge:\n\nSwimming or Water Aerobics: 20 minutes.\nSeated Shoulder Press (with light dumbbells): 3 sets x 12 reps.\nWall Sit: 3 sets, hold for 30 seconds each.\nBicep Curls (with light dumbbells): 3 sets x 12 reps\n.Cooling Down: 10 minutes of gentle stretching.")
            print("\nDay 6 Casual Cardio Cruise Challenge:\n\nActive Recovery or Rest.")
        elif round_precentage_goal < 36:
            print("\nCongratulations! You have been recommended the 'ZigZagging Zebra Zoom'.\n\nThis is a medium intensity workout plan.\n\nImagine jogging with the grace of a zebra prancing in a meadow, with the speed of a sloth on a sugar rush.\n\nSo, put on your running shoes, embrace your inner zebra, and lets make marathon training thrilling!" )
            print("\nDay 1 ZigZagging Zebra Zoom Challenge:\n\nRunning or Jogging: 30 minutes.\nJump Rope: 10 minutes.\nBodyweight Squats: 4 sets x 15 reps.\nPush-Ups: 4 sets x 10-12 reps.\nPlank: 3 sets, hold for 40 seconds each.")
            print("\nDay 2 ZigZagging Zebra Zoom Challenge:\n\nActive Recovery or Rest.")
            print("\nDay 3 ZigZagging Zebra Zoom Challenge:\n\nHigh-Intensity Interval Training (HIIT) - Sprinting or Cycling: 20 minutes.\nJumping Lunges: 3 sets x 15 reps per leg.\nDumbbell Rows: 3 sets x 12 reps.\nRussian Twists: 3 sets x 20 reps per side.\nMountain Climbers: 3 sets x 30 seconds.")
            print("\nDay 4 ZigZagging Zebra Zoom Challenge:\n\nElliptical Trainer: 30 minutes.\nBodyweight Step-Ups: 4 sets x 15 reps per leg.\nTricep Dips: 3 sets x 15 reps.\nLeg Raises: 3 sets x 15 reps.\nSide Plank: 3 sets, hold for 30 seconds each side. ")
            print("\nDay 5 ZigZagging Zebra Zoom Challenge:\n\nSwimming or Water Aerobics: 20 minutes.\nSeated Shoulder Press (with light dumbbells): 4 sets x 12 reps.\nWall Sit: 3 sets, hold for 40 seconds each.\nBicep Curls (with light dumbbells): 4 sets x 12 reps.\nCooling Down: 10 minutes of gentle stretching.")
            print("\nDay 6 ZigZagging Zebra Zoom Challenge:\n\nActive Recovery or Rest.")
        elif round_precentage_goal < 49:
            print("\nCongratulations! You've just become an official member of the 'Mighty Meteorite Marathons' where perseverance is the cosmic currency, and endurance is sculpted with the explosive energy of a comet in a hurry!" )
            print("\nDay 1 Mighty Meteorite Marathons Challenge:\n\nHigh-Intensity Interval Training (HIIT) - Sprinting: 30 minutes (alternating between sprints and brisk walking/jogging).\nJump Rope: 15 minutes.\nBodyweight Squats: 4 sets x 20 reps.\nPush-Ups: 4 sets x 15 reps.\nPlank: 3 sets, hold for 45 seconds each.")
            print("\nDay 2 Mighty Meteorite Marathons Challenge:\n\nActive Recovery or Rest.")
            print("\nDay 3 Mighty Meteorite Marathons Challenge:\n\nHIIT - Cycling: 20 minutes (alternating between high-intensity cycling and moderate pace).\nJumping Lunges: 4 sets x 20 reps per leg.\nDumbbell Rows: 4 sets x 12 reps.\nRussian Twists: 3 sets x 25 reps per side.\nMountain Climbers: 3 sets x 45 seconds.")
            print("\nDay 4 Mighty Meteorite Marathons Challenge:\n\nRunning or Jogging: 40 minutes.\nBox Jumps: 4 sets x 15 reps.\nTricep Dips: 4 sets x 15 reps.\nLeg Raises: 4 sets x 15 reps.\nSide Plank: 3 sets, hold for 60 seconds each side.")
            print("\nDay 5 Mighty Meteorite Marathons Challenge:\n\nRowing Machine: 15 minutes.\nKettlebell Swings: 4 sets x 20 reps.\nBurpees: 4 sets x 15 reps.\nPlank to Push-Up: 3 sets x 20 reps.\nCooling Down: 10 minutes of gentle stretching.")
            print("\nDay 6 Mighty Meteorite Marathons Challenge:\n\nActive Recovery or Rest.")
    while fitness_goal not in [1, 2, 3]:
        fitness_goal = int(input("\nOops! Looks like you've entered an intergalactic space code instead of a number.\n\nPlease pick a number between 1, 2, 3 to continue: "))
            
    response= input("\nWould you like to begin a new workout? Yes or no: ")
    if response != "yes":
        user_wants_workout = False
        print("\nA big thank you for joining our community of fitness enthusiasts. We hope you had a rocking FitPlan experience!!") 


    









