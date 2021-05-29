#tkinter
#Operators
#Data Types and its methods 
#Inbuilt library as time,date-time,random

from tkinter import *
from tkinter import ttk #for Combobox
import random
import time
import datetime

#creating window object
root=Tk()
root.geometry("1350x850") #size of frame
root.title("BOOKING SYSTEM") #window name
root.configure(background="dark blue")

#To exit windows bases application
def Exit():
  qExit=messagebox.askyesno("Trip Booking System","Do you want to exit the system")
  if qExit> 0:
    root.destroy()
    return

def Reset():          #combined with reset button
  TicketNum.set('')
  Tax.set('')
  SubTotal.set('')
  TotalCost.set('')
  CustomerName.set('')
  CustomerMob.set('')
  CustomerEmail.set('')
  TimeOfOrder.set('')
  DateOfOrder.set('')
  CostOFAdult.set(0)
  CostOfChild.set(0)
  CostOfSenior.set(0)
  CostOfConcession.set(0)         #for prime user
  UnitPriceAdult.set(0)
  UnitPriceChild.set(0)
  UnitPriceSenior.set(0)
  UnitPriceConcession(0)
  QtyAdult.set(0)
  QtyChild.set(0)
  QtySenior.set(0)
  QtyConcession.set(0)
  CardNum.set('')
  CardValidity.set('')
  Discount.set(0)
  cmdMethodOfPayment.set('Other')          #dropdown

def Ticketref():           #creating ref no. of the ticket
  Refpay=random.randint(10300,709467)     #create a random ticket no.
  Refpaid=('ORD'+str(Refpay))
  TicketNum.set(Refpaid)

def CostOfOrder():
  Qty1=float(QtyAdult.get())
  Qty2=float(QtyChild.get())
  Qty3=float(QtySenior.get())
  Qty4=float(QtyConcession.get())

  UnitPrice1=float(UnitPriceAdult.get())
  UnitPrice2=float(UnitPriceChild.get())
  UnitPrice3=float(UnitPriceSenior.get())
  UnitPrice4=float(UnitPriceConcession.get())

  CostOfCategory1='$ '+str('%.2f'%(Qty1*UnitPrice1))
  CostOfCategory2='$ '+str('%.2f'%(Qty2*UnitPrice2))
  CostOfCategory3='$ '+str('%.2f'%(Qty3*UnitPrice3))
  CostOfCategory4='$ '+str('%.2f'%(Qty4*UnitPrice4))
  
  CostOfAdult.set(CostOfCategory1)
  CostOfChild.set(CostOfCategory2)
  CostOfSenior.set(CostOfCategory3)
  CostOfConcession.set(CostOfCategory4)

  AllItemCost=((Qty1*UnitPrice1)+(Qty2*UnitPrice2)+(Qty3*UnitPrice3)+(Qty4*UnitPrice4))
  AppliedDiscount=float(Discount.get())
  DiscountOnAllItem=(AllItemCost*(AppliedDiscount/100))
  CostAfterDiscount=AllItemCost-DiscountOnAllItem

  TaxOnAllItem='$ '+str('%.2f'%((CostAfterDiscount)*0.05))
  Tax.set(TaxOnAllItem)

  SubTotalp='$ '+str('%.2f'%(AllItemCost)) 
  SubTotal.set(SubTotalp)

  TotalCostp='$ '+str('%.2f'%(CostAfterDiscount+((CostAfterDiscount)*0.05))) 
  TotalCost.set(TotalCostp)

  Ticketref()
  return 

def TicketReceipt():
  root1=Tk()             #creating Receipt window
  root1.geometry("500x390")
  root1.title("Trip Ticket Receipt")
  root1.configure(background="light blue")

txtTicketDetail=Text(root1,font=('arial',10,'bold'),fg='dark blue',bg='light yellow')
txtTicketDetail.grid(row=0,column=0)

txtTicketDetail.insert(END,''+'\n')
txtTicketDetail.insert(END,"CustomerName:"+CustomerName.get()+"\t\t\t\t"+'Mob:'+CustomerMob.get()+'\t\t'+"Email:"+CustomerEmail.get()+'\n')
txtTicketDetail.insert(END,"Ticket No:"+TicketNum.get()+'\t\t\t\t'+'Time:'+TimeOfOrder.get()+'\t\t'+"Date:"+DateOfOrder.get()+'\n')
txtTicketDetail.insert(END,'=========================================================================================================='+'\n')

