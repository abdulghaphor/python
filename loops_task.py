items = {
	"apple" : 1,
	"orange" : 0.5,
	"chocolate" : 0.75,
	"sandwich" : 1.5
}
print("### Welcome Hapoopi to Baqala House!")
for item in items:
	print("### item: %s, price: %s" % (item,items[item]))
x = "start"
cart = {}
while x:
	x = input("Item please: ")
	if x in items:
		t = input("Quantity please: ")
		if t.isdigit() == True:
			cart[x] = int(t)
	elif x == "done":
		print("# Thank You for Shopping with us")
		print("----- RECEIPT -----")
		m = 0
		for c in cart:
			print("%s %s: %s" % (cart[c],c,cart[c]*items[c]))
			m += cart[c]*items[c]
		print("TOTAL:",m)
		break
	else:
		print("invalid entry")
		continue