import random
print("VERY WARM WELCOME BY GOD OF FIRE")
print("Rock , Paper , Scissors")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
while True:
    player=input("Enter R, P or S: \n")
    player=player.upper()
    cpu=str(random.randint(1,3))
    if(cpu=='1'):
        cpu= 'R'
    elif(cpu== '2'):
        cpu= 'P'
    else:
        cpu= 'S'
    if(player=='R' or player=='P' or player=='S'):
        if((player=='R' and cpu=='S') or (player== 'P' and cpu=='R') or (player=='S' and cpu=='P')):
            print("CPU: " + cpu)
            print("PLAYER: " + player)
            print("\nYou Won ")
        elif (player==cpu):
            print("CPU: " + cpu)
            print("PLAYER: " + player)
            print("\nMatch Draw ")
        else:
            print("CPU: " + cpu)
            print("PLAYER: " + player)
            print("\nCPU Won ")
    

    else:
        print("Please try again.")