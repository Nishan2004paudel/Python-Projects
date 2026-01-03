from time import time 



def typerror(prompt):
    global inwords 
    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else: 
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1]==words[i+1])& (inwords[i-1]==words[i-1]):
                    continue
                else:
                    errors +=1
            else:
                errors +=1
    return errors
    
def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed= twords / time  

    return speed

def elapsedtime(stime, etime):
    time = etime - stime
    return time

if __name__ == '__main__':
    prompt = "Nepal is beautiful country. It is situated between india and china. Nepal consists of 77 disticts and 7 states. World's highest mountain: Mount Everest, also known as Sagarmatha is situated in Nepal. Current prime minister of Nepal is Sushila Karki."
    print("Type this:- '", prompt, "'")

          
    input("Press Enter when you are ready to check your speed !!!")

    stime = time()

    inprompt = input()
    etime = time()


    time = round(elapsedtime(stime, etime),2)

    speed = speed(inprompt,stime, etime)

    errors = typerror(prompt)
     
    print("############################################")
    print("Total time elapsed: ", time, "seconds")
    print("Your Average Typing speed was ", speed, "words per minute (w/m)")

    print("with the total of ", errors, "errors ")

    print("#######################################3")