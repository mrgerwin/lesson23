from guizero import App, PushButton, Text, TextBox, ListBox, Box, Window

def DisplayCustomer():
    
    for cust in Customers:
        ID = cust[0]
        if ID == CustIDTextBox.value:
            CustNameText.value = cust[1]
            CustPhoneText.value = cust[2]
            return
    else:
        CustNameText.value = "Not Found"
        CustPhoneText.value = ""

def DisplayProduct():
    global CurrentIndex
    
    CurrentIndex = 0
    for prod in Products:
        ID = prod[0]
        if ID == ProductIDTextBox.value:
            ProdNameText.value = prod[1]
            ProdCostText.value = prod[2]
            return
        else:
            CurrentIndex += 1
    else:
        ProdNameText.value = "Not Found"
        ProdCostText.value = ""
        CurrentIndex = None

def Purchase():
    global Total
    if CurrentIndex != None:
        CartListBox.append([Products[CurrentIndex][1], Products[CurrentIndex][2]])
        Total += Products[CurrentIndex][2]
        TotalText.value= "Total: $" + str(Total)
    else:
        print("No Product Selected")
MainWindow = App("Cash Register", 800, 800)

CustomerBox = Box(MainWindow, layout="grid", border = 1)
ProductBox = Box(MainWindow, layout ="grid", border = 1)
CartBox = Box(MainWindow, layout = "grid",border = 1)

CustText = Text(CustomerBox, text = "Customer ID Number", grid=[0,0])
CustIDTextBox = TextBox(CustomerBox, grid=[0,1])

EnterCustButton = PushButton(CustomerBox, text="Enter", command = DisplayCustomer, grid=[1,1])
AddCustButton = PushButton(CustomerBox, text="Add/Edit Customer", grid=[2,1])
CustNameText = Text(CustomerBox, text = "Name:", grid=[0,2])
CustPhoneText = Text(CustomerBox, text = "Phone:", grid=[1,2])

EnterProductButton = PushButton(ProductBox, text="Enter", command =DisplayProduct, grid=[1,1])
ProductText = Text(ProductBox, text = "Product ID Number", grid=[0,0])
ProductIDTextBox = TextBox(ProductBox, grid=[0,1])
AddProductButton = PushButton(ProductBox, text="Add/Edit Product", grid=[2,1])
ProdNameText = Text(ProductBox, text="Name:", grid=[0, 2])
ProdCostText = Text(ProductBox, text = "$", grid=[1,2])

PurchaseButton = PushButton(CartBox, text = "Purchase", command=Purchase, grid=[0,0])
CartListBox = ListBox(CartBox, grid=[0,1])
TotalText = Text(CartBox, text = "Total: $0.00", grid=[0,2])
CheckOutButton = PushButton(CartBox, text = "Check Out", grid = [0,3])

#Data Structures

#Customers
Customers = [["9230", "John Doe", 4192229999], ["0001","First Customer", 8886667777], ["0002", "Second Customer", 7659287162]]
#Products
Products = [["10232", "Pens Pack of 10", 2.99, 43], ["11111", "Folders", 3.99, 34], ["00001", "Pencils", .99, 24], ["92932", "Stationary", 4.99, 53]]

CurrentIndex = None
Total = 0

