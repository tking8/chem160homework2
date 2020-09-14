from random import choices
ntrials=15000
player1wins=0
ndice1=3
ndice2=2
for i in range(ntrials):
    dice2=choices(range(1,7),k=ndice2)
    dice2.sort(reverse=True)
    if dice2[0]==dice2[1]:
        continue
    dice1=choices(range(1,7),k=ndice1)
    dice1.sort(reverse=True)
    if (dice1[0]+dice1[1])>(dice2[0]+dice2[1]):
        player1wins=player1wins+1
print(player1wins/ntrials)