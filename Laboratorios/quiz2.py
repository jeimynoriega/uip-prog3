#quiz2

descuento1 = 0.35
descuento2 = 0.20
descuento3 = 0.10

comprador = 0
	while comprador < 5 ;
	monto = int(int(input("ingresar monto:"))
	comprador +=1
	if (monto >= 500):
	subtotal1 = monto * descuento1
	total = monto - subtotal1
	print("el total es {0}:".format(total))
	elif (monto < 500 and monto >= 200):
	subtotal1 = monto * descuento2
	total = monto * subtotal
	print("el total es {0}:".format(total)
elif monto < 200 and monto >= 100 :
	subtotal = monto * descuento3
	total = monto * subtotal 
	print("el total es {0}".format(total)
else:
	print("no hay descuento \n gracias por su compra")
