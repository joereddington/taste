from random import randint


def move(ingredients,amount):
    giver=0
    taker=0
    while (giver==taker):
        giver=randint(0,len(ingredients.keys())-1)
        taker=randint(0,len(ingredients.keys())-1)
        
    print("{} {}".format(giver,taker))
    old_fitness=fitness(ingredients)
    giver_name=list(ingredients)[giver]
    taker_name=list(ingredients)[taker]
    ingredients[giver_name]-=amount
    ingredients[taker_name]+=amount
    new_fitness=fitness(ingredients)
    print("Old fitness was {:.2f} and new fitness is {:.2f}".format(old_fitness,new_fitness))
    if old_fitness<new_fitness:
        ingredients[giver_name]+=amount
        ingredients[taker_name]-=amount
        


def fitness(ingredients):
    total=0
    #I really want a least squares error but we'll get there. 
    total=total+tot_fat_target-total_up(ingredients,tot_fat)
    total=total+sat_fat_target-total_up(ingredients,sat_fat)
    return abs(total) # we only want positive numbers


def total_up(ingredients,attribute):
    total=0
    for key in ingredients.keys():
        amount=ingredients[key]*attribute[key]/100 #the 100 is because the values are stored as grams per 100 rather than a decimal percentage
        total+=amount
#        print("There is {}g of {}, which is {} percent important, for a total of {}".format(ingredients[key],key,attribute[key],amount))
    return total


tot_fat={}
tot_fat['water']=0
tot_fat['paprika']=13
tot_fat['coriander']=0.5
tot_fat['turmeric']=10
tot_fat['cumin']=22
tot_fat['fennel']=0.2
tot_fat['cloves']=0
tot_fat['rapeseed_oil']=100
tot_fat['salt']=0
tot_fat['maize_flour']=0
tot_fat['acetic_acid']=0
tot_fat['citric_acid']=0
tot_fat['tamarind']=0
tot_fat['garlic_powder']=0
sat_fat={}
sat_fat['water']=0
sat_fat['paprika']=2.1
sat_fat['coriander']=0.52 
sat_fat['turmeric']=3.1
sat_fat['cumin']=1.5
sat_fat['fennel']=0
sat_fat['cloves']=0
sat_fat['rapeseed_oil']=8
sat_fat['salt']=0
sat_fat['maize_flour']=0
sat_fat['acetic_acid']=0
sat_fat['citric_acid']=0
sat_fat['tamarind']=0
sat_fat['garlic_powder']=0

serving_size=100  #sometimes would be 30 or similar 
step_size=1 #for the start 
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
ingredients['salt']=0
ingredients['maize_flour']=0
ingredients['acetic_acid']=0
ingredients['citric_acid']=0
ingredients['tamarind']=0
ingredients['garlic_powder']=0

tot_fat_target=22.3
sat_fat_target=1.7
initial_value=serving_size/len(ingredients.keys())
print("The initial value is {:.3f}g".format(initial_value))
for key in ingredients.keys():
    ingredients[key]=initial_value

print(fitness(ingredients))

for x in range(1000):
    step_size=step_size-0.001
    move(ingredients,step_size)

print("The Final Ingredients are:")

for ingredient in ingredients:
    print("{} - {:.3f}g".format(ingredient,ingredients[ingredient]))




