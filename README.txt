Taste: 

Deducing ingredient amounts from nutritional information. 


Given ten ingredients, which have different values for Fat, Protein and Carbs, Find the mix that correctly finds Fat protein and Carbs for the whole food. 

This is clearly a specialised form of constraint satisfaction. 


This was my stackexchange question: https://softwarerecs.stackexchange.com/questions/79729/i-want-to-deduce-recipes-from-commercial-food-packaging?noredirect=1#comment97630_79729


This is the library I'm trying: https://pypi.org/project/python-constraint/


## 30/06/21 08:10 to 08:28, First go.
What's the first thing I want to try?  


Hummous has 9 https://www.ocado.com/products/ocado-houmous-56648011
Dressing has 8 https://www.tesco.com/groceries/en-GB/products/292613583

No, let's do the one we have, but only for 'Fat' for now. 

## 30/06/21 09:16, 
Okay, so I have a problem with the function constraint.  When used in the solver it's passed integers.  But I want to pass attributes 


## 30/06/21 09:29, Okay but this should be easy I just want to be able to say "This variable has two..." 

Wait...   

I can do them, because I can have an exact match between water fat and water satfat

## 01/07/21 06:14, Okay, I'm looking at the constraint satisfaction algorithms and I think 'roll your own is' correct. 

The constraint satisfaction algorithms involve a work list for re-processing all affected notes - however our f/c/p checks will affect all nodes it would be a waste to write that. 

Also, every time we add a gram to something we take it from somewhere else. 


Wait.... 

Assign 100 grams across the ingredients (equally).  Work out the nutrition. randomly choose one of the ingredients to take a gram from, and to give that gram to (obviously only allowing it to be in the order). See if that improves the nutrition. Do that 1000 times, and then do it for 0.1 of a gram for a 1000 times.    

This is effectively simulated annealing. And there is a 'goodness function' which is effectively 'how close are we to a perfect nutrition match'.  

Okay, so what are our tests?  

We'll need a class.  

How do I store these when I read them. Or go through.hhmmm.   

## 01/07/21 06:43, 
Okay so I can write totalls. 
I now need an overall value function. And then the ability to swap grams sometimes.  


## 01/07/21 06:55, Okay, so you have to have an order check, because otherwise you can't backtrack at all. (or, you have to have explicit backtracking)  


## 01/07/21 07:22, I've added carbs, sugars and protein, but I'm getting wildly different values even after 10000 runs 


## 01/07/21 07:56, So here is the problem about inorder -There is exactly one move first (which comes up rarely) then two possible moves after tat. 

## 01/07/21 08:17, Okay, I've solved a bunch of bugs, feel pleased with that. 

# TODO 
* Add the ordering constraints
* Add fixing the rest of the numbers 



















