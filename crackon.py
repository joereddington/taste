from random import randint


def inorder(ingredients):
    in_list=list(ingredients)
    for i in range(len(in_list)-1):
        first=in_list[i]
        second=in_list[i+1]
        if ingredients[first]<ingredients[second]:
#            print("Error: there shouldn't be less {}({}) than {}({})".format(first,ingredients[first],second,ingredients[second]))
            return False
    return True

def move(ingredients,amount):
    giver=randint(0,len(ingredients.keys())-1)
    taker=randint(0,len(ingredients.keys())-1)
    old_fitness=fitness(ingredients)
    giver_name=list(ingredients)[giver]
    taker_name=list(ingredients)[taker]
    ingredients[giver_name]-=amount
    ingredients[taker_name]+=amount
    if ingredients[giver_name]<0: #taker is never going to be below zero
        ingredients[giver_name]+=amount
        ingredients[taker_name]-=amount
        return
    new_fitness=fitness(ingredients)
#    print("Old fitness was {:.2f} and new fitness is {:.2f}".format(old_fitness,new_fitness))
    if old_fitness<new_fitness:
        ingredients[giver_name]+=amount
        ingredients[taker_name]-=amount
        


def fitness(ingredients):
    total=0
    #I really want a least squares error but we'll get there. 
    total=total+abs(tot_fat_target-total_up(ingredients,tot_fat))
    total=total+abs(sat_fat_target-total_up(ingredients,sat_fat))
    total=total+abs(carb_target-total_up(ingredients,carb))
    total=total+abs(sugar_target-total_up(ingredients,sugar))
    total=total+abs(sugar_target-total_up(ingredients,protein))
    return abs(total) # we only want positive numbers


def total_up(ingredients,attribute):
    total=0
    for key in ingredients.keys():
        amount=ingredients[key]*attribute[key]/100 #the 100 is because the values are stored as grams per 100 rather than a decimal percentage
        total+=amount
#        print("There is {}g of {}, which is {} percent important, for a total of {}".format(ingredients[key],key,attribute[key],amount))
    return abs(total)

protein={}
protein['water']=0
protein['paprika']=14
protein['coriander']=2.1
protein['turmeric']=7.8
protein['cumin']=18
protein['fennel']=1.2
protein['cloves']=6
protein['rapeseed_oil']=0
protein['salt']=0
protein['maize_flour']=7
protein['acetic_acid']=0
protein['citric_acid']=0
protein['tamarind']=0
sugar={}
sugar['water']=0
sugar['paprika']=10
sugar['coriander']=0.9
sugar['turmeric']=3.2
sugar['cumin']=2.3
sugar['fennel']=0
sugar['cloves']=2.4
sugar['rapeseed_oil']=0
sugar['salt']=0
sugar['maize_flour']=1.6
sugar['acetic_acid']=0
sugar['citric_acid']=0
sugar['tamarind']=0
carb={}
carb['water']=0
carb['paprika']=54
carb['coriander']=0.9
carb['turmeric']=64.9
carb['cumin']=44
carb['fennel']=7
carb['cloves']=66
carb['rapeseed_oil']=0
carb['salt']=0
carb['maize_flour']=79
carb['acetic_acid']=0
carb['citric_acid']=0
carb['tamarind']=0

tot_fat={}
tot_fat['water']=0
tot_fat['paprika']=13
tot_fat['coriander']=0.5
tot_fat['turmeric']=10
tot_fat['cumin']=22
tot_fat['fennel']=0.2
tot_fat['cloves']=13
tot_fat['rapeseed_oil']=100
tot_fat['salt']=0
tot_fat['maize_flour']=1.8
tot_fat['acetic_acid']=0
tot_fat['citric_acid']=0
tot_fat['tamarind']=0
sat_fat={}
sat_fat['water']=0
sat_fat['paprika']=2.1
sat_fat['coriander']=0.52 
sat_fat['turmeric']=3.1
sat_fat['cumin']=1.5
sat_fat['fennel']=0
sat_fat['cloves']=4
sat_fat['rapeseed_oil']=8
sat_fat['salt']=0
sat_fat['maize_flour']=0.2
sat_fat['acetic_acid']=1000
sat_fat['citric_acid']=1000
sat_fat['tamarind']=1000

serving_size=100  #sometimes would be 30 or similar 
step_size=3 #for the start 
ingredients={}
ingredients
ingredients['water']=0
ingredients['paprika']=0
ingredients['coriander']=0
ingredients['turmeric']=0
ingredients['cumin']=0
ingredients['fennel']=0
ingredients['cloves']=0
ingredients['rapeseed_oil']=0
ingredients['maize_flour']=0

tot_fat_target=22.3
sat_fat_target=1.7
carb_target=6.5
sugar_target=0.7
protein_target=3.4

initial_value=serving_size/len(ingredients.keys())
print("The initial value is {:.3f}g".format(initial_value))
for key in ingredients.keys():
    ingredients[key]=initial_value
ingredients['water']+=1
ingredients['maize_flour']-=1

print(fitness(ingredients))

trials=10000
change_in_step=step_size/trials
for x in range(trials):
    step_size=step_size-change_in_step
    move(ingredients,step_size)

print("The Final Ingredients are:")

for ingredient in ingredients:
    print("{} - {:.3f}g".format(ingredient,ingredients[ingredient]))

print(fitness(ingredients))

print("Fat target was {}, and we have {}".format(tot_fat_target,total_up(ingredients,tot_fat)))
print("Sat Fat target was {}, and we have {}".format(sat_fat_target,total_up(ingredients,sat_fat)))
print("Carb target was {}, and we have {}".format(carb_target,total_up(ingredients,carb)))
print("Sugar target was {}, and we have {}".format(sugar_target,total_up(ingredients,sugar)))
print("Protein target was {}, and we have {}".format(protein_target,total_up(ingredients,protein)))