txtTicketDetail.insert(END,"Ticket Category:\t\t\t"+'Qty:\t\t\t'+"UnitPrice:\t\t\t"+'\n')
txtTicketDetail.insert(END,'Adult:\t\t\t'+QtyAdult.get()+'\t\t\t'+UnitPriceAdult.get()+'\t\t\t'+'\n')
txtTicketDetail.insert(END,'\t\t\t\t'+'====================================='+'\n')
txtTicketDetail.insert(END,'\t\t\t\t'+'Total Price: \t'+CostOfAdult.get()+'\n')

txtTicketDetail.insert(END,'Child:\t\t\t'+QtyChild.get()+'\t\t\t'+UnitPriceChild.get()+'\t\t\t'+'\n')
txtTicketDetail.insert(END,'\t\t\t\t'+'====================================='+'\n')
txtTicketDetail.insert(END,'\t\t\t\t'+'Total Price: \t'+CostOfChild.get()+'\n')

txtTicketDetail.insert(END,'Senior:\t\t\t'+QtySenior.get()+'\t\t\t'+UnitPriceSenior.get()+'\t\t\t'+'\n')
txtTicketDetail.insert(END,'\t\t\t\t'+'====================================='+'\n')
txtTicketDetail.insert(END,'\t\t\t\t'+'Total Price: \t'+CostOfSenior.get()+'\n')


txtTicketDetail.insert(END,'Concession:\t\t\t'+QtyConcession.get()+'\t\t\t'+UnitPriceConcession.get()+'\t\t\t'+'\n')
txtTicketDetail.insert(END,'\t\t\t\t'+'====================================='+'\n')
txtTicketDetail.insert(END,'\t\t\t\t'+'Total Price: \t'+CostOfConcession.get()+'\n')

txtTicketDetail.insert(END,'\t\t'+'Sub Total($): \t\t\t'+SubTotal.get()+'\n')
txtTicketDetail.insert(END,'\t\t'+'Discount (in %): \t\t\t'+Discount.get()+'%'+'\n')
txtTicketDetail.insert(END,'\t\t'+'Tax: \t\t\t'+Tax.get()+'\n')
txtTicketDetail.insert(END,'\t\t'+'====================================='+'\n')
txtTicketDetail.insert(END,'\t\t'+'Total Payable Price ($):\t'+TotalCost.get()+'\n')


#-------------------------Define variables------------TextBoxes------------------
TicketNum=StringVar()
Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostOfAdult=StringVar() 
CostOfChild=StringVar()
CostOfSenior=StringVar()
CostOfConcession=StringVar()
CustomerName=StringVar()
CustomerMob=StringVar()
CustomerEmail=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
Discount=StringVar()
UnitPriceAdult=StringVar()
UnitPriceChild=StringVar()
UnitPriceSenior=StringVar()
UnitPriceConcession=StringVar()
QtyAdult=StringVar()
QtyChild=StringVar()
QtySenior=StringVar()
QtyConcession=StringVar()
CardNum=StringVar()
CardValidity=StringVar()
Discount=StringVar()

#-------------------Set default value of component-----------------
CostOfAdult.set(0)
CostOfChild.set(0)
CostOfSenior.set(0)
CostOfConcession.set(0)
UnitPriceAdult.set(0)               #deafult values in thr textboxes
UnitPriceChild.set(0)
UnitPriceSenior.set(0)
UnitPriceConcession.set(0)
QtyAdult.set(0)
QtyChild.set(0)
QtySenior.set(0)
QtyConcession.set(0)
Discount.set(0)

#----------------Set deafault value of Date and Time component--------------------
TimeOfOrder.set(time.strftime('%H:%M:%S'))
DateOfOrder.set(time.strftime('%d/%m/%y'))

#--------------------Frame Design------------------------------------------------
Tops=Frame(root,width=1350,height=50,bd=16,relief='raise')
Tops.pack(side=TOP)                    #used pack method

LF=Frame(root,width=700,height=650,bd=16,relief='raise')
LF.pack(side=LEFT)

RF=Frame(root,width=600,height=650,bd=16,relief='raise')
RF.pack(side=RIGHT)

Tops.configure(background='dark blue')
LF.configure(background='dark blue')
RF.configure(background='dark blue')

