from tkinter import *
import joblib
import pandas as pd
master = Tk()
master.title("Second hand car selling price")
master.geometry('1200x1500')
master.config(bg='orange')
def predict():
    p1 = float(e1.get())
    p2 = float(e2.get())
    p3 = float(e3.get())
    p4 = float(e4.get())
    p5 = float(e5.get())
    p6 = float(e6.get())
    p7 = float(e7.get())
    model = joblib.load('car_price_predictor')
    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven':p2,
        'Fuel_Type': p3,
        'Seller_Type':p4,
        'Transmission':p5 ,
        'Owner':p6 ,
        'Age':p7
    },index=[0])
    result = round(model.predict(data_new)[0])
    Label(master,text="car Selling/Purchasing amount..",
          font=("times",24,'bold')).place(x=200,y=650)
    Label(master,text=str(result),
          font=("times",24,'bold')).place(x=650,y=650)
    print(result)
lable = Label(text="Welcome to Car Price Prediction!",bg='black',
              fg='white',font=("times",24,'bold'))
lable.place(x=500,y=50)
Label(master,text='Present_Price',
      font=("Helvetica",18,'bold')).place(x=200,y=150)
Label(master,text='KMS Driven',
      font=("Helvetica",18,'bold')).place(x=200,y=200)
Label(master,text='Fuel Type',
      font=("Helvetica",18,'bold')).place(x=200,y=250)
Label(master,text='Seller Type',
      font=("Helvetica",18,'bold')).place(x=200,y=300)
Label(master,text='Transmission',
      font=("Helvetica",18,'bold')).place(x=200,y=350)
Label(master,text='Owner',
      font=("Helvetica",18,'bold')).place(x=200,y=400)
Label(master,text='Age',
      font=("Helvetica",18,'bold')).place(x=200,y=450)
e1 = Entry(master,font=("Helvetica",18,'bold'))
e1.place(x=400,y=150)
e2 = Entry(master,font=("Helvetica",18,'bold'))
e2.place(x=400,y=200)
e3 = Entry(master,font=("Helvetica",18,'bold'))
e3.place(x=400,y=250)
e4 = Entry(master,font=("Helvetica",18,'bold'))
e4.place(x=400,y=300)
e5 = Entry(master,font=("Helvetica",18,'bold'))
e5.place(x=400,y=350)
e6 = Entry(master,font=("Helvetica",18,'bold'))
e6.place(x=400,y=400)
e7 = Entry(master,font=("Helvetica",18,'bold'))
e7.place(x=400,y=450)
Button(master,text='predict price',command=predict,
       font=("Helvetica",18,'bold')).place(x=300,y=500)
Button(master,text='Exit',command=master.destroy,
       font=("Helvetica",18,'bold')).place(x=500,y=500)

mainloop()
