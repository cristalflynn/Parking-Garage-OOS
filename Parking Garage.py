class parking(): #start
        def __init__(self, tickets, parkingSpaces):
            self.tickets = tickets
            self.parkingSpaces = parkingSpaces

        def garageSize(self): 
          while True:
                lotSize = int(input("pick your garage size range from: (1-200) ")) 
                if (lotSize > 0) and (lotSize < 201): 
                    for spots in range(1, lotSize+1): #going through spaces from start number 
                        self.tickets.append(spots)  #adds amount of spaces and tickets to pick from
                        self.parkingSpaces.append(spots)
                    break
                else:
                 print("Out of parking garage range")
                 continue

        def takeTicket(self, currentTicket):  
            self.currentTicket = currentTicket
            if self.currentTicket != []:  #the parking spot picked / ticket collected start from []
                 currentTicket.update({self.tickets[0]:""}) #add if paid/option from start
                 del self.tickets[0]  #once it's taken it -1
                 del self.parkingSpaces[0]
                 self.show(currentTicket) #show what's remaining 
            else:
                print("Sorry, there are no more spots available")
                
        def pay(self, currentTicket):
             self.show(currentTicket)
             key = int(input("What's your ticket number? ")) #asking payment options / follow up answer
             print(f"Your ticket number is  {key}")  #putting it in a dic key/ value 
             value = input("Payment options: 'cash' or 'card'? ")
             if value == 'card':
                currentTicket[key] = 'paid with card'
             elif value == 'cash':
                currentTicket[key] = 'paid with cash'
             else:
                    print("Invalid payment option")
        def show(self, currentTicket):
            print(f"\nAvailable tickets: {self.tickets} \n available parking spaces {self.parkingSpaces}")
            print(f"\ncurrent tickets: {currentTicket}\n") #looking at what's taken /paid 

        def leaving(self, currentTicket): 
            print(currentTicket)
            key = int(input("take your paid ticket ")) #picking a paid ticket from list / -1 from show list 
            if currentTicket[key] == "paid with card" or (currentTicket[key] == 'paid with cash'):
                    print("Thank you, you have 15 min to leave.")
                    self.tickets.append(key)
                    self.parkingSpaces.append(key)
                    currentTicket.pop(key)

            else:
                    print("Payment is required ")
                
def parkingGarage():
     tickets = []  #start with empty list and dic so you can add / remove per options
     parkingSpaces = []
     currentTicket = {}
     parking(tickets, parkingSpaces).garageSize() # taking in attributes per garage size method 
     while True:  #looping through options in parking with method 
        garageOptions = input("Menu:\npark,pay,show,leave,quit: ")
        if garageOptions == 'park':
            parking(tickets, parkingSpaces).takeTicket(currentTicket)
        elif garageOptions == 'pay':
            parking(tickets, parkingSpaces).pay(currentTicket)
        elif garageOptions == 'show':
            parking(tickets, parkingSpaces).show(currentTicket)
        elif garageOptions == 'leave':
            parking(tickets, parkingSpaces).leaving(currentTicket)
        else:
            garageOptions == 'quit'
            break

parkingGarage()
        
           

           