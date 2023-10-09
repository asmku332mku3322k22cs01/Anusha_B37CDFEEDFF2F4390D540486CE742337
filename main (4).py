"""
write a function called linear search ptoducts that takes the list of products and target products.
name as input.The function should perform a linear search to find the target product in the list and
return a list of indices of all occurences of the product if found,or an empty list if the product is not
found.
"""


def linearsearchproduct(productlist,targetproduct):
  indices = []

  for index,product in enumerate(productlist):
    if product ==                  targetproduct:
     indices.append(index)

  return indices


#Example usage
product = ["shoes","boot","loafer","shoes","sandals","shoes"]
target="shoes"
target2="apple"
result = linearsearchproduct(product, target)
print(result)

