from tkinter import *
from tkinter import ttk
from data import *
from tkinter import messagebox

def exportar():
    
    strMonedas=grabarMonedas(scrapping_tipoCambio())
    fw=open('monedas.csv','w')
    fw.write(strMonedas)
    fw.close()
    messagebox.showinfo("Informacion","Se ha exportado correctamente")
    

app = Tk()
app.geometry('610x300')

app.title('Tipos de cambios')

tree = ttk.Treeview(app)
tree['columns'] = ('Moneda','Compra','Venta')

tree.column('#0',width=0,stretch=NO)
tree.column('Moneda')
tree.column('Compra')
tree.column('Venta')

tree.heading('#0',text='id')
tree.heading('Moneda',text='Moneda')
tree.heading('Compra',text='Precio Compra')
tree.heading('Venta',text='Precio Venta')

tree.grid(row=0,column=0)

#boton
btnSaludo = Button(app,text='Exportar CSV',command=exportar)
btnSaludo.grid(row=1,column=0)

        
#insertar datos
for contador in range(0,len(scrapping_tipoCambio())):  

    moneda=''
    precioCompra=''
    precioVenta=''

    for clave,valor in scrapping_tipoCambio()[contador].items():
        if(clave=='moneda'):
            moneda=valor
        elif(clave=='compra'):
            precioCompra=valor
        else:
            precioVenta=valor
            	
    tree.insert('',END,contador,values=(moneda,precioCompra,precioVenta),text='01')
   
app.mainloop()