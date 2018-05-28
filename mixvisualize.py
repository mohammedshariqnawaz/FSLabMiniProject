
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.size'] = 9.0

arr=[]
data = pd.read_csv("kc_house_data.csv")
data2= pd.read_csv("datafile.csv")
data3=pd.read_csv("houseShortage.csv")
while(1):
	print("Choose the parameters to visualize\n")
	print(" 1v-Bedrooms vs count based on current geo location\n 2v-Price vs Latitude based on current geo location \n 3v-Price vs Square Feet \n 4v-Bedroom vs price based on current geo location\n 5v-Price vs location( Based on postal code)\n 6v-Know your scheme based on Gov. of India \n 7v-State vs Estimated number of households in India\n 8v-Housing 2012 (India)\n key board interrupt-exit\n")
	vch=input("enter the choice\n")
	if(vch=="1v"):
		data['bedrooms'].value_counts().plot(kind='bar')
		plt.title('number of Bedroom')
		plt.xlabel('Bedrooms')
		plt.ylabel('Count')
		sns.despine
		plt.show()
	elif(vch=="2v"):
		plt.scatter(data.price,data.lat)
		plt.xlabel("Price")
		plt.ylabel('Latitude')
		plt.title("Latitude vs Price")
		plt.show()

	elif(vch=="3v"):
		plt.scatter(data.price,data.sqft_living)
		plt.title("Price vs Square Feet")
		plt.show()

	elif(vch=="4v"):
		plt.scatter(data.bedrooms,data.price)
		plt.title("Bedroom and Price ")
		plt.xlabel("Bedrooms")
		plt.ylabel("Price")
		plt.show()
		sns.despine
		plt.show()

	elif(vch=="5v"):
		plt.scatter(data.zipcode,data.price)
		plt.title("Which is the pricey location by zipcode?")
		plt.show()

	elif(vch=="6v"):
		plt.scatter(data2.Started_in,data2.Name_of_the_Scheme)
		plt.title("Housing schemes in India")
		plt.show()
	elif(vch=="7v"):
		N = data3.Name_State.count()
		print(N)
		ind = np.arange(N)
		width = 0.22
		plt.bar(ind, data3.Estimated_households_BPL_Urban, width, label='Houses below poverty line')
		plt.bar(ind + width,data3.Number_Katcha_households, width,
		    label=' katcha houses')

		plt.ylabel('Hoseholds')
		plt.xlabel('States')
		plt.title('State vs Estimated number of households')

		plt.xticks(ind + width / 2,data3.Name_State )
		plt.legend(loc='best')
		plt.show()

	elif(vch=="8v"):
		labels = data3.Name_State
		sizes = data3.State_wise_Dist_Housing_shortage2012_inMllions
		#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
		        shadow=False, startangle=4,pctdistance=1.1, labeldistance=1.2)
		ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
		plt.title("Housing 2012")
		plt.show()


	else:
		exit()
