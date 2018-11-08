
'''For my first check I want to make the program choose random intergers from multiple lists and print them.
There are 6 strings total for the project, listed below: All of these lists are used to hold the different strings that will be randomized.'''
''''import random' is put at the top of the entire program becuse of the fact that I want this to be a global aspect of the program.
#This also allows the program to be a little cleaner because of the fact that everything is under it, so I don't have to worry about
whether or not the code is in the parameters of the import.'''


import random

#love is pieces of poems that have to do with  adversity in love
love = ["Hollers of agonizing cries" , "Eyes closed, Heartbeat stopped, Barely alive" , "There was nothing in her life ahead" , "Devils had done her heart way too many wrongs" , "Watching as she wholly became hollow" , "That helped and hurt me, oh so much" , "Nobody knows it's empty, The smile that I wear" , "Nobody knows I miss you" , "Nobody knows I need you" , "But they don't know I am crying, When I am all alone..." , "That you failed my heart and didn't even try" , "I love you, and regrets are something that I don't want for you"] #14

#race is the adversiBty in race.
race = ["I am the red man driven from the land", "I am the immigrant clutching the hope I seek-", "I am the Negro, servant to you all", "Beaten yet today-O, Pioneers!", "I am the man who never got ahead", "The poorest worker bartered through the years", "Why is there prejudice and fear?", "We defend out own kind", "We work out in the hot sun", "Who give our race a bad name", "What's the difference, when others don't care" ]
#9
#religion is the adversity in religion or what religious views people may have.
religion = ["When God is the source of our every need" ,  "The enemy will tempt us, will try to attack" , "We thought that was the end, but that's where he begins" , "I see You here beside me" , "When I was broken or would cry" , "What is a God but a reason for men to do evil and believe it for an honorable purpose?" , "Gods. Are they real?" , "I ask God the question, Why?" , "I say, God please tell me why" , "Yet, not bother taking ten minutes to pray?" , "There is only one that died for you" , "Heaven's kingdom on His blood alone" , "When God returns to reign on this earth"]

#depression is the adversity that people feel from their depression.
depression = ["Emotions. Do you feel them"  , "Broken, Do you know what that feels like?" , "But soon the sky darkens, The sun begins to fall" , "I look in dismay at the night sky" , "The world is dark and nothing is fair" , "Making her believe, That the demons knew best" , "Knocking down the life she knew" , "Hating everything about her" , "She hated herself too" , "These demons can't be seen" , "Now I will see and remember that I was so broken" , "Without being considered insane" , "Around people or not, I still feel alone" , "I cry all the time now"]

#Neigh_Bullies has different poem fragments that have to do with bullying. Which was a very big part of my life.
Neigh_Bullies = ["He started to sing as he tackled the thing, That couldn't be done, and he did it" ,  "Somebody scoffed: Oh, you'll never do that; At least no one ever has done it", "There are thousands to point out to you, one by one,The dangers that wait to assail you" , "The bully is never wanted, unless wanted to leave" , "Remember, words can hurt more than the punch" , "Day by day you torment them" , "Called names like ugly, strange and fat" , "I beg for all this hurt to stop" , "ARE YOU HAPPY NOW? NOW THAT THEY ARE GONE?!" , "Died for NO REASON, and did NOTHING WRONG!"]
#Break_Up has a lot to do with the feeling of losing a significant other, specifically the hurt that they've caused; as opposed to love, which has to do with the feelings of being abandoned almost, and the anger and emptiness that produces.
Break_Up = ["I can't go on being with you... sometimes I'd rather be dead" , "I will never love you again so let me go" , "You hurt me so bad and it makes me sick" , "I should have pushed harder for it to work" , "Fantasies are nightmares, dreams are like hell" , "With blood all around me, I feel nothing now" , "I didn't know if I could live without you" , "My skin is turning cold, hard and blue" , "I'm sorry you couldn't love me" , "I'm sorry you didn't love me" , "Day by day I wait for you" , "I no longer think, I no longer cry"]


#the total_choice is here to tell the program to choose only ONE random part of the list that I am calling from (not choosing the entire list)
total_choice = [love , race , religion , depression , Neigh_Bullies , Break_Up]
#total_choice_2 is there to copy the original lines, that way the original lines will not be deleted from.
total_choice_2 = total_choice
'''proof of concept, that random.choice() works in a format:
print random.choice(love) + "," + "\n" + random.choice(race) + "," + "\n" + random.choice(religion) + "," + "\n" + random.choice(depression) + "," + "\n" + random.choice(Neigh_Bullies) + "," + "\n" + random.choice(Break_Up) + "."'''
def poem():
    length = random.randint(1,6) #The reason why I chose random.randint is because I want the amount of lines to be different every time I raise 'poem'. In other words, this is saying that I want the length of the poem to be anywhere in that range of intergers (1,6) '''
    chosen = []  #I then created an empty string to output the lines of the poems to.
    for lines in range(length):
        line_type = random.choice(total_choice_2) #I then told the program to choose  any of the lines in total_choice then to append those to the empty string. I then told the program to return the now full string and then print that out.'''
        line = random.choice(line_type)
        #count = random.randint(0, )
        chosen.append(line)

    return chosen
    chosen.remove(line)
print poem()
