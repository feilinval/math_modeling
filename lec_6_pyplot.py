import matplotlib.pyplot as plt  #Импорт модуля pyplot
plt.plot([1,2,3],[5,7,10]) #plot - команда
plt.show()

x=[3,4,5]
y=[40,10,30]
plt.plot(x,y,color="g",label="luchte",marker=">",ms=5)

plt.xlabel("Coord: x") 
plt.ylabel("Coord: y")
plt.legend()
plt.show()
