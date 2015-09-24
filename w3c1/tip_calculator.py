def calculate_tip(total_bill) :
	return total_bill * 0.2;


bill_amt = 42.50
print "Bill of %.2f: %.2f" % (bill_amt, calculate_tip(bill_amt))
bill_amt = 40.0
print "Bill of %.2f: %.2f" % (bill_amt, calculate_tip(bill_amt))
bill_amt = 110.0
print "Bill of %.2f: %.2f" % (bill_amt, calculate_tip(bill_amt))

def calculate_tip2(total_bill, tip_percent):
    return total_bill * tip_percent

bill_amt = 42.50
tip_amt = .2
print "Bill of %.2f with tip of %.2f: %.2f" % (bill_amt, tip_amt, calculate_tip2(bill_amt, tip_amt))
bill_amt = 40.0
tip_amt = .1
print "Bill of %.2f with tip of %.2f: %.2f" % (bill_amt, tip_amt, calculate_tip2(bill_amt, tip_amt))
bill_amt = 110.0
tip_amt = .6
print "Bill of %.2f with tip of %.2f: %.2f" % (bill_amt, tip_amt, calculate_tip2(bill_amt, tip_amt))

def tip_with_friends(total_bill, tip_percent, num_friends):
	return (total_bill * tip_percent) / num_friends

bill_amt = 42.50
tip_pct = 0.2
friends = 2
print_args = (bill_amt, tip_pct, friends, tip_with_friends(bill_amt, tip_pct, friends))
print "$%.2f bill with a %.2f tip split between %i friends is: %0.2f" % print_args

bill_amt = 40.0
tip_pct = 0.1
friends = 4
print_args = (bill_amt, tip_pct, friends, tip_with_friends(bill_amt, tip_pct, friends))
print "$%.2f bill with a %.2f tip split between %i friends is: %0.2f" % print_args

bill_amt = 110.0
tip_pct = 0.6
friends = 3
print_args = (bill_amt, tip_pct, friends, tip_with_friends(bill_amt, tip_pct, friends))
print "$%.2f bill with a %.2f tip split between %i friends is: %0.2f" % print_args