#this is a would you rather program

import random
def questionAndQuestions():
    #determines how many questions to give the user based on their input to this question
    print("The game is would you rather, you will be asked to make a choice between 2 silly options and judged accordingly by the AI, you have been warned.\n")
    print("To answer the questions correctly you must base your choice closey off the written questions and options\nHave Fun.\n")
    print("How many turns would you like to take?\n")
    numberOfDilemmas = input()
    #using int to only accept numerical input
    numberOfDilemmas = int(numberOfDilemmas)
    #limits the user to only 10 questions at a time
    if numberOfDilemmas > 10:
        print("What! Look I don't have all day you'll need to choose less than that")
        questionAndQuestions()
        #if the user chooses 0 the game ends
    if numberOfDilemmas <=0:
        print("Ok then...Bye.")
        exit(0)
    else:
        #this is the list that the questions will be chosen from at random

        for dilemmasWanted in range (numberOfDilemmas):
            Scene1 = 1
            Scene2 = 2
            Scene3 = 3
            Scene4 = 4
            Scene5 = 5
            Scene6 = 6
            Scene7 = 7
            Scene8 = 8
            Scene9 = 9
            Scene10 = 10
            Scene11 = 11
            Scene12 = 12
            Scene13 = 13
            Scene14 = 14
            Scene15 = 15
            Scene16 = 16
            Scene17 = 17
            Scene18 = 18
            Scene19 = 19
            Scene20 = 20
            Scene21 = 21
            Scene22 = 22
            Scene23 = 23
            Scene24 = 24
            Scene25 = 25
            #the random variable that chooses in range of 25 questions

            questionNumber = random.randint(1,25)
                #if random is this number it will ask this question
            if questionNumber ==1:
                Scene1Answer = input("Would you rather Skittles or M&Ms?\n")
                #if user response is one of these options then a response will play
                if Scene1Answer == "Skittles" or Scene1Answer == "skittles":
                    print("Oh, you're on of those... very well next question\n")
                #if user response is one of these options then a response will play
                elif Scene1Answer == "M&Ms" or Scene1Answer == "m&ms":
                    print("Right, clearly the only correct answer here.\n")
                #if the user doesn't want to make a proper choice then it will end.
                else:
                    print("wow\n")
                    exit(0)

            if questionNumber ==2:
                #if random is this number it will ask this question
                Scene2Answer = input("Would you rather be hunted by the Terminator or the Predator?\n")
                if Scene2Answer == "Terminator" or Scene2Answer == "terminator":
                    print("Yeah right, like you'd have a chance against Arnold.\n")
                elif Scene2Answer == "Predator" or Scene2Answer == "predator":
                    print("You got to be some sort of slick to evade the Predator.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("No\n")
                    exit(0)

            if questionNumber ==3:
                #if random is this number it will ask this question
                Scene3Answer = input("Would you rather super speed or strength?\n")
                 #if user response is one of these options then a response will play
                if Scene3Answer == "Speed" or Scene3Answer =="speed":
                    print("I don't know, I think if you could run at the speed of light your body would melt, but hey your choice.\n")
                     #if user response is one of these options then a response will play
                elif Scene3Answer == "Strength" or Scene3Answer =="strength":
                    print("Right, because the world needs more meatheads.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("hmmm.\n")
                    exit(0)

            if questionNumber ==4:
                #if random is this number it will ask this question
                Scene4Answer = input("Would you rather fight Mike Tyson or Mayweather?\n")
                 #if user response is one of these options then a response will play
                if Scene4Answer == "Tyson" or Scene4Answer =="tyson" or Scene4Answer =="mike" or Scene4Answer =="Mike Tyson" or Scene4Answer =="Mike":
                    print("Good luck paying for that hospital bill\n")
                     #if user response is one of these options then a response will play
                elif Scene4Answer == "Mayweather" or Scene4Answer =="mayweather" or Scene4Answer =="Floyd Mayweather":
                    print("Lets hope he takes it easy on you\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("nah\n")
                    exit(0)

            if questionNumber ==5:
                #if random is this number it will ask this question
                Scene5Answer = input("Would you rather learn to use Nunchucks or Tonfa\n")
                 #if user response is one of these options then a response will play
                if Scene5Answer == "Nunchucks" or Scene5Answer =="nunchucks":
                    print("Oh, I see you must be a Bruce Lee fan.\n")
                     #if user response is one of these options then a response will play
                elif Scene5Answer == "Tonfa" or Scene5Answer =="tonfa":
                    print("can't imagine they'd even let you walk the streets with those.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("huh\n")
                    exit(0)
            if questionNumber ==6:
                #if random is this number it will ask this question
                Scene6Answer = input("Would you rather not be able to stop dancing or not stop singing?\n")
                 #if user response is one of these options then a response will play
                if Scene6Answer == "Singing" or Scene6Answer =="singing":
                    print("Man your neighbors would hate you... moving on.\n")
                     #if user response is one of these options then a response will play
                elif Scene6Answer == "dancing" or Scene6Answer =="Dancing":
                    print("Alright twinkle toes good luck with sleeping.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("oh\n")
                    exit(0)

            if questionNumber ==7:
                #if random is this number it will ask this question
                Scene7Answer = input("would you rather be poor with lots of good friends or rich with no friends?\n")
                 #if user response is one of these options then a response will play
                if Scene7Answer == "poor" or Scene7Answer =="Poor":
                    print("I could imagine you like a little RobinHood.\n")
                     #if user response is one of these options then a response will play
                elif Scene7Answer == "Rich" or Scene7Answer =="rich":
                    print("You'd probably be like Bruce Wayne minus the Batman part.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("I see\n")
                    exit(0)

            if questionNumber ==8:
                #if random is this number it will ask this question
                Scene8Answer = input("Would you rather be completely alone for 5 years or constantly be surrounded by people and never be alone for 5 years?\n")
                 #if user response is one of these options then a response will play
                if Scene8Answer == "Alone" or Scene8Answer == "alone":
                    print("Exactly, people are such a hassle am I right?.\n")
                     #if user response is one of these options then a response will play
                elif Scene8Answer == "Surrounded" or Scene8Answer == "surrounded":
                    print("Say goodbye to privacy.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("uh.\n")
                    exit(0)

            if questionNumber ==9:
                #if random is this number it will ask this question
                Scene9Answer = input("Would you rather have a song of your choice play repeatedly 24 hours a day for a year or have songs that you have no control over play 24 hours a day for a year?\n")
                 #if user response is one of these options then a response will play
                if Scene9Answer == "song of choice" or  Scene9Answer =="Song of choice":
                    print("Oh, you're going to go insane.\n")
                     #if user response is one of these options then a response will play
                elif Scene9Answer == "No control of songs" or  Scene9Answer =="no control of songs":
                    print("ah yes when life gives you lemons make it a variety.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("shh\n")
                    exit(0)

            if questionNumber ==10:
                #if random is this number it will ask this question
                Scene10Answer = input("Would you rather be hot all the time or cold all the time\n")
                 #if user response is one of these options then a response will play
                if Scene10Answer == "hot"or Scene10Answer =="Hot":
                    print("You'd be dripping like a faucet, you'd need to shower every hour.\n")
                     #if user response is one of these options then a response will play
                elif Scene10Answer == "Cold" or Scene10Answer == "cold":
                    print("Hopefully you have lots of blankets.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("ok\n")
                    exit(0)

            if questionNumber ==11:
                #if random is this number it will ask this question
                Scene11Answer = input("Would you rather lose your sight or memories?\n")
                 #if user response is one of these options then a response will play
                if Scene11Answer == "Sight" or Scene11Answer =="sight":
                    print("Maybe chosing blindness may heighten your memory?\n")
                     #if user response is one of these options then a response will play
                elif Scene11Answer == "memories" or Scene11Answer =="Memories":
                    print("With no memories I don't know if you'd remember this conversation we're having... or me.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("wow\n")
                    exit(0)

            if questionNumber ==12:
                #if random is this number it will ask this question
                Scene12Answer = input("Would you rather be labor under th hot sun or extreme cold?\n")
                 #if user response is one of these options then a response will play
                if Scene12Answer == "Hot Sun" or Scene12Answer =="hot sun":
                    print("I don't think you'd survive till lunch time in the sun.\n")
                     #if user response is one of these options then a response will play
                elif Scene12Answer == "extreme cold" or Scene12Answer =="Extreme Cold":
                    print("Maybe if you bundle up you might prevent frostbite.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("dang\n")
                    exit(0)

            if questionNumber ==13:
                #if random is this number it will ask this question
                Scene13Answer = input("Would you rather buy 10 things you don't need every time you go shopping or always forget the one thing you need when you go to the store?\n")
                 #if user response is one of these options then a response will play
                if Scene13Answer == "10 things" or Scene13Answer =="10 Things":
                    print("You'd probably waste a whole paycheck on bean bag chairs.\n")
                     #if user response is one of these options then a response will play
                elif Scene13Answer == "Forget the one thing" or Scene13Answer == "forget the one thing":
                    print("It would be kinda pointless to go to the store and not get what you needed.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("Wrong.\n")
                    exit(0)

            if questionNumber ==14:
                #if random is this number it will ask this question
                Scene14Answer = input("Would you rather never be able to go out during the day or never be able to go out at night?\n")
                 #if user response is one of these options then a response will play
                if Scene14Answer == "Day" or Scene14Answer == "day" or Scene14Answer == "The day" or Scene14Answer == "the day":
                    print("Literal vampire.\n")
                     #if user response is one of these options then a response will play
                elif Scene14Answer == "Night" or Scene14Answer =="night" or Scene14Answer == "The night" or Scene14Answer =="the night":
                    print("What about doing all the cool stuff you could do during the day just at night?\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("ugh\n")
                    exit(0)

            if questionNumber ==15:
                #if random is this number it will ask this question
                Scene15Answer = input("Would you rather communicate only in emoji or never be able to text at all ever again?\n")
                 #if user response is one of these options then a response will play
                if Scene15Answer == "emoji"or Scene15Answer == "Emoji":
                    print("Might as well become a professional mime.\n")
                     #if user response is one of these options then a response will play
                elif Scene15Answer == "Never be able to text" or Scene15Answer == "never be able to text" or Scene15Answer =="text":
                    print("That would surely make phone calls useful.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("Golly\n")
                    exit(0)
            if questionNumber ==16:
                #if random is this number it will ask this question
                Scene16Answer = input("Would you rather watch nothing but christmas movies or nothing but horror movies?\n")
                 #if user response is one of these options then a response will play
                if Scene16Answer == "Christmas movies" or Scene16Answer == "christmas movies":
                    print("You better hope no one else wants to watch anything else with you.\n")
                     #if user response is one of these options then a response will play
                elif Scene16Answer == "horror movies" or Scene16Answer == "Horror movies":
                    print("literally the only right answer here.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("neat\n")
                    exit(0)

            if questionNumber ==17:
                #if random is this number it will ask this question
                Scene17Answer = input("would you rather have a pause or rewind button in your life?\n")
                 #if user response is one of these options then a response will play
                if Scene17Answer == "pause" or Scene17Answer == "Pause":
                    print("It would really be something if you pause right in time and still get caught after unpausing.\n")
                     #if user response is one of these options then a response will play
                elif Scene17Answer == "Rewind" or Scene17Answer == "rewind":
                    print("I figure all risks and dangers in life just be negated, try free falling.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("Ahh\n")
                    exit(0)

            if questionNumber ==18:
                #if random is this number it will ask this question
                Scene18Answer = input("Would you rather oversleep every day for a week or not get any sleep at all for four days?\n")
                 #if user response is one of these options then a response will play
                if Scene18Answer == "oversleep" or Scene18Answer == "Oversleep":
                    print("Its going to be a rough week if you have any responsiblities?\n")
                     #if user response is one of these options then a response will play
                elif Scene18Answer == "not get any sleep" or Scene18Answer == "Not get any sleep" or Scene18Answer =="no sleep":
                    print("four days yeah thats easy.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("gosh.\n")
                    exit(0)

            if questionNumber ==19:
                #if random is this number it will ask this question
                Scene19Answer = input("Would you rather spend a year at war or a year in prison?\n")
                 #if user response is one of these options then a response will play
                if Scene19Answer == "war" or Scene19Answer == "War":
                    print("War is hell.\n")
                     #if user response is one of these options then a response will play
                elif Scene19Answer == "prison" or Scene19Answer =="Prison":
                    print("that would make job hunting tough.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("ooh\n")
                    exit(0)

            if questionNumber ==20:
                #if random is this number it will ask this question
                Scene20Answer = input("Would you rather walk to work in heels or drive to work in reverse\n")
                 #if user response is one of these options then a response will play
                if Scene20Answer == "heels" or Scene20Answer == "Heels":
                    print("Yeah you'd look stylish at the workplace.\n")
                     #if user response is one of these options then a response will play
                elif Scene20Answer == "reverse" or Scene20Answer =="Reverse" or Scene20Answer =="drive to work in reverse" or Scene20Answer =="Drive to work in reverse":
                    print("Lots of insurance bills.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("rah\n")
                    exit(0)

            if questionNumber ==21:
                #if random is this number it will ask this question
                Scene21Answer = input("Would you rather hunt and butcher your own meat or never eat meat again?\n")
                 #if user response is one of these options then a response will play
                if Scene21Answer == "hunt" or Scene21Answer ==  "Hunt":
                    print("I don't know where you're going to hunt burgers.\n")
                     #if user response is one of these options then a response will play
                elif Scene21Answer == "Never eat meat" or Scene21Answer ==  "never eat meat":
                    print("Maybe, if you can commit to that.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("Course\n")
                    exit(0)

            if questionNumber ==22:
                #if random is this number it will ask this question
                Scene22Answer = input("Would you rather have unlimited battery life on all devices or have free WIFI wherever you go?\n")
                 #if user response is one of these options then a response will play
                if Scene22Answer == "battery" or Scene22Answer == "Battery" or"unlimited battery life" or Scene22Answer == "Unlimited battery life":
                    print("You really struggle with charging stuff that much?\n")
                     #if user response is one of these options then a response will play
                elif Scene22Answer == "Wifi" or Scene22Answer ==  "WIFI"or Scene22Answer == "free WIFI":
                    print("Better hope its good service.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("uhh\n")
                    exit(0)

            if questionNumber ==23:
                #if random is this number it will ask this question
                Scene23Answer = input("Would you rather travel the world for free for a year or have $50,000 to spend however you please?\n")
                 #if user response is one of these options then a response will play
                if Scene23Answer == "Travel" or Scene23Answer == "travel" or Scene23Answer == "travel the world for free":
                    print("honestly that may well be the best year of your life.\n")
                     #if user response is one of these options then a response will play
                elif Scene23Answer == "50,000" or Scene23Answer == "fifty thousand dollars":
                    print("Right, travelling is overated.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("phew.\n")
                    exit(0)

            if questionNumber ==24:
                #if random is this number it will ask this question
                Scene24Answer = input("Would you rather only be able to talk to your pet or have your pet be able to talk to you when you're alone?\n")
                 #if user response is one of these options then a response will play
                if Scene24Answer == "only be able to talk to my pet" or Scene24Answer == "Only be able to talk to my pet":
                    print("That will make communication pretty hard\n")
                     #if user response is one of these options then a response will play
                elif Scene24Answer == "pet be able to talk " or Scene24Answer == "pet be able to talk to me when I'm alone" or Scene24Answer == "pet be able to talk to me when i'm alone":
                    print("Awesome but you might end up in a mental insitution\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("right\n")
                    exit(0)

            if questionNumber ==25:
                #if random is this number it will ask this question
                Scene25Answer = input("Would you rather have super-sensitive taste buds or super-sensitive hearing?\n")
                 #if user response is one of these options then a response will play
                if Scene25Answer == "taste buds" or Scene25Answer =="Taste buds" or Scene25Answer =="super-sensitive taste buds"or Scene25Answer =="Super-sensitive taste buds":
                    print("Stay away from spicy foods.\n")
                     #if user response is one of these options then a response will play
                elif Scene25Answer == "hearing" or Scene25Answer == "Hearing"or Scene25Answer == "super-sensitive hearing"or Scene25Answer == "Super-sensitive hearing":
                    print("That would probably be annoying when trying to sleep.\n")
                else:
                    #if the user doesn't want to make a proper choice then it will end.
                    print("nope\n")
                    exit(0)

questionAndQuestions()

    
