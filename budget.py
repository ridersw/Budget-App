class Category:
	def __init__(self, name):
		self.name = name
		self.ledger = []
		self.totalAmount = 0
		
	def deposit(self, amount, description="" ):
		self.ledger.append({'amount': (amount), 'description': description})
		#print("ledger: ",self.ledger)
		self.totalAmount += amount
		
	def withdraw(self, amount, description=""):
		if amount < self.totalAmount:
			self.ledger.append({'amount': -(amount), 'description': description})
			self.totalAmount -= amount
			return True
		else:
			return False
			
	def get_balance(self):
		return self.totalAmount
		
	def transfer(self, amount, obj):
		if amount < self.totalAmount:
			description = "Transfer to " + str(obj.name)
			self.withdraw(amount, description)
			description = "Transfer from " + str(self.name)
			obj.deposit(amount, description)
			return True
		else:
			return False	
	
	def check_funds(self, amount):
		if amount <= self.totalAmount:
			return True
		else:
			return False
			
	def __str__(self):
		name = self.name
		s = name.center(30,"*")
		for items in self.ledger:
			try:
				left = items['description'][0:23]
			except TypeError:
				left=''
			right = str("{:.2f}".format(items['amount']))
			s+= f"\n{left:<23}{right:>7}"
		s += "\nTotal: "+ str(self.get_balance())
		return s
	
def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for name in categories:
    total = 0
    for item in name.ledger:
      if item['amount'] < 0:
        total = total- item['amount']
    spent.append(round(total, 2))
    category_names.append(name.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "

    

  return(graph)
	