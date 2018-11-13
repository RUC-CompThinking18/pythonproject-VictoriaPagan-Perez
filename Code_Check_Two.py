
'''For my first check I want to make the program choose random intergers from multiple lists and print them.
There are 6 strings total for the project, listed below: All of these lists are used to hold the different strings that will be randomized.'''
''''import random' is put at the top of the entire program becuse of the fact that I want this to be a global aspect of the program.
#This also allows the program to be a little cleaner because of the fact that everything is under it, so I don't have to worry about
whether or not the code is in the parameters of the import.'''

'''All parts of these poems were found on a poetry website under various sub categories,
to ensure they were completely randomized... The website is: www.familyfriendpoems.com, some of the
categories I explored were 'life poems', 'sad poems', 'death poems', and 'poems on Overcoming Hardship' '''

import timeit
import random

#love is pieces of poems that have to do with  adversity in love
love = ["Hollers of agonizing cries," , "Eyes closed, Heartbeat stopped, Barely alive," , "There was nothing in her life ahead," , "Devils had done her heart way too many wrongs," , "Watching as she wholly became hollow," , "That helped and hurt me, oh so much," , "Nobody knows it's empty, The smile that I wear," , "Nobody knows I miss you," , "Nobody knows I need you," , "But they don't know I am crying, When I am all alone...," , "That you failed my heart and didn't even try," , "I love you, and regrets are something that I don't want for you,"] #14

#race is the adversiBty in race.
race = ["I am the red man driven from the land,", "I am the immigrant clutching the hope I seek-,", "I am the Negro, servant to you all,", "Beaten yet today-O, Pioneers!,", "I am the man who never got ahead,", "The poorest worker bartered through the years,", "Why is there prejudice and fear?,", "We defend out own kind,", "We work out in the hot sun,", "Who give our race a bad name,", "What's the difference, when others don't care," ]
#9
#religion is the adversity in religion or what religious views people may have.
religion = ["When God is the source of our every need," ,  "The enemy will tempt us, will try to attack," , "We thought that was the end, but that's where he begins," , "I see You here beside me," , "When I was broken or would cry," , "What is a God but a reason for men to do evil and believe it for an honorable purpose?," , "Gods. Are they real?," , "I ask God the question, Why?," , "I say, God please tell me why," , "Yet, not bother taking ten minutes to pray?," , "There is only one that died for you," , "Heaven's kingdom on His blood alone," , "When God returns to reign on this earth,"]

#depression is the adversity that people feel from their depression.
depression = ["Emotions. Do you feel them,"  , "Broken, Do you know what that feels like?," , "But soon the sky darkens, The sun begins to fall," , "I look in dismay at the night sky," , "The world is dark and nothing is fair," , "Making her believe, That the demons knew best," , "Knocking down the life she knew," , "Hating everything about her," , "She hated herself too," , "These demons can't be seen," , "Now I will see and remember that I was so broken," , "Without being considered insane," , "Around people or not, I still feel alone," , "I cry all the time now,"]

#Neigh_Bullies has different poem fragments that have to do with bullying. Which was a very big part of my life.
Neigh_Bullies = ["He started to sing as he tackled the thing, That couldn't be done, and he did it," ,  "Somebody scoffed: Oh, you'll never do that; At least no one ever has done it,", "There are thousands to point out to you, one by one, The dangers that wait to assail you," , "The bully is never wanted, unless wanted to leave," , "Remember, words can hurt more than the punch," , "Day by day you torment them," , "Called names like ugly, strange and fat," , "I beg for all this hurt to stop," , "ARE YOU HAPPY NOW? NOW THAT THEY ARE GONE?!," , "Died for NO REASON, and did NOTHING WRONG!,"]
#Break_Up has a lot to do with the feeling of losing a significant other, specifically the hurt that they've caused; as opposed to love, which has to do with the feelings of being abandoned almost, and the anger and emptiness that produces.
Break_Up = ["I can't go on being with you... sometimes I'd rather be dead," , "I will never love you again so let me go," , "You hurt me so bad and it makes me sick," , "I should have pushed harder for it to work," , "Fantasies are nightmares, dreams are like hell," , "With blood all around me, I feel nothing now," , "I didn't know if I could live without you," , "My skin is turning cold, hard and blue," , "I'm sorry you couldn't love me," , "I'm sorry you didn't love me," , "Day by day I wait for you," , "I no longer think, I no longer cry,"]

'''I added  and wrote a 'story' string because of the fact that many people who go through all of these things never seem to tell their story, except for the few like myself.
This final string is something that I wrote that adds the ownership of these emotions and showing a sort of courage that is associated with telling your own story.
This also adds onto the narrative in the aspect of the ownership role changing, as this demonstrates that the program/person knows that it/they aren't the only ones
experiencing these troubles.'''
Story = ["This is my story." , "This is your story." , "This is her story." , "This is his story." , "This is their story." , "This is our story." , "This is my family's story." , ]

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
        chosen.append(line) #''' I then told the program that whatever it chose would then be appended to chosen. This gives something to print.'''
        return  '\n'.join(chosen) + '\n' + random.choice(Story) #I added a new string entitled 'Story' which ends each poem with an ownership sentence.
        #Not only does this differientiate one poem from the next, but it also takes a nameless program and put a humanistic quality that takes the poems
        # from interesting to almost melancholic and haunting.


days_of_sickness = 1
while days_of_sickness <= 12:
    days_of_sickness += 1
    print poem()  + '\n'* 4
''' Check Two Changes:
 1. Added a new string to the whole program
 2. Manually formatted the definition's print output(This took about a week since I am so technologically impaired.)
 3. Added in a while loop to have the poems print 12 times only (since infinately would cause the computer to crash)'''

#days_of_sickness
#then the while loop
#while days <=
#print(poem)
#days_of_sickness += 1
#ok so we have the def poem but we don't want multiples in that one. so just return the poem in poem definiton, revert to poem funct. then do whu
#SO have the while loop in the global scope and call it in the while loop. and days of sickness should