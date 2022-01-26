class Category:
  def __init__(self, name: str) -> None:
    self.name = name
    self.ledger = []
    self.balance = 0.0
    self.spending = 0.0
  
  def deposit(self, amount, description: str = '') -> None:
    new_entry = {"amount": amount, "description": description}
    self.ledger.append(new_entry)
    self.balance += amount

  def withdraw(self, amount, description: str = '') -> bool:
    if self.check_funds(amount) is False:
      return False
    new_entry = {"amount": -amount, "description": description}
    self.ledger.append(new_entry)
    self.balance -= amount
    self.spending += amount
    return True

  def get_balance(self) -> float:
    return self.balance
  
  def transfer(self, amount, category) -> bool:
    if self.check_funds(amount) is False:
      return False
    self.withdraw(amount, f'Transfer to {category.name}')
    category.deposit(amount, f'Transfer from {self.name}')
    return True
  
  def check_funds(self, amount) -> bool:
    return self.balance >= amount

  def __str__(self):
    money_format = "{:.2f}"
    title = self.name.center(30, '*')
    output_string = title
    for entry in self.ledger:
      left_side = entry["description"][:23].ljust(23)
      right_side = money_format.format(entry["amount"]).rjust(7)
      output_string += '\n' + left_side + right_side
    total = "Total: {:.2f}".format(self.balance)
    output_string += '\n' + total
    return output_string

def create_spend_chart(categories) -> str:
  output = 'Percentage spent by category'
  total = 0
  graph_data = []
  for category in categories:
    total += category.spending
  max_length = 0
  for category in categories:
    pct_spending = category.spending / total
    graph_data.append({"desc": category.name, "pct": pct_spending})
    max_length = max(max_length, len(category.name))

  #have the info now I need to create the graph, yahoo!
  for i in range(100, -1, -10):
    line = f'{str(i).rjust(3)}|'
    for k in range(0, len(graph_data)):
      line += 'o'.center(3) if i < graph_data[k]["pct"] * 100 else ''.center(3)
    output += '\n' + line + ' '
  output += '\n' + ' ' * 4 + '---' * len(graph_data) + '-'
  for x in range(0, max_length):
    line = ' ' * 4
    for i in range(0, len(graph_data)):
      description = graph_data[i]["desc"]
      if len(description) > x:
        line += description[x].center(3)
      else:
        line += ''.center(3)
    output += '\n' + line + ' '
  return output