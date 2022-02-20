
meal_cost = float(input().strip())

tip_percent = int(input().strip())

tax_percent = int(input().strip())

        
tip_percent =  meal_cost/100*20    
tax_percent =   + meal_cost/100*8
ft = tip_percent + tax_percent + meal_cost
print(int(round(ft)))