#--------------------------------------------------------------------------------
LeftInsideLF=Frame(LF,width=700,height=100,bd=8,relief='raise',bg='yellow')
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF,width=700,height=400,bd=8,relief='raise',bg='light blue')
LeftInsideLFLF.pack(side=LEFT)
#--------------------------------------------------------------------------------
RightInsideLF=Frame(RF,width=604,height=300,bd=8,relief='raise',bg='light blue')
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF,width=306,height=400,bd=8,relief='raise',bg='yellow')
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF,width=300,height=800,bd=8,relief='raise',bg='blue')
RightInsideRFRF.pack(side=RIGHT)

#-------------------------------------Define Title-------------------------------
lblInfo=Label(Tops,font=('Century Schoolbook',50,'bold'),text='            Country Trip Booking System          ',bg='dark blue',fg='orange',bd=10,anchor='w')
lblInfo.grid(row=0,column=1)

#-------------------------Top Left Frame--------------------------------------------
lblCustomerName=Label(LeftInsideLF,font=('arial',14,'bold'),text='Client Name',bg='yellow',fg='blue',bd=10,anchor='w')
lblCustomerName.grid(row=0,column=0)

txtCustomerName=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=10,width=43,bg='white',justify='left',textvariable=CustomerName)
txtCustomerName.grid(row=0,column=1)

lblCustomerMob=Label(LeftInsideLF,font=('arial',14,'bold'),text='Contact',bg='yellow',fg='blue',bd=10,anchor='w')
lblCustomerMob.grid(row=1,column=0)

txtCustomerMob=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=10,width=43,bg='white',justify='left',textvariable=CustomerMob)
txtCustomerMob.grid(row=1,column=1)

lblCustomerEmail=Label(LeftInsideLF,font=('arial',14,'bold'),text='Email',bg='yellow',fg='blue',bd=10,anchor='w')
lblCustomerEmail.grid(row=2,column=0)

txtCustomerEmail=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=10,width=43,bg='white',justify='left',textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2,column=1)

#----------------------------Top Right Frame---------------------------------------------
lblDateOfOrder=Label(RightInsideLF,font=('arial',12,'bold'),text='Date',bg='light blue',fg='blue',bd=10,anchor='w')
lblDateOfOrder.grid(row=0,column=0)

txtDateOfOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,bg='white',justify='left',textvariable=DateOfOrder)
txtDateOfOrder.grid(row=0,column=1)

lblTimeOfOrder=Label(RightInsideLF,font=('arial',12,'bold'),text='Time',bg='light blue',fg='blue',bd=10,anchor='w')
lblTimeOfOrder.grid(row=1,column=0)

txtTimeOfOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,bg='white',justify='left',textvariable=TimeOfOrder)
txtTimeOfOrder.grid(row=1,column=1)

lblTicketNumber=Label(RightInsideLF,font=('arial',12,'bold'),text='Ticket Reciept No.    ',bg='light blue',fg='blue',bd=10,anchor='w')
lblTickerNumber.grid(row=2,column=0)

txtTicketNumber=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,bg='white',justify='left',textvariable=TicketNum)
txtTicketNumber.grid(row=2,column=1)

#------------------------------------Bottom Right Frame-------------------------------------
lblSubTotal=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Sub Total($)',bg='yellow',fg='blue',bd=16,anchor='w')
lblSubTotal.grid(row=0,column=0)

txtSubTotal=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=0,column=1)

lblDiscount=Label(RightInsideLFLF,font=('arial',12,'bold'),text='-Discount(%)',bg='yellow',fg='blue',bd=16,anchor='w')
lblDiscount.grid(row=1,column=0)

txtDiscount=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=Dicount)
txtDiscount.grid(row=1,column=1)

lblTax=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Tax(5% value)',bg='yellow',fg='blue',bd=16,anchor='w')
lblTax.grid(row=2,column=0)

txtTax=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=Tax)
txtTax.grid(row=2,column=1)

lblTotalCost=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Total Cost($) ',bg='yellow',fg='blue',bd=16,anchor='w')
lblTotalCost.grid(row=3,column=0)

txtTotalCost=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=TotalCost)
txtTotalCost.grid(row=3,column=1)

lblMethodOfPayment=Label(RightInsideLFLFfont=('arial',12,'bold'),text='Mode Of Payment',bg='yellow',fg='blue',bd=16,anchor='w')
lblMethodOfPayment.grid(row=4,column=0)

