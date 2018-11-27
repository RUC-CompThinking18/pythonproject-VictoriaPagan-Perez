# -*- coding: utf-8 -*-

'''This program chooses random intergers from 6 lists and prints them in .join format with indenting that I made myself.

There are 6 strings total for the project, listed below: All of these lists are used to hold the different strings that will be randomized.

import random' is put at the top of the entire program becuse of the fact that I want this to be a global aspect of the program.
#This also allows the program to be a little cleaner because of the fact that everything is under it, so I don't have to worry about
whether or not the code is in the parameters of the import.

Import time is used for spacing out of the printing of every instance of poem() as well as for the next printouts that are to take place.
It is put at the top of the code for the same reasons as import random.


***VERY IMPORTANT NOTE: At times, when the program is run, it will say that an error occurred, that it was unable to continue due to an
empty list. This is a welcomed error, as it can represent life with depression and mental illness. Many people end their lives too soon
due to mental illnesses, it is because of this that I feel that this error represents those people who ended their lives before their
stories could finish being told.***'''


'''All parts of these poems were found on a poetry website under various sub categories,
to ensure they were completely randomized... The website is: www.familyfriendpoems.com I also , some of the
categories I explored were 'life poems', 'sad poems', 'death poems', and 'poems on Overcoming Hardship'

International Suicide Hotlines were found at:
http://ibpf.org/resource/list-international-suicide-hotlines
"List of International Suicide Hotlines"    from the International Bipolar Foundation
'''

import time
import random

#love is pieces of poems that have to do with  adversity in love
love = ["Hollers of agonizing cries," , "Eyes closed, Heartbeat stopped, Barely alive," , "There was nothing in her life ahead," , "Devils had done her heart way too many wrongs," , "Watching as she wholly became hollow," , "That helped and hurt me, oh so much," , "Nobody knows it's empty, The smile that I wear," , "Nobody knows I miss you," , "Nobody knows I need you," , "But they don't know I am crying, When I am all alone," , "That you failed my heart and didn't even try," , "I love you, and regrets are something that I don't want for you,"]

#race is the adversiBty in race.
race = ["I am the red man driven from the land,", "I am the immigrant clutching the hope I seek,", "I am the Negro, servant to you all,", "Beaten yet today-O, Pioneers,", "I am the man who never got ahead,", "The poorest worker bartered through the years,", "Why is there prejudice and fear,", "We defend our own kind,", "We work out in the hot sun,", "Who give our race a bad name,", "What's the difference, when others don't care," , "What if a black Christ could view," , "Racial slurs and epitahs" , "Perpetuating hatred," , "I'm within my right to expect equality,"]

#religion is the adversity in religion or what religious views people may have.
religion = ["When God is the source of our every need," ,  "The enemy will tempt us, will try to attack," , "We thought that was the end, but that's where he begins," , "I see You here beside me," , "When I was broken or would cry," , "What is a God but a reason for men to do evil and believe it for an honorable purpose," , "Gods. Are they real," , "I ask God the question, Why," , "I say, God please tell me why," , "Yet, not bother taking ten minutes to pray," , "There is only one that died for you," , "Heaven's kingdom on His blood alone," , "When God returns to reign on this earth,"]

#depression is the adversity that people feel from their depression.
depression = ["Emotions. Do you feel them,"  , "Broken, Do you know what that feels like," , "But soon the sky darkens, The sun begins to fall," , "I look in dismay at the night sky," , "The world is dark and nothing is fair," , "Making her believe, That the demons knew best," , "Knocking down the life she knew," , "Hating everything about her," , "She hated herself too," , "These demons can't be seen," , "Now I will see and remember that I was so broken," , "Without being considered insane," , "Around people or not, I still feel alone," , "I cry all the time now,"]

#Neigh_Bullies has different poem fragments that have to do with bullying. Which was a very big part of my life.
Neigh_Bullies = ["He started to sing as he tackled the thing, That couldn't be done, and he did it," ,  "Somebody scoffed: Oh, you'll never do that; At least no one ever has done it,", "There are thousands to point out to you, one by one, The dangers that wait to assail you," , "The bully is never wanted, unless wanted to leave," , "Remember, words can hurt more than the punch," , "Day by day you torment them," , "Called names like ugly, strange and fat," , "I beg for all this hurt to stop," , "ARE YOU HAPPY NOW? NOW THAT THEY ARE GONE," , "Died for NO REASON, and did NOTHING WRONG,"]
#Break_Up has a lot to do with the feeling of losing a significant other, specifically the hurt that they've caused; as opposed to love, which has to do with the feelings of being abandoned almost, and the anger and emptiness that produces.
Break_Up = ["I can't go on being with you... sometimes I'd rather be dead," , "I will never love you again so let me go," , "You hurt me so bad and it makes me sick," , "I should have pushed harder for it to work," , "Fantasies are nightmares, dreams are like hell," , "With blood all around me, I feel nothing now," , "I didn't know if I could live without you," , "My skin is turning cold, hard and blue," , "I'm sorry you couldn't love me," , "I'm sorry you didn't love me," , "Day by day I wait for you," , "I no longer think, I no longer cry,"]

