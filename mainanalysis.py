rprice = []
price = []
niprice = []
bing = []
bingcured = []
values = []
import matplotlib.pyplot as plt
with open('output.txt',encoding = 'utf8') as oh:
    for line in oh:
        bing.append(line)
for i in range(1,len(bing)):
    x = bing[i].split()
    if len(x) > 5 and x[2] == 'sold' and x[4] == 'Enchanted':
        niprice.append(x[9])
        print(x)
print(niprice)
for i in niprice:
	if i[0] == '$':
		price.append(i)			
print(price)
for i in range(0,len(price)):
    rprice.append(price[i].replace(',', '').replace('$', ''))
    values.append(int(x[3].replace('x','')))
for i in range(0,len(rprice)):
	rprice[i] = round(float(rprice[i]))/values[i]
rprice.reverse()
plt.style.use('ggplot')
z= []
for i in range(0,len(rprice)):
	z.append(i)

plt.plot(rprice, alpha=0.4)
print(rprice)
plt.show()
