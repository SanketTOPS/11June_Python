"""import requests
import pandas

url="https://fakestoreapi.com/products/"

req=requests.get(url)

data=req.json()
#print(data)

pd=pandas.DataFrame(data)

print(pd[['id','title','price']])
"""


import requests
import pandas

url = "https://fakestoreapi.com/products/"
req = requests.get(url)
data = req.json()

pd = pandas.DataFrame(data)

# Rename columns

pd.rename(columns={'id':'pid','title': 'pname','price':'pr.price'}, inplace=True)

# Print selected columns with renamed column
print(pd[['pid', 'pname', 'pr.price']])
