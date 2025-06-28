# Joe Melia EET-107
STATE_TAX_RATE = .051
COUNTY_TAX_RATE = .025

def main():
    print('This program will calculate your taxes!\n')

    sale = float(input('How much is the cost of your purchase? '))
    #state_tax needs to be defined and both values need to be assigned as floats
    state_tax = float(calculate_state_tax(sale, STATE_TAX_RATE))
    county_tax = float(calculate_county_tax(COUNTY_TAX_RATE, sale))
    total_cost = sale + state_tax + county_tax

    print('\nSale amount: $', format(sale, '.2f'), sep = '')
    print('State tax  : $', format(state_tax, '.2f'), sep = '')
    print('County tax : $', format(county_tax, '.2f'), sep = '')
    print('Total cost : $', format(total_cost, '.2f'), sep = '')

def calculate_state_tax(sales_amount, tax_rate):
	return(sales_amount * tax_rate)
	
def calculate_county_tax(amount, rate):
	return(amount * rate)
#make this a return instead of random variable 
main()