cmdMethodOfPayment=ttk.Combobox(RightInsideLFLF,font=('arial',10,'bold'))
cmdMethodOfPayment['value']=('Other','Cash On Delivery','Credit Card','Visa Card','Master Card')
cmdMethodOfPayment.grid(row=4,column=1)
cmdMethodOfPayment.set('Other')

lblCardNum=Label(RightInsideLFLFfont=('arial',12,'bold'),text='Card Ref.(14 digit)',bg='yellow',fg='blue',bd=16,anchor='w')
lblCardNum.grid(row=5,column=0)

txtCardNum=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=CardNum)
txtCardNum.grid(row=5,column=1)

lblCardValidty=Label(RightInsideLFLFfont=('arial',12,'bold'),text='Card Validity (MM/YYYY)',bg='yellow',fg='blue',bd=16,anchor='w')
lblCardValidity.grid(row=6,column=0)

txtCardValidity=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=CardValidity)
txtCardValidity.grid(row=6,column=1)

#-------------------------------Bottom Left Frame------------------------------------
lblTicket=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Ticket',bg='light blue',fg='blue',bd=20)
lblTicket.grid(row=0,column=0)

lblQty=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Quantity',bg='light blue',fg='blue',bd=10)
lblQty.grid(row=0,column=1)

lblUnitPrice=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Unit Cost($)',bg='light blue',fg='blue',bd=20)
lblUnitPrice.grid(row=0,column=2)

lblCostOfTicket=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Total Cost($)',bg='light blue',fg='blue',bd=20)
lblCostOfTicket.grid(row=0,column=3)

#-------------------------------------------------------------------------
lblAdult=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Adult',bg='light blue',fg='blue',bd=20)
lblAdult.grid(row=1,column=0)

lblChild=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Child',bg='light blue',fg='blue',bd=10)
lblChild.grid(row=2,column=0)

lblSenior=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Senior',bg='light blue',fg='blue',bd=20)
lblSenior.grid(row=3,column=0)

lblConcession=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Concession',bg='light blue',fg='blue',bd=20)
lblConcession.grid(row=4,column=0)

#------------------------------------------------------------------------------
txtQtyAdult=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=QtyAdult)
txtQtyAdult.grid(row=1,column=1)

txtQtyChild=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=QtyChild)
txtQtyChild.grid(row=2,column=1)

txtQtySenior=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=QtySenior)
txtQtySenior.grid(row=3,column=1)

txtQtyConcession=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=QtyConcession)
txtQtyConcession.grid(row=4,column=1)

#-------------------------------------------------------------------------------
txtUnitPriceAdult=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=UnitPriceAdult)
txtUnitPriceAdult.grid(row=1,column=2)

txtUnitPriceChild=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=UnitPriceChild)
txtUnitPriceChild.grid(row=2,column=2)

txtUnitPriceSenior=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=UnitPriceSenior)
txtUnitPriceSenior.grid(row=3,column=2)

txtUnitPriceConcession=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=UnitPriceConcession)
txtUnitPriceConcession.grid(row=4,column=2)

#-------------------------------------------------------------------------------
txtCostOfAdult=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=CostOfAdult)
txtCostOfAdult.grid(row=1,column=3)

txtCostOfChild=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=CostOfChild)
txtCostOfChild.grid(row=2,column=3)

txtCostOfSenior=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=CostOfSenior)
txtCostOfSenior.grid(row=3,column=3)

txtCostOfConcession=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=CostOfConcession)
txtCostOfConcession.grid(row=4,column=3)

#----------------------------------Buttons Right Frame---------------------------------------
btnTotalCost=Button(RightInsideRFRF,pady=5,bd=5,fg='blue',font=('arial',16,'bold'),width=11,text='Total Cost',bg='light blue',command=CostOfOrder).grid(row=0,column=0)
btnReset=Button(RightInsideRFRF,pady=5,bd=5,fg='blue',font=('arial',16,'bold'),width=11,text='Reset',bg='light blue',command=Reset).grid(row=1,column=0)
btnTicketReceipt=Button(RightInsideRFRF,pady=5,bd=5,fg='blue',font=('arial',16,'bold'),width=11,text='Receipt',bg='light blue',command=TicketReceipt).grid(row=2,column=0)
btnExit=Button(RightInsideRFRF,pady=5,bd=5,fg='blue',font=('arial',16,'bold'),width=11,text='Exit',bg='light blue',command=Exit).grid(row=3,column=0)

root.mainloop()



