'''I added  and wrote a 'story' string because of the fact that many people who go through all of these things never seem to tell their story, except for the few like myself.
This final string is something that I wrote that adds the ownership of these emotions and showing a sort of courage that is associated with telling your own story.
This also adds onto the narrative in the aspect of the ownership role changing, as this demonstrates that the program/person knows that it/they aren't the only ones
experiencing these troubles.'''
Story = ["       This is my story." , "       This is your story." , "       This is her story." , "       This is his story." , "        This is their story." , "       This is our story." , "       This is my family's story." ]


#the total_choice is here to tell the program to choose only ONE random part of the list that I am calling from (not choosing the entire list)
total_choice = [love , race , religion , depression , Neigh_Bullies , Break_Up]
#total_choice_2 is there to copy the original lines, that way the original lines will not be deleted from.
total_choice_copy = total_choice
'''proof of concept, that random.choice() works in a format:
print random.choice(love) + "," + "\n" + random.choice(race) + "," + "\n" + random.choice(religion) + "," + "\n" + random.choice(depression) + "," + "\n" + random.choice(Neigh_Bullies) + "," + "\n" + random.choice(Break_Up) + "."'''
def poem():
    length = random.randint(1,6) #The reason why I chose random.randint is because I want the amount of lines to be different every time I raise 'poem'. In other words, this is saying that I want the length of the poem to be anywhere in that range of intergers (1,6) '''
    chosen = []  #I then created an empty string to output the lines of the poems to.
    total_choice_copy = total_choice
    for lines in range(length):
        line_type = random.choice(total_choice_copy) #I then told the program to choose  any of the lines in total_choice_copy then to append those to the empty string. I then told the program to return the now full string and then print that out.'''
        count = random.randint(-1, len(line_type) - 1) #I did a count variable because of the fact that I needed a method of selecting the sentences that the program wanted, since it only understands intergers, I needed to use the indices of the strings.
        line = line_type.pop(count)
        '''I then named a new variable called line. What this does is it takes the indices of what was chosen out of 'count' and it pops it into another string that is labeled 'line'.
        This stops that line from  being repeated, as that index number no longer exists in the original string.'''
        chosen.append(line)
    time.sleep(random.randint(1,6)) # I then told the program that whatever it chose would then be appended to chosen. This gives something to print. I also added a random.randint for time.sleep because I found that it added to the narrative of different stories being told.
    return  "      " + '\n'.join(chosen) + '\n' + random.choice(Story) + '\n' #I added a new string entitled 'Story' which ends each poem with an ownership sentence as well as a new line after it, this helped differientiate the different poems from eachother.
        #The new "Story" list also takes a nameless program and put a humanistic quality that takes the poems from interesting to almost melancholic and haunting.

'''NOTES ON IF, ELIF, ELSE FORMATTING:
I put everything in an if, elif, else statement becuase of the fact that there are many factors that I want the program to have a prompt for.
When doing user interaction the first thing that I wanted to make sure that worked was if the user entered 'yes'. This was arguably one of the harder parts for me because of
the fact that I hadn't done raw input ever before. I only did boolean true/false statements. Once I did some research and I got it to answer the way that I wanted it to is when I realized
that I would need elif statements as well, since there is more than two possible outcomes. Since I also wanted the second warning to come up, I knew that I needed to nest the second if, elif, else statement in
the original question if, elif, else, statement. This was a little tricky for me since I had trouble getting the while loop to nest in there and print to twelve iterations, with the random poem length.
'''

'''NOTES ON WHILE LOOP:
The reason why I wanted to put in  a while loop is because of the fact that I know that many people who have mental illnesses choose to stay silent and never
suffer in silence because their illnesses can be seen as a 'weakness' or a sign of fragility. So I wanted my program to have a poem per year that I've been diagnosed with my mental illness.
In order to achieve this I created a while loop. The reason why I used the while loop is because it can run the code over and over again until it hits the 12th poem.
This code is also in  the global scope of the code. The reason for this is that the definition already has it's parameters, therefore it cannot handle another equation.
I also want this entire code to follow this while loop, therefore it has to go in the global scope. '''

