OVERVIEW OF THE PROJECT:
THE PROGRAM WILL:
    >>Ask the user if they are ready for the program to begin, if 'yes' is typed in, a second prompt will be triggered to ensure that they are ready for the program to begin.
    >> If "no" is written for either prompt, the program will print "This isn't for you" and a TypeError will be thrown with the message "goodbye", to ensure the program stops.
    >>If anything else is typed other than 'yes' or 'no' as shown, there will be a prompt that instructs the user to reload the program and type 'yes' or 'no' as it is written.
    >>Choose random lines from random strings to construct a poem in poem format.
            IE:       ______________________,
                    ________________________,
    >>The first and last lines will be indented by a large margin.
    >>The last line is chosen from a list of possessive sentences ("This is _____ story.")
    >>After this prints 12 times, the second half of prints will trigger with a time.sleep of 5 seconds counting down to one
    >>The next print will consist of suicide prevention hotlines that can be called internationally, and a final farewell message will be printed.
    >>This is where the program ends.
    >>There are rare occasions in which the program will shut down if one list runs out of lines to pick. This is a welcomed error as it also has meaning. Some people don't get to finish their story since their lives end too soon.




    For my project, I wanted to do something that represented a side of me that not a lot of people know about. The side of me that not many know about is the mentally ill side of me. I have Bipolar Disorder, Severe Anxiety, Severe Depression, Social Anxiety Disorder, and
 ADHD. All of these things cause me to be on a constant rollercoaster of emotions and can cause some very traumatic experiences for me. One of the things that I try to do whenever I am in a very bad place mentally, is to try and get those emotions out. Since I had a terrible speech
impediment when I was younger and I was a good writer, I used poems as an escape from my own mind. I also found that expressing my frustrations and emotions through poems was doing something with these emotions and expressing them physically, which provided and still does provide a
greater comfort than just simply talking about it. I also find that my poems during these times are very fragmented and disjointed. When I found out we were doing this project is when I got the inspiration for this project. I wanted to talk about the adversities in not only my life
but in many people's lives and have it be completely randomized in order and sentence like my illnesses make my emotions and my reactions to the world completely random.  It saddens me that many people don't want to talk about illnesses like mine as well as almost shunning people
with them. It was because of that fact that I wanted to approach these topics with something that's very non-threatening and relatable to most people, poetry. I wanted to show that it is okay to ask for help and that it is okay to own who you are and say "I'm not okay and I need help".
I am doing that through showing that I am not the only one going through hardships, although I am one of the few that is comfortable enough to talk about it. Another reason as to why I wanted the program to choose everything completely at random was because conversations about my mental illness
usually come up at random and can range in length. I also wanted to acknowledge that I am not the only person going through hardships either, which is why each poem ends with "This is ______ story." This brings a slightly humanistic property to the program and makes the user relate even
more to the piece.

THE FIRST CHECK

    The first thing that I wanted to do was to make sure that, at the very least, the concept worked. In order to do that I wanted to make the
program's lists first. Since this whole project has to do with adversity, I wanted to pick lines of poems that had to do with different types of adversity.
It was then that I settled on six main categories and their meanings as listed below:
        1.Love- Love is all about the adversity that people face in love.
        2.Race- Race is about the adversity that many find due to race.
        3.Religion- Religion is about the adversity that religion can bring.
        4.Depression- Depression is about the adversity that people can feel due to their depression.
        5.Neigh-sayers/Bullies(listed in code as Neigh_Bullies)- Neigh_Bullies is about all of the people that can become an obstacle in a person's life, and how they make that person feel.
        6.Break Ups(listed in code as Break_Up)- Break_Up is about all of the feelings and emotions that come with a break-up.
After finding all of the lines that I wanted on www.friendfamilypoems.com in multiple subcategories from the site like: "Life Poems", "Sad Poems", "Death Poems", "Poems on Overcoming Hardship", and "Race";
I then entered that information into Atom as six separate lists. To ensure that the program did recognize them as lists, I proceeded to tell Atom to print each list as it is and the output confirmed that they
indeed, recognized each string.

    The next step for me was to see if I could then enact the random function on the lists that I have. It was then that I imported the random function at the top of the code. The reason why I did this was to
make the code neater since the random function is a global aspect to this code, it made more sense to put it at the top. After I did that I wanted to make sure that random.choice would work with the
lists that I made. So I started off with simply typing in 'print random.choice(love)', which returned a random line from the 'love' list. From there I constructed a print(that is commented out as "proof of concept " on lines 44 and 45)
which printed out a random.choice of each line at once. Once I found that could be done is when I decided to move on to randomizing the lists that would be chosen as well as the number of lines that would be printed.
At first, I had no idea how to do this, and through multiple meetings and countless hours, the professor and I decided that the cleanest way to achieve this was through doing a list that contained the other lists with random.choice already
applied to them. This would not only make things neater, but it also did some work that the definition that I was constructing under it would have had to do otherwise.

    Under this new list, (known as total_choice) I began to construct the definition. I decided to name this definition "poem" simply because I knew that this definition contained everything that was needed to create the poem. This means that
