from constraint import *
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
percent=range(10)
print(percent)
problem = Problem()
def order(a,b):
    return a>=b

def sum_tot_fat(amount, *args):
    print(amount)
    print(args)
    total=0
    for ingredient in args:
        total=total+(ingredient*tot_fat[ingredient])
        print("{}: {}".format(ingredient,tot_fat[ingredient]))
    
    print(total)
    return total==amount

problem.addVariable("water", percent)
problem.addVariable("paprika", percent)
problem.addVariable("coriander", percent)
problem.addVariable("turmeric",  percent)
problem.addVariable("cumin", percent)
problem.addConstraint(ExactSumConstraint(6)) #the total size of the serving - should be 100. 
problem.addConstraint(FunctionConstraint(order), ["water","paprika"])
problem.addConstraint(FunctionConstraint(order), ["paprika","coriander"])
problem.addConstraint(FunctionConstraint(order), ["coriander","turmeric"])
problem.addConstraint(FunctionConstraint(order), ["turmeric","cumin"])

for solution in problem.getSolutions():
    print(solution)

print(order("water","cumin"))

print(sum_tot_fat(44,"water","paprika","coriander"))