question = raw_input("Hello, I have a question for you, Are you ready? Type 'yes' or 'no':")#This raw_input is the first question that I want to ask. The reason why I am asking this is to not only generate interest,  but to also give the user a chance to leave, if they choose.
years_of_sickness = 0 #The counter starts at zero because of the fact that the other previous prints count towards the total count.
#I found that the neatest way to achieve this User Interaction was to do a if, elif else statement nested in another if, elif, else statement. That way everything could be understandable and I could find any errors quickly and painlessly.
if question == "yes":
    warning = raw_input("The program that is about to execute has to do with content that some may find disturbing. " + '\n' + "If you still wish to continue type 'yes', if not, type 'no':") #I put in a second warning to ensure that the user knows what they are getting into.
    if warning == "no":
        print "This isn't for you"#The reason why I have the TypeError and the sentence "This isn't for you." is because the topics in this piece can be seen as triggering and I don't want to trigger anyone.
        raise TypeError("goodbye")#I raised the TypeError because I wanted the program to stop here if they were to type "no"
    elif warning == "yes":
        years_of_sickness = 0 #The reason why I used years_of_sickness is because that  is how many years I have been diagnosed with all of these illnesses.
        while years_of_sickness < 12:#I used 12 because I was diagnosed 12 years ago.... This line of code specifically says that as long as the years_of_sickness (iteration of the above code) is less than or equal to 12, to do the following.
            years_of_sickness += 1#This piece of code is acting as the counter in the code. This is here so that the code doesn't loop infinately, if it did, then the computer would crash.
                                 #This then tells the code that as soon as the code counter hits 12, to stop printing the code under poem() which is the code that contains all of the strings, counters, and formatting.
            print poem()
#The reason why I added in all of these prints is because I really wanted to put the fact that we aren't alone in the spotlight. For me, the first thing I think is that I'm alone and that's how it's always going to be, so I put this in so that people knew, they aren't alone.
        print '\n' + '\n'"Do you understand now? There are millions like us. We feel like no one understands, like no one cares..." + '\n' + '\n'
        time.sleep(5)#You'll notice that I did a countdown from 5 here. The reason why I did this is becuase it is one of the first anxiety techniques that I was taught. When I am about to have an attack, I need to clear my head and count down from 5. That makes me feel safe, which is why at the end of the countdown is where the hotlines are displayed.
        print "Like we aren't worth it or don't matter enough to do something about it." + '\n' + '\n'
        time.sleep(4)
        print "Like we are nothing but a burden, a waste of space..." + '\n' + '\n'
        time.sleep(3)
        print "But we aren't... you aren't." + '\n' + '\n' + "If you have depression, thoughts of harming yourself, or suicide," + '\n' + "Please don't hesitate to call: " + '\n' + '\n'
        time.sleep(2)#I did a time.sleep of 4 seconds so that the user can have some time to digest all of the infornmation they were given.
        print "Argentina: +5402234930430" + '\n' + "Australia: 131114" + '\n' + "Austria: 017133374" + '\n' + "Belgium: 106" + '\n' + "Bosnia & Herzegovina: 080 05 03 05" + '\n' + "Botswana: 3911270" + '\n' + "Brazil: 188 for the CVV National Association" + '\n' + "Canada: 5147234000 (Montreal); 18662773553 (outside Montreal)" + '\n' + "Croatia: 014833888" + '\n' + "Denmark: +4570201201" + '\n' + "Egypt: 7621602" + '\n' + "Estonia: 3726558088; in Russian 3726555688" + '\n' + "Finland: 010 195 202" + '\n' + "France: 0145394000" + '\n' + "Germany: 08001810771" + '\n' + "Holland: 09000767" + '\n' + "Hong Kong: +852 2382 0000" + '\n' + "Hungary: 116123" + '\n' + "India: 8888817666" + '\n' + "Ireland: +4408457909090" + '\n' + "Italy: 800860022" + '\n' + "Japan: +810352869090" + '\n' + "Mexico: 5255102550" + '\n' + "New Zealand: 0800543354" + '\n' + "Norway: +4781533300" + '\n' + "Philippines: 028969191" + '\n' + "Poland: 5270000" + '\n' + "Portugal: 21 854 07 40/8 . 96 898 21 50" + '\n' + "Russia: 0078202577577" + '\n' + "Spain: 914590050" + '\n' + "South Africa: 0514445691" + '\n' + "Sweden: 46317112400" + '\n' + "Switzerland: 143" + '\n' + "United Kingdom: 08457909090" + '\n' + "USA: 18002738255" + '\n' + "Veterans' Crisis Line: 1 800 273 8255/ text 838255"
        time.sleep(1)
        print '\n' + '\n' + "The truth is, you were never alone, and you never will be. Thank you for using this program... I wish you well... Goodbye"
    else:
        print 'Please reload and type in "yes" or "no" as it is written!'#The reason why I have the program end here if it wasn't typed in as written was because of the fact that when in a depression it takes so much to do one thing. This, in a way, represents the set backs that happen in someones mind if they do just one thing wrong.
elif question == "no":#This addresses the first raw_input, if the answer is "no" then to raise the TypeError.
    print "This isn't for you."
    raise TypeError("goodbye") #I raised the TypeError to ensure that the code would stop.
else:
    print 'Please reload and type in "yes" or "no" as it is written!'#The reason why I have the program end here if it wasn't typed in as written was because of the fact that when in a depression it takes so much to do one thing. This, in a way, represents the set backs that happen in someones mind if they do just one thing wrong.