if I saw any problems with the poem construction itself during testing, I knew I needed to look into the poem definition. Inside of this definition, the first thing that I needed to find out was how many lines I wanted the poem to print out
with. Since I wanted that to be randomized as well, I knew that I needed some type of random function. After trying a few and asking the professor when I couldn't find the solution, we found that the cleanest method would be to use the
random.randint() function. In this random.randint() function I decided to put a range of 1-6. The reason why I did this is that I didn't want the poems to be too long, as my poems during my episodes seem to be short and impactful.
The next order of business for my project was to tackle the issue of having some of the lines repeat themselves when they would print. In order to counteract that I needed to put in an empty string that would print out only what was chosen.
I decided to name this empty list "chosen". From there I made the for loop that would iterate through the lists that it was given and append the outcome to the empty chosen list. In this for loop, I created a line_type list that contained the
random choice of the total_choice. I then told the program to append whatever it chose to choose. I then put return chosen to finish the loop. I then printed poem to ensure that it worked and it did.


THE SECOND CHECK

    For the second check I did three main things:
            1. Add a new string to the whole program
            2. Manually formatted the definition's print output
            3. Added a while loop to make the poem print out 12 times only.
    The first thing that I tackled was the output of the definition. As I stated above, I wanted the output to have a poem format. I experimented with many different types of things to try to get the format that I want. After looking at the book again,
I found the .join function which got the print of the poem to be in the overall format that I wanted. I did find a few issues, though. The first thing that I found was that whenever it printed, it seemed to feel like it was unfinished. In order to
rectify that I added a new list to the program entitled "Story". Story contains a list of ending sentences that provide ownership to the poems. This added a whole new level to the individual poems so that they look like a person was actually writing
these poems instead of a generator. The next thing that I wanted to do, which took most of the time, was creating the while loop and having it print out 12 times. This was one of the hardest things for me to do simply because I didn't know where to begin.
After I experimented a little with the names of the loop I decided on days_of_sickness, and later changed it to years_of_sickness. I decided on years_of_sickness because of the fact that I wanted to show how long I have had these illnesses and giving a physical representation
of how long that truly is. I've been suffering from my illnesses for 12 years in a clinical standpoint (diagnosed at 11 years old). After I was able to make it print to twelve, I was able to submit for check two.

FINAL CHANGES

            1. Added in User Interactions via raw-input.
            2. Nested everything in if, elif, else statements.
            3. Used sleep functions to add stylistically.
            4. Altered the while loop to ensure 12 instances of poem() will print.
            5. Added in Helplines and a closing message, all timed.

    This was the largest changes I've made to the program and it was also one of the trickiest parts to do. The first thing that I wanted to make sure that I could do was to add in User Interactions, which the professor seemed really excited for me to implement.
 Since I've only done Boolean true/false statements, I was very nervous about trying to do this. After a lot of research, a lot of questions, and some very unsuccessful attempts I was able to make a test function work, where I asked the program to tell me if someone
could vote or not, based on their age. Once I got that to work I then began to try to get the same code to work on my code. I found that just one of the many places that hung me up was that I had typed in input instead of
raw_input. After I got that to work and register as the starting question I then went on to try to get the program to equate "yes" to ask another raw_input question. After I figured that out I needed to find a way for the program to execute the program 12 times.
This was a little challenge for me but after re-doing the code again I found that my problem was that I didn't put the years_of_sickness in scope that the while loop will recognize. After figuring that out I then needed to construct all of the other possible an-
swers. I found that the best fit to make all of that code neat was to put everything in an if, elif, else statement. That way, I would not only be able to raise the TypeErrors to stop the program if "no" or anything else other than "yes" would be typed in, but I'd
also be able to see everything neatly. I put in TypeErrors in for every time someone answers "no" because of the fact that some of the lines of poems are very heavy and emotional, which I didn't want to trigger anyone. After all of this, when I went to print out the
program I found that it only printed 11 times. I found that because of the previous questions asked, that it needed to compensate for the number of things that printed (since the answer to the previous questions counted as one). In order to rectify this, I changed
years_of_sickness from 1 to 0. This ended up fixing that issue. I then put in international suicide prevention hotlines not only for the safety of others but because they once saved my life. I also put in a few sentences that I wish someone would've said to me
that night that I tried to take my own life. All of these final printouts are timed. The reason why they are timed is that of one of the coping techniques that I learned for my anxiety disorder. I was taught that whenever I feel an anxiety attack coming to count down
from 5. Which is why I put that in the end, as it can create that simple rhythm that has saved me thousands of times.

    One of the things that I made sure to remember to do after I stabilized my moods and learned coping mechanisms was to help others overcome the stigma and almost "shame" of having a mental illness. I wanted to be one of those people that showed that not only could
someone be successful with mental illnesses, but they can also make a difference. I hope I did that with this project. This project was very challenging for me, as I have never touched coding before. I did find that now, I just want to go deeper into it and learn more.
Thank you so much for this opportunity, and to my professor, thank you so much for all of your help. I have all of the sources listed below!

Sources:
www.friendfamilypoems.come
    "Life Poems"
    "Sad Poems"
    "Death Poems"
    "Poems on Overcoming Hardship"
    "Race"
Suicide prevention numbers:
http://ibpf.org/resource/list-international-suicide-hotlines
"List of International Suicide Hotlines"    from the International Bipolar Foundation
