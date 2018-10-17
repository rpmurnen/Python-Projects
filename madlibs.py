# Mad Libs! in python

def mad_libs():
    x = input('ready to play!? y/n')
    if str.lower(x) in ('yes','y'):
        writing = True
        while writing == True:
            first_noun = input('input a location')
            second_noun = input('input a noun')


            first_adjective = input('input an adjective')
            second_adjective = input('input an adjective')


            first_verb = input('input a verb')
            second_verb = input('input a verb')
            third_verb = input('input a verb')
            
            
            print('when you ' +first_verb + ' to ' + first_noun+ ', it is important to ' + second_verb + '. people there are likely to want to '+ third_verb +' you in a way that most people would describe as '+ first_adjective+'. But, if you remember to keep things '+second_adjective+' , all will be well!')


            y = input('Play again!?'' y/n')
            if str.lower(y) not in ('yes','y'):
                writing = False

mad_libs()

