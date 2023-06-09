class ShoppingCart:
	def __init__(self,qpa,qpb,qpc):
		self.quantity_of_productA=qpa
		self.quantity_of_productB=qpb
		self.quantity_of_productC=qpc	
		self.shipping_fee=0

	def sub_total(self,qwf):
		self.total_of_productA=20*qpa
		self.total_of_productB=40*qpb
		self.total_of_productC=50*qpc
		self.sub_total=self.total_of_productA+self.total_of_productB+self.total_of_productC
		self.total_unit=qpa+qpb+qpc
		if self.total_unit%10==0:
			self.shipping_charge=(self.total_unit//10)*5
		else:
			self.shipping_charge=(self.total_unit//10)*5+5			
		if qwf=="yes":
			self.wrapping_charge=self.total_unit*1
		else:
			self.wrapping_charge=0
	
	def discount_rule(self):
		discount1=0
		discount2=0
		discount3=0
		discount4=0
		if self.sub_total>200:
			discount1=self.sub_total*0.1
		discount_a=0
		discount_b=0
		discount_c=0
		if self.quantity_of_productA>10:	
			discount_a=self.total_of_productA*0.05
		if self.quantity_of_productB>10:	
			discount_b=self.total_of_productB*0.05
		if self.quantity_of_productC>10:	
			discount_c=self.total_of_productC*0.05
		discount2=discount_a+discount_b+discount_c
		if self.total_unit>20:
			discount3=self.sub_total*0.1
		if self.total_unit>30:
			if self.quantity_of_productA>15:
				discount_1a=(20*15)+((self.quantity_of_productA-15)*20*0.5)
			if self.quantity_of_productB>15:
				discount_1b=(40*15)+((self.quantity_of_productB-15)*40*0.5)
			if self.quantity_of_productA>15:
				discount_1c=(20*15)+((self.quantity_of_productA-15)*20*0.5)
			discount4=discount_a+discount_b+discount_c
		if discount1>discount2 and discount1>discount2 and discount1>discount3:
			self.selected_discount=discount1
			self.discount_selected="flat 10% discount"
		elif discount2>discount1 and discount2>discount3 and discount2>discount4:
			self.selected_discount=discount2
			self.discount_selected="bulk 5% discount"
		elif discount3>discount1 and discount3>discount2 and discount3>discount4:
			self.selected_discount=discount3
			self.discount_selected="bulk 10% discount"
		else:
			self.selected_discount=discount4
			self.discount_selected="tiered 50% discount"
		self.net_total=self.sub_total+self.wrapping_charge+self.shipping_charge-self.selected_discount
	def display(self):
		print("Product A								:",self.quantity_of_productA)
		print("Product B								:",self.quantity_of_productB)
		print("Product C								:",self.quantity_of_productC)
		print("Total of Product A						:",self.total_of_productA)
		print("Total of Product B						:",self.total_of_productB)
		print("Total of Product C						:",self.total_of_productC)
		print("Sub Total								:",self.sub_total)
		print("Gift wrapping charge						:",self.wrapping_charge)
		print("Shipping charge							:",self.shipping_charge)
		print("Discount selected						:",self.discount_selected)
		print("Discount 								:",self.selected_discount)
		print("-------------------------------------------------------------")
		print("Net charge 							:",self.net_total)

qpa=int(input("Enter the quantity of product A:"))
qpb=int(input("Enter the quantity of product B:"))
qpc=int(input("Enter the quantity of product C:"))
qwf=input("Product is wrapped as gift(yes/no)")
shpng_crt=ShoppingCart(qpa,qpb,qpc)
shpng_crt.sub_total(qwf)
shpng_crt.discount_rule()
shpng_crt.display()
