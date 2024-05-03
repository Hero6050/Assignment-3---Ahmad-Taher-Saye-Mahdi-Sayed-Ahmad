import pickle
import tkinter as tk

# Here we create a class tp represent people
# This will save us a lot of time when creating other classes
class Person:
    # Construct the person
    def __init__(self, name, age, dateOfBirth):
        self.__name = name
        self.__age = age
        self.__dateOfBirth = dateOfBirth

    # Some setter/getter functions
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age
    def setDateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth
    def getDateOfBirth(self):
        return self.__dateOfBirth


    # Polymorphic function to help display details
    def displayDetails(self):
        print(f"Name: {self.getName()}")
        print(f"Age: {self.getAge()}")
        print(f"Date Of Birth: {self.getDateOfBirth()}")



# Here we create a class to represent employees
# This class will be used as a foundation to other employee classes
# Such as managers. This will be done via inheritance
class Employee(Person):
    # Here we construct an employee
    def __init__(self, name, empID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails, managerID):
        # Super function to call the constructor of the parent class
        super().__init__(name=name, age=age,dateOfBirth=dateOfBirth)
        self.__empID = empID
        self.__department = department
        self.__jobTitle = jobTitle
        self.__managerID = managerID
        self.__passportDetails = passportDetails
        # This is here to ensure no error occurs while using our GUI
        try:
            # Someone's salary can't be a negative number
            # 0 might mean they are volunteers
            if float(basicSalary) >= 0:
                self.__basicSalary = float(basicSalary)
            else:
                self.__basicSalary = 0
        except:
                self.__basicSalary = 0

    # Setter/Getter functions
    def setID(self, ID):
        self.__empID = ID
    def getID(self):
        return self.__empID
    def setDepartment(self, department):
        self.__department = department
    def getDepartment(self):
        return self.__department
    def setJobTitle(self, jobTitle):
        self.__jobTitle = jobTitle
    def getJobTitle(self):
        return self.__jobTitle
    def setBasicSalary(self, salary):
        try:
            # A salary can't be a negative number
            if float(salary) >= 0:
                self.__basicSalary = float(salary)
                return True
            else:
                print("Invalid salary")
                return False
        except:
            self.__basicSalary = 0
    def getBasicSalary(self):
        return self.__basicSalary
    def setManagerID(self, managerID):
        self.__managerID = managerID
    def getManagerID(self):
        return self.__managerID
    def setPassportDetails(self, passportDetails):
        self.__passportDetails = passportDetails
    def getPassportDetails(self):
        return self.__passportDetails


    # Polymorphic function to help display details
    def displayDetails(self):
        # Super function to call parent class's same polymorphic function
        super().displayDetails()
        print(f"Employee ID: {self.getID()}")
        print(f"Department: {self.getDepartment()}")
        print(f"Job Title: {self.getJobTitle()}")
        print(f"Basic Salary: {self.getBasicSalary()}")
        print(f"Manager ID: {self.getManagerID()}")
        print(f"Passport Details: {self.getPassportDetails()}")



# This class will represent a manager
# Managers are still employees but have extra methods
# Hence the inheritance
class Manager(Employee):
    # We construct the object here
    def __init__(self, name, empID, department, basicSalary, age, dateOfBirth, passportDetails, managerID):
        # We used super function to call the parent class's constructor
        # A manager will always have the same job title
        super().__init__(name = name, empID = empID, department=department, jobTitle="Manager", basicSalary=basicSalary,
                         age = age, dateOfBirth=dateOfBirth, passportDetails=passportDetails, managerID=managerID)

        # Here is employees this manager manages
        self.__employees = []

    # Here we add, remove, and get employee information
    def addEmployee(self, employee):
        # Make sure employee is not already being managed by this manager
        if employee not in self.__employees:
            # Update the employee's information
            # Then add the employee to this manager's list
            employee.setManagerID(self.getID())
            self.__employees.append(employee)
            return True
        return False
    def removeEmployee(self, employee):
        # Make sure this employee is managed by this manager
        if employee in self.__employees:
            # Update employee's information
            # Then remove the employee from this manager's list
            employee.setManagerID(None)
            self.__employees.remove(employee)
        return True
    def getEmployees(self):
        return self.__employees


    # Here are some functions for managers to manage their employee information
    def setEmployeeSalary(self, employee, salary):
        # We need to check if the manager has access or not first
        if employee in self.__employees:
            employee.setBasicSalary(salary)
        return False
    def setEmployeeID(self, employee, ID):
        # We need to check if the manager has access or not first
        if employee in self.__employees:
            employee.setEmpID(ID)
            return True
        return False
    def setEmployeeDepartment(self, employee, department):
        # We need to check if the manager has access or not first
        if employee in self.__employees:
            employee.setDepartment(department)
            return True
        return False
    def setEmployeeJobTitle(self, employee, jobTitle):
        # We need to check if the manager has access or not first
        if employee in self.__employees:
            employee.setJobTitle(jobTitle)
            return True
        return False
    def setEmployeeManagerID(self, employee, managerID):
        # We need to check if the manager has access or not first
        if employee in self.__employees:
            employee.setManagerID(managerID)
            return True
        return False


    # Polymorphic function to help display details
    def displayDetails(self):
        # Super function to call parent class's same polymorphic function
        super().displayDetails()
        print(f"Employees Managed:")
        empList = self.__employees
        for employee in range(len(empList)):
            print(f"{employee + 1}. Employee ID: {empList[employee].getID()}")



# This will represent a event member
# This helps simplify the code using inheritance
class EventMember(Person):
    # Construct an event member
    def __init__(self, name, age, dateOfBirth, address, contactDetails):
        # Super function to call the constructor of the parent class
        super().__init__(name=name, age=age, dateOfBirth=dateOfBirth)
        self.__address = address
        self.__contactDetails = contactDetails

    # Setter/Getter functions
    def setAddress(self, address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def setContactDetails(self, contactDetails):
        self.__contactDetails = contactDetails
    def getContactDetails(self):
        return self.__contactDetails


    # Polymorphic function to help display details
    def displayDetails(self):
    # Super function to call parent class's same polymorphic function
        super().displayDetails()
        print(f"Address: {self.getAddress()}")
        print(f"Contact Details: {self.getContactDetails()}")



# This class represents a client.
# A client is also a person
class Client(EventMember):
    def __init__(self, clientID, name, age, dateOfBirth, address, contactDetails, budget):
        super().__init__(name=name, age=age, dateOfBirth=dateOfBirth, address=address, contactDetails=contactDetails)
        self.__clientID = clientID

        # This is here to make sure no error appear while using our GUI
        try:
            if float(budget) >= 0:
                # Budget can't be a negative number
                self.__budget = float(budget)
            else:
                self.__budget = 0
        except:
            self.__budget = 0

        # A client could organize multiple events
        # We will use a list to store all of them
        self.__events = []

    # Setter/Getter functions
    def setID(self, ID):
        self.__clientID = ID
    def getID(self):
        return self.__clientID
    def setBudget(self, budget):
        try:
            if float(budget) >= 0:
                # Budget can't be a negative number
                self.__budget = float(budget)
            else:
                self.__budget = 0
        except:
            self.__budget = 0
    def getBudget(self):
        return self.__budget

    # Functions for a client to create/organize an event
    def createEvent(self, eventID, eventType, theme, date, time, duration, venue, guestList,
                    cateringComp, cleaningComp, decorationComp, entertainmentComp, furnitureComp, invoice):

        # We create the event then add it to the list of events
        event = Event(eventID, eventType, theme, date, time, duration, venue.getAddress(), self.getID(), guestList,
                     cateringComp.getName(), cleaningComp.getName(), decorationComp.getName(), entertainmentComp.getName(),
                      furnitureComp.getName(), invoice)

        self.__events.append(event)
        return event

    def addEvent(self, event):
        if event not in self.__events:
            self.__events.append(event)
            # We update the event's ID
            event.setClientID(self.getID())
            return True
        return False
    def removeEvent(self, event):
        if event in self.__events:
            self.__events.remove(event)
            # We update the event's ID
            event.setClientID(None)
        return True
    def getEvents(self):
        return self.__events


    # Polymorphic function to help display details
    def displayDetails(self):
    # Super function to call parent class's same polymorphic function
        super().displayDetails()
        print(f"Client ID: {self.getID()}")
        print(f"Budget: {self.getBudget()}")
        eventList = self.getEvents()
        print (f"Organized Events: ")
        for event in range(len(eventList)):
            print(f"{event + 1}. Event ID: {eventList[event].getID()}")



# This class represents a client
# A guest is a party member hence the inheritance
class Guest(EventMember):
    # Construct a quest
    def __init__(self, guestID, name, age, dateOfBirth, address, contactDetails):
        super().__init__(name=name, age=age, dateOfBirth=dateOfBirth, address=address, contactDetails=contactDetails)
        self.__guestID = guestID
        # This list will be a list for due events
        self.__dueEvents = []

    # Setter/Getter functions
    def setID(self, ID):
        self.__guestID = ID
    def getID(self):
        return self.__guestID

    # To add, remove, and get due event list
    def addEvent(self, event):
        if event not in self.__dueEvents:
            self.__dueEvents.append(event)
            return True
        return False
    def removeEvent(self, event):
        if event in self.__dueEvents:
            self.__dueEvents.remove(event)
        return True
    def getEvents(self):
        return self.__dueEvents


    def displayDetails(self):
    # Super function to call parent class's same polymorphic function
        super().displayDetails()
        print(f"Guest ID: {self.getID()}")
        eventList = self.getEvents()
        print(f"Due events: ")
        for event in range(len(eventList)):
            print(f"{event + 1}. Event ID: {eventList[event].getID()}")



# This class will represent an event
class Event:
    # Construct an event
    def __init__(self, eventID, eventType, theme, date, time, duration, venueAddress, clientID, guestList,
                     cateringComp, cleaningComp, decorationComp, entertainmentComp, furnitureComp, invoice):

        self.__eventID = eventID
        self.__type = eventType
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venueAddress = venueAddress
        self.__clientID = clientID
        self.__guestList = guestList
        # This sends invites to the guests
        for guest in guestList:
            guest.addEvent(self)
        self.__cateringComp = cateringComp
        self.__cleaningComp = cleaningComp
        self.__decorationComp = decorationComp
        self.__entertainmentComp = entertainmentComp
        self.__furnitureComp = furnitureComp
        self.__invoice = invoice

    # Setter/Getter functions
    def setID(self, ID):
        self.__eventID = ID
    def getID(self):
        return self.__eventID
    def setType(self, type):
        self.__type = type
    def getType(self):
        return self.__type
    def setTheme(self, theme):
        self.__theme = theme
    def getTheme(self):
        return self.__theme
    def setDate(self, date):
        self.__date = date
    def getDate(self):
        return self.__date
    def setTime(self, time):
        self.__time = time
    def getTime(self):
        return self.__time
    def setDuration(self, duration):
        self.__duration = duration
    def getDuration(self):
        return self.__duration
    def setVenueAddress(self, venueAddress):
        self.__venueAddress = venueAddress
    def getVenueAddress(self):
        return self.__venueAddress
    def setClientID(self, clientID):
        self.__clientID = clientID
    def getClientID(self):
        return self.__clientID
    def setCatering(self, cateringComp):
        self.__cateringComp = cateringComp
    def getCatering(self):
        return self.__cateringComp
    def setCleaning(self, cleaningComp):
        self.__cateringComp = cleaningComp
    def getCleaning(self):
        return self.__cleaningComp
    def setDecoration(self, decorationComp):
        self.__decorationComp = decorationComp
    def getDecoration(self):
        return self.__decorationComp
    def setEntertainment(self, entertainmentComp):
        self.__entertainmentComp = entertainmentComp
    def getEntertainment(self):
        return self.__entertainmentComp
    def setFurniture(self, furnitureComp):
        self.__furnitureComp = furnitureComp
    def getFurniture(self):
        return self.__furnitureComp
    def setInvoice(self, invoice):
        self.__invoice = invoice
    def getInvoice(self):
        return self.__invoice

    # To add, remove, get guest list
    def addGuest(self, guest):
        if guest not in self.__guestList:
            guest.addEvent(self)
            self.__guestList.append(guest)
            return True
        return False
    def removeGuest(self, guest):
        if guest in self.__guestList:
            guest.removeEvent(self)
            self.__guestList.remove(guest)
        return True
    def getGuests(self):
        return self.__guestList


    # Polymorphic function to help display details
    def displayDetails(self):
        print(f"Event ID: {self.getID()}")
        print(f"Event Type: {self.getType()}")
        print(f"Theme: {self.getTheme()}")
        print(f"Date: {self.getDate()}")
        print(f"Time: {self.getTime()}")
        print(f"Duration: {self.getDuration()}")
        print(f"Venue Address: {self.getVenueAddress()}")
        print(f"Client ID: {self.getClientID()}")
        guestList = self.getGuests()
        print(f"Guests: ")
        for guest in range(len(guestList)):
            print(f"{guest + 1}. Guest ID: {guestList[guest].getID()}")
        print(f"Catering Company: {self.getCatering()}")
        print(f"Cleaning Company: {self.getCleaning()}")
        print(f"Decoration Company: {self.getDecoration()}")
        print(f"Furniture Company: {self.getFurniture()}")
        print(f"Invoice: {self.getInvoice()}")



# This class will represent Venue
class Venue:
    # Construct a venue
    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        self.__venueID = venueID
        self.__name = name
        self.__address = address
        self.__contact = contact
        self.__minGuests = minGuests
        self.__maxGuests = maxGuests

    # Setter/Getter functions
    def setID(self, ID):
        self.__venueID = ID
    def getID(self):
        return self.__venueID
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAddress(self, address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def setContact(self, contact):
        self.__contact = contact
    def getContact(self):
        return self.__contact
    def setMaxGuests(self, maxGuests):
        self.__maxGuests = maxGuests
    def getMaxGuests(self):
        return self.__maxGuests
    def setMinGuests(self, minGuests):
        self.__minGuests = minGuests
    def getMinGuests(self):
        return self.__minGuests


    # To display venue information
    def displayDetails(self):
        print(f"Venue ID: {self.getID()}")
        print(f"Venue Name: {self.getName()}")
        print(f"Address: {self.getAddress()}")
        print(f"Contact: {self.getContact()}")
        print(f"Minimum Number of Guests: {self.getMinGuests()}")
        print(f"Maximum Number of Guests: {self.getMaxGuests()}")



# This class will represent suppliers
class Supplier:
    # Construct a supplier
    def __init__(self, catererID, name, address, contactDetails, menu, minGuests, maxGuests):
        self.__catererID = catererID
        self.__name = name
        self.__address = address
        self.__contactDetails = contactDetails
        self.__menu = menu
        self.__minGuests = minGuests
        self.__maxGuests = maxGuests

    # Setter/Getter Functions
    def setID(self, ID):
        self.__catererID = ID
    def getID(self):
        return self.__catererID
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAddress(self, address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def setContactDetails(self, contact):
        self.__contactDetails = contact
    def getContactDetails(self):
        return self.__contactDetails
    def setMenu(self, menu):
        self.__menu = menu
    def getMenu(self):
        return self.__menu
    def setMaxGuests(self, maxGuests):
        self.__maxGuests = maxGuests
    def getMaxGuests(self):
        return self.__maxGuests
    def setMinGuests(self, minGuests):
        self.__minGuests = minGuests
    def getMinGuests(self):
        return self.__minGuests


    # To display venue information
    def displayDetails(self):
        print(f"Caterer ID: {self.getID()}")
        print(f"Supplier Name: {self.getName()}")
        print(f"Address: {self.getAddress()}")
        print(f"Contact Details: {self.getContactDetails()}")
        print(f"Minimum Number of Guests: {self.getMinGuests()}")
        print(f"Maximum Number of Guests: {self.getMaxGuests()}")


# This class will represent our system.
# Our system will store the information in binary files
# And will be able to manage/alter them
class System:
    # Here we construct the system with a list of classes we want to store into a binary file
    def __init__(self, emp, eventsInfo, clientsInfo, suppliersInfo, guestsInfo, venuesInfo):
        self._update_file('EmployeesFile.pkl', emp)
        self._update_file('EventsFile.pkl', eventsInfo)
        self._update_file('ClientsFile.pkl', clientsInfo)
        self._update_file('SuppliersFile.pkl', suppliersInfo)
        self._update_file('GuestsFile.pkl', guestsInfo)
        self._update_file('VenueFile.pkl', venuesInfo)

    # Here we first create and check if it exists then dump everything in
    def _update_file(self, filename, data):
        try:
            with open(filename, 'rb') as file:
                existing_data = pickle.load(file)
        except (EOFError, FileNotFoundError):
            existing_data = {}

        with open(filename, 'wb') as file:
            for item in data:
                existing_data[item.getID()] = item
            pickle.dump(existing_data, file)

    # Here are functions to find, create, modify, and delete objects in the binary file
    def findEmployee(self, empID):
        # We load the file and search for the employee
        # When we find them we display their info
        with open('EmployeesFile.pkl', 'rb') as empFile:
            employees = pickle.load(empFile)
            for employee in employees:
                if employee == empID:
                    employees[employee].displayDetails()
                    return True
            return False

    def findEvent(self, eventID):
        with open('EventsFile.pkl', 'rb') as eventFile:
            events = pickle.load(eventFile)
            for event in events:
                if event == eventID:
                    events[eventID].displayDetails()
                    return True
            return False

    def findClient(self, clientID):
        with open('ClientsFile.pkl', 'rb') as clientFile:
            clients = pickle.load(clientFile)
            for client in clients:
                if client == clientID:
                    clients[client].displayDetails()
                    return True
            return False

    def findSupplier(self, supplierID):
        with open('SuppliersFile.pkl', 'rb') as supplierFile:
            suppliers = pickle.load(supplierFile)
            for supplier in suppliers:
                if supplier == supplierID:
                    suppliers[supplier].displayDetails()
                    return True
            return False

    def findGuest(self, guestID):
        with open('GuestsFile.pkl', 'rb') as guestFile:
            guests = pickle.load(guestFile)
            for guest in guests:
                if guest == guestID:
                    guests[guest].displayDetails()
                    return True
            return False

    def findVenue(self, venueID):
        with open('VenueFile.pkl', 'rb') as venueFile:
            venues = pickle.load(venueFile)
            for venue in venues:
                if venue == venueID:
                    venues[venue].displayDetails()
                    return True
            return False

    # This will create an object
    # If the object exists it will be modified instead.
    # You can't have two objects with the same ID, the old one will be modified
    def createEmployee(self, empID, name, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails, managerID):
        # Here we check if the employee exists, if they do, we keep unmodified info
        oldEmployee = self.deleteEmployee(empID)

        # We create a new object if an old employee does not exist
        if oldEmployee == False:
            newEmployee = Employee(name, empID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails, managerID)
        else:
            # If the employee exists we modify the changed information
            # An input that was empty means we don't modify it in the GUI
            if name != "":
                oldEmployee.setName(name)
            if department != "":
                oldEmployee.setDepartment(department)
            if jobTitle != "":
                oldEmployee.setJobTitle(jobTitle)
            if basicSalary != "":
                oldEmployee.setBasicSalary(basicSalary)
            if age != "":
                oldEmployee.setAge(age)
            if dateOfBirth != "":
                oldEmployee.setDateOfBirth(dateOfBirth)
            if passportDetails != "":
                oldEmployee.setPassportDetails(passportDetails)
            if managerID != "":
                oldEmployee.setManagerID(managerID)

            # Now we update the old employee to new employee
            newEmployee = oldEmployee

        # We dump the new employee into the binary file with the other employees
        # We need to read first, then dump
        with open('EmployeesFile.pkl', 'rb') as empFile:
            employees = pickle.load(empFile)
            employees[empID] = newEmployee

        with open('EmployeesFile.pkl', 'wb') as empFile:
            pickle.dump(employees, empFile)

    def createEvent(self, eventID, eventType, theme, date, time, duration, venueAddress, clientID, guestList,
                     cateringComp, cleaningComp, decorationComp, entertainmentComp, furnitureComp, invoice):

        oldEvent = self.deleteEvent(eventID)

        if oldEvent == False:
            newEvent = Event(eventID, eventType, theme, date, time, duration, venueAddress, clientID, guestList,
                          cateringComp, cleaningComp, decorationComp, entertainmentComp, furnitureComp, invoice)
        else:
            if eventType != "":
                oldEvent.setType(eventType)
            if theme != "":
                oldEvent.setTheme(theme)
            if date != "":
                oldEvent.setDate(date)
            if time != "":
                oldEvent.setTime(time)
            if duration != "":
                oldEvent.setDuration(duration)
            if venueAddress != "":
                oldEvent.setVenueAddress(venueAddress)
            if clientID != "":
                oldEvent.setClientID(clientID)
            if cateringComp != "":
                oldEvent.setCatering(cateringComp)
            if cleaningComp != "":
                oldEvent.setCleaning(cateringComp)
            if decorationComp != "":
                oldEvent.setDecoration(decorationComp)
            if entertainmentComp != "":
                oldEvent.setEntertainment(entertainmentComp)
            if furnitureComp != "":
                oldEvent.setFurniture(furnitureComp)
            if invoice != "":
                oldEvent.setInvoice(invoice)

            newEvent = oldEvent

        with open('EventsFile.pkl', 'rb') as eventFile:
            events = pickle.load(eventFile)
            events[eventID] = newEvent
        with open('EventsFile.pkl', 'wb') as eventFile:
            pickle.dump(events, eventFile)

    def createClient(self, clientID, name, age, dateOfBirth, address, contactDetails, budget):
        oldClient = self.deleteClient(clientID)

        if oldClient == False:
            newClient = Client(clientID, name, age, dateOfBirth, address, contactDetails, budget)
        else:
            if name != "":
                oldClient.setName(name)
            if age != "":
                oldClient.setAge(age)
            if dateOfBirth != "":
                oldClient.setDateOfBirth(dateOfBirth)
            if address != "":
                oldClient.setAddress(address)
            if contactDetails != "":
                oldClient.setContactDetails(contactDetails)
            if budget != "":
                oldClient.setBudget(budget)

            newClient = oldClient

        with open('ClientsFile.pkl', 'rb') as clientFile:
            clients = pickle.load(clientFile)
            clients[clientID] = newClient
        with open('ClientsFile.pkl', 'wb') as clientFile:
            pickle.dump(clients, clientFile)

    def createSupplier(self, catererID, name, address, contactDetails, menu, minGuests, maxGuests):
        oldSupplier = self.deleteSupplier(catererID)

        if oldSupplier == False:
            newSupplier = Supplier(catererID, name, address, contactDetails, menu, minGuests, maxGuests)
        else:
            if name != "":
                oldSupplier.setName(name)
            if address != "":
                oldSupplier.setAddress(address)
            if contactDetails != "":
                oldSupplier.setContactDetails(contactDetails)
            if menu != "":
                oldSupplier.setMenu(menu)
            if minGuests != "":
                oldSupplier.setMinGuests(minGuests)
            if maxGuests != "":
                oldSupplier.setMaxGuests(maxGuests)

            newSupplier = oldSupplier

        with open('SuppliersFile.pkl', 'rb') as supplierFile:
            suppliers = pickle.load(supplierFile)
            suppliers[catererID] = newSupplier
        with open('SuppliersFile.pkl', 'wb') as supplierFile:
            pickle.dump(suppliers, supplierFile)

    def createGuest(self, guestID, name, age, dateOfBirth, address, contactDetails):
        oldGuest = self.deleteGuest(guestID)

        if oldGuest == False:
            newGuest = Guest(guestID, name, age, dateOfBirth, address, contactDetails)
        else:
            if name != "":
                oldGuest.setName(name)
            if age != "":
                oldGuest.setAge(age)
            if dateOfBirth != "":
                oldGuest.setDateOfBirth(dateOfBirth)
            if address != "":
                oldGuest.setAddress(address)
            if contactDetails != "":
                oldGuest.setContactDetails(contactDetails)

            newGuest = oldGuest

        with open('GuestsFile.pkl', 'rb') as guestFile:
            guests = pickle.load(guestFile)
            guests[guestID] = newGuest
        with open('GuestsFile.pkl', 'wb') as guestFile:
            pickle.dump(guests, guestFile)

    def createVenue(self, venueID, name, address, contact, minGuests, maxGuests):
        oldVenue = self.deleteVenue(venueID)

        if oldVenue == False:
            newVenue = Venue(venueID, name, address, contact, minGuests, maxGuests)
        else:
            if name != "":
                oldVenue.setName(name)
            if address != "":
                oldVenue.setAddress(address)
            if contact != "":
                oldVenue.setContact(contact)
            if minGuests != "":
                oldVenue.setMinGuests(minGuests)
            if maxGuests != "":
                oldVenue.setMaxGuests(maxGuests)

            newVenue = oldVenue

        with open('VenueFile.pkl', 'rb') as venueFile:
            venues = pickle.load(venueFile)
            venues[venueID] = newVenue
        with open('VenueFile.pkl', 'wb') as venueFile:
            pickle.dump(venues, venueFile)

    # Functions to remove objects
    def deleteEmployee(self, empID):
        # If the employee exists, we will delete it
        # Otherwise we don't need to remove it
        if self.findEmployee(empID) == True:
            # We popped the object and returned it for when we want to modify
            # The existent object
            with open('EmployeesFile.pkl', 'rb') as empFile:
                employees = pickle.load(empFile)
                employee = employees.pop(empID)
            with open('EmployeesFile.pkl', 'wb') as empFile:
                pickle.dump(employees, empFile)
            return employee
        # This will let us know that the employee does not exist
        return False

    # We do the same for the other classes
    def deleteEvent(self, eventID):
        if self.findEvent(eventID) == True:
            with open('EventsFile.pkl', 'rb') as eventFile:
                events = pickle.load(eventFile)
                event = events.pop(eventID)
            with open('EventsFile.pkl', 'wb') as eventFile:
                pickle.dump(events, eventFile)
            return event
        return False

    def deleteClient(self, clientID):
        if self.findClient(clientID) == True:
            with open('ClientsFile.pkl', 'rb') as clientFile:
                clients = pickle.load(clientFile)
                client = clients.pop(clientID)
            with open('ClientsFile.pkl', 'wb') as clientFile:
                pickle.dump(clients, clientFile)
            return client
        return False

    def deleteSupplier(self, supplierID):
        if self.findSupplier(supplierID):
            with open('SuppliersFile.pkl', 'rb') as supplierFile:
                suppliers = pickle.load(supplierFile)
                supplier = suppliers.pop(supplierID)
            with open('SuppliersFile.pkl', 'wb') as supplierFile:
                pickle.dump(suppliers, supplierFile)
            return supplier
        return False

    def deleteGuest(self, guestID):
        if self.findGuest(guestID) == True:
            with open('GuestsFile.pkl', 'rb') as guestFile:
                guests = pickle.load(guestFile)
                guest = guests.pop(guestID)
            with open('GuestsFile.pkl', 'wb') as guestFile:
                pickle.dump(guests, guestFile)
            return guest
        return False

    def deleteVenue(self, venueID):
        if self.findVenue(venueID) == True:
            with open('VenueFile.pkl', 'rb') as venueFile:
                venues = pickle.load(venueFile)
                venue = venues.pop(venueID)
            with open('VenueFile.pkl', 'wb') as venueFile:
                pickle.dump(venues, venueFile)
            return venue
        return False

    # Functions to return the dictionary of objects
    def getEmployees(self):
        # We open the file in read mode then return the dictionary
        with open('EmployeesFile.pkl', 'rb') as empFile:
            return pickle.load(empFile)
    def getEvents(self):
        with open('EventsFile.pkl', 'rb') as eventFile:
            return pickle.load(eventFile)
    def getClients(self):
        with open('ClientsFile.pkl', 'rb') as clientFile:
            return pickle.load(clientFile)
    def getSuppliers(self):
        with open('SuppliersFile.pkl', 'rb') as supplierFile:
            return pickle.load(supplierFile)
    def getGuests(self):
        with open('GuestsFile.pkl', 'rb') as guestFile:
            return pickle.load(guestFile)
    def getVenues(self):
        with open('VenueFile.pkl', 'rb') as venueFile:
            return pickle.load(venueFile)



# This class will represent our GUI
class GUI(tk.Tk):
    def __init__(self):
        # Initialize the system
        self.mySystem = System([], [], [], [], [], [])

        super().__init__()
        self.title("System GUI")

        # Store the values from each grid
        self.grid_values = {}

        # Top Frame - Find
        # Here we create the top frame
        # Make sure to pack it
        self.find_frame = tk.Frame(self)
        self.find_frame.pack(side="top", fill="x")

        # Here we label this frame so that the user knows this is where you find an object
        # We pack this into teh GUI
        find_label = tk.Label(self.find_frame, text="Find", font=("Arial", 12))
        find_label.pack(side="top")

        # Here we provide a list of options as a form of a menu
        # The user will be able to select what they are looking for
        # After that, we use this to search for that item with a specific ID
        # Make sure to pack this
        self.find_options = ["Employee", "Event", "Client", "Supplier", "Guest", "Venue"]
        self.find_option_var = tk.StringVar(value=self.find_options[0])
        self.find_option_menu = tk.OptionMenu(self.find_frame, self.find_option_var, *self.find_options)
        self.find_option_menu.pack(side="top", padx=10, pady=5, fill="x")

        # This label will ensure that the users knows to enter the ID for object they are looking for
        # Make sure to pack them and everything that follows.
        self.find_id_label = tk.Label(self.find_frame, text="ID:")
        self.find_id_label.pack(side="left", padx=10, pady=5)

        # Here we create the entry we will use
        # This entry will be used to enter an ID, which then will be used to search for a specific object
        self.find_id_entry = tk.Entry(self.find_frame)
        self.find_id_entry.pack(side="left", padx=5, pady=5, fill="x")

        # Here we create the get button, pack it, and link it to a function
        self.find_button = tk.Button(self.find_frame, text="Get", command=self.get_info)
        self.find_button.pack(side="left", padx=10, pady=5)

        # Here we create the "Get All" button, pack it, and link it to its function
        self.get_all_button = tk.Button(self.find_frame, text="Get All", command=self.get_all_info)
        self.get_all_button.pack(side="left", padx=10, pady=5)

        # Here we create the delete button, pack it, and link it to a function
        self.delete_button = tk.Button(self.find_frame, text="Delete", command=self.delete_info)
        self.delete_button.pack(side="left", padx=10, pady=5)

        # Frame 1 - Create/Modify
        # We create and pack the final frame
        self.create_frame1 = tk.Frame(self)
        self.create_frame1.pack(side="left", fill="both", expand=True)

        # We create a label for this section and pack it
        create_label = tk.Label(self.create_frame1, text="Create / Modify", font=("Arial", 12))
        create_label.pack(side="top")

        # Here we create widgets for each class
        # It will help us create/modify each class
        self.create_widgets(self.create_frame1, 0, 2)

        # Frame 2 - Create/Modify
        # We pack the frame into the GUI
        self.create_frame2 = tk.Frame(self)
        self.create_frame2.pack(side="left", fill="both", expand=True)

        # We create a label for this section and pack it
        create_label = tk.Label(self.create_frame2, text="Create / Modify", font=("Arial", 12))
        create_label.pack(side="top")

        # Here we create widgets for each class
        # It will help us create/modify each class
        self.create_widgets(self.create_frame2, 2, 4)

        # Frame 3 - Create/Modify
        # We pack the frame
        self.create_frame3 = tk.Frame(self)
        self.create_frame3.pack(side="left", fill="both", expand=True)

        # We create a label for this section and pack it
        create_label = tk.Label(self.create_frame3, text="Create / Modify", font=("Arial", 12))
        create_label.pack(side="top")

        # Here we create widgets for each class
        # It will help us create/modify each class
        self.create_widgets(self.create_frame3, 4, 6)

        # Add Submit button outside of frames
        submit_button = tk.Button(self, text="Submit", command=self.submit_info)
        submit_button.pack(side="bottom", padx=10, pady=5)
        self.mainloop()

    def create_widgets(self, frame, start, end):
        # Here we create widgets for each square in the grids
        labels = ["Employee", "Client", "Guest", "Venue", "Event", "Supplier"]
        entries = [
            ["ID", "Name", "Department", "Job Title", "Basic Salary", "Age", "Date of Birth", "Passport Details", "Manager ID"],
            ["ID", "Name", "Age", "Date of Birth", "Address", "Contact Details", "Budget"],
            ["ID", "Name", "Age", "Date of Birth", "Address", "Contact Details"],
            ["ID", "Name", "Address", "Contact", "Minimum Guests", "Maximum Guests"],
            ["ID", "Type", "Theme", "Date", "Time", "Duration", "Venue Address", "Client ID",
             "Catering Company", "Cleaning Company", "Decorations Company", "Entertainment Company",
             "Furniture Company", "Invoice"],
            ["ID", "Name", "Address", "Contact Details", "Menu", "Minimum Guests", "Maximum Guests"]
        ]

        # Here we iteratively create the widgets and the entries
        # We used the lists to automate the process
        # We make sure to pack the values into the frame
        for i in range(start, end):
            frame = tk.Frame(frame)
            frame.pack(side="top", padx=5, pady=5, fill="both", expand=True)
            label = tk.Label(frame, text=labels[i], font=("Arial", 10, "bold"))
            label.pack(side="top", padx=5, pady=5)
            entry_values = []
            for entry_label in entries[i]:
                entry_frame = tk.Frame(frame)
                entry_frame.pack(side="top", padx=5, pady=2)
                entry_label = tk.Label(entry_frame, text=entry_label)
                entry_label.pack(side="left", padx=5)
                entry = tk.Entry(entry_frame)
                entry.pack(side="right", padx=5, fill="x", expand=True)
                entry_values.append(entry)
            # Store entry values with their label
            self.grid_values[labels[i]] = entry_values

    def get_info(self):
        # When we use the get button this function will run.
        # We look at the selected options
        # Then look for a specific ID in that option
        # For example, if you select "Employee", we will look for an employee with that ID
        # Then we display that employee's information
        find_option = self.find_option_var.get()
        find_id = self.find_id_entry.get()
        if find_option == "Employee":
            self.mySystem.findEmployee(find_id)
        elif find_option == "Event":
            self.mySystem.findEvent(find_id)
        elif find_option == "Client":
            self.mySystem.findClient(find_id)
        elif find_option == "Supplier":
            self.mySystem.findSupplier(find_id)
        elif find_option == "Guest":
            self.mySystem.findGuest(find_id)
        else:
            self.mySystem.findVenue(find_id)

    def get_all_info(self):
        print(f"Employees: {self.mySystem.getEmployees()}")
        print("")
        print(f"Events: {self.mySystem.getEvents()}")
        print("")
        print(f"Suppliers: {self.mySystem.getSuppliers()}")
        print("")
        print(f"Guests: {self.mySystem.getGuests()}")
        print("")
        print(f"Venues: {self.mySystem.getVenues()}")

    def delete_info(self):
        # When we use the delete button this function will run.
        # We look at the selected options
        # Then look for a specific ID in that option
        # For example, if you select "Employee", we will look for an employee with that ID
        # Then we delete that employee
        find_option = self.find_option_var.get()
        find_id = self.find_id_entry.get()
        if find_option == "Employee":
            self.mySystem.deleteEmployee(find_id)
        elif find_option == "Event":
            self.mySystem.deleteEvent(find_id)
        elif find_option == "Client":
            self.mySystem.deleteClient(find_id)
        elif find_option == "Supplier":
            self.mySystem.deleteSupplier(find_id)
        elif find_option == "Guest":
            self.mySystem.deleteGuest(find_id)
        else:
            self.mySystem.deleteVenue(find_id)

    def submit_info(self):
        # When we use the submit button this function will run
        # Here we take the values in each grid then put the value of the entries into a list
        # We make a dictionary to temporarily store them
        grid_info = {}
        for label, entries in self.grid_values.items():
            entry_values = [entry.get() for entry in entries]
            grid_info[label] = entry_values

        employee_values = grid_info.get("Employee", [])
        empployeeID = employee_values[0]

        client_values = grid_info.get("Client", [])
        clientID = client_values[0]

        guest_values = grid_info.get("Guest", [])
        guestID = guest_values[0]

        venue_values = grid_info.get("venue", [])
        venueID = venue_values[0]

        # This is so we don't miss the guest list parameter
        event_values = grid_info.get("Event", [])
        eventID = event_values[0]
        event_params = [
            event_values[0],  # eventID
            event_values[1],  # eventType
            event_values[2],  # theme
            event_values[3],  # date
            event_values[4],  # time
            event_values[5],  # duration
            event_values[6],  # venueAddress
            event_values[7],  # clientID
            [],  # guestList (empty list)
            event_values[8],  # cateringComp
            event_values[9],  # cleaningComp
            event_values[10],  # decorationComp
            event_values[11],  # entertainmentComp
            event_values[12],  # furnitureComp
            event_values[13]  # invoice
        ]

        supplier_values = grid_info.get("Supplier", [])
        supplierID = supplier_values[0]

        # Here we unpack the values in the entries and create the objects
        # We also make sure to filter out anything we didn't mean to create
        if empployeeID != "":
            self.mySystem.createEmployee(*grid_info.get("Employee", []))
        if clientID != "":
            self.mySystem.createClient(*grid_info.get("Client", []))
        if guestID != "":
            self.mySystem.createGuest(*grid_info.get("Guest", []))
        if venueID != "":
            self.mySystem.createVenue(*grid_info.get("Venue", []))
        if eventID != "":
            self.mySystem.createEvent(*event_params)
        if supplierID != "":
            self.mySystem.createSupplier(*grid_info.get("Supplier", []))




# Some test-cases before GUI
# First lets do one for employees
manager1 = Manager("Andrew", "M00001", "Managing", 20000, 32,
                   "3/5/1992", "Passport",None)
emp1 = Employee("emp1", "E00001", "Sales", "Salesperson", 15000, 20,
                "3/5/2004", "Passport", None)

#Let us display both
manager1.displayDetails()
print("")
emp1.displayDetails()
print("")
print("")

# Let us try changing the mangerID of emp1 to manager1's ID
print("Changing managers:")
manager1.addEmployee(emp1)
manager1.displayDetails()
print("")
emp1.displayDetails()
print("")
print("")

# Now lets try making the manager alter some information about the employee
manager1.setEmployeeSalary(emp1, 17000)
manager1.setEmployeeDepartment(emp1, "Sales 2")
manager1.removeEmployee(emp1)
print("Changing employee info then removing them via manager:")
emp1.displayDetails()
manager1.addEmployee(emp1)
print("")
print("")

# Now that it works we returned the employee back and will start working on clients, event, venues, suppliers
# and guests
client1 = Client("C00001", "Ahmad", 19, "26/12/2004", "Home",
                "Phone number: 123456789", 8000)
guest1 = Guest("G00001", "Mohammed", 19, "20/12/2004", "Home2",
               "Phone Number: 1231341413")
guest2 = Guest("G00002", "Pancake", 19, "22/6/2004", "Home3",
               "Phone Number: 8591471238")
venue1 = Venue("V00001", "Graduation 1", "Stadium section 1",
               "Email: Graduation@gmail.com", 20, 50)

cateringSupplier = Supplier("S00001", "Jerry's Food", "Catering Section",
                            "Email: jerryFood@gmail.com","Menu1", 10, 50)
cleanSupplier = Supplier("S00002", "Jerry's Cleaning", "Cleaning Section",
                            "Email: jerryClean@gmail.com",None, 10, 50)
furnitureSupplier = Supplier("S00003", "Jerry's Furniture", "Furniture Section",
                            "Email: jerryFurniture@gmail.com","Menu1", 10, 50)
decorationSupplier = Supplier("S00004", "Jerry's Decorations", "Decoration section",
                            "Email: jerryDecoration@gmail.com",None, 10, 50)
entertainmentSupplier = Supplier("S00005", "Jerry's Entertainment", "Entertainment section",
                            "Email: jerryEntertainment@gmail.com",None, 10, 50)

# Before creating events and sending invites
print(f"Before creating events and sending invites: ")
client1.displayDetails()
print("")
guest1.displayDetails()
print("")
guest2.displayDetails()
print("")
venue1.displayDetails()
print("")
cateringSupplier.displayDetails()
print("")
cleanSupplier.displayDetails()
print("")
furnitureSupplier.displayDetails()
print("")
decorationSupplier.displayDetails()
print("")
entertainmentSupplier.displayDetails()
print("")
print("")

# After creating event
# The client as to create it
event1 = client1.createEvent("E00001", "Graduation", "Formal", "3/5/2024", "14:00",
                             "2 hours", venue1, [guest1], cateringSupplier, cleanSupplier,
                             furnitureSupplier, decorationSupplier, entertainmentSupplier, 2000)
print("Event and after creating it: ")
event1.displayDetails()
print("")
client1.displayDetails()
print("")
guest1.displayDetails()
print("")
guest2.displayDetails()
print("")
print("")

# Let us send an invitation to guest 2 and remove guest 1's and bring them back after
event1.addGuest(guest2)
event1.removeGuest(guest1)

event1.displayDetails()
print("")
guest1.displayDetails()
print("")
guest2.displayDetails()
event1.addGuest(guest1)
print("")
print("")

# Now let us put everything into the system after creating it
emps = [manager1, emp1]
events = [event1]
clients = [client1]
suppliers = [cateringSupplier, cleanSupplier,furnitureSupplier, decorationSupplier, entertainmentSupplier]
guests = [guest1, guest2]
venues = [venue1]

system1 = System(emps, events, clients, suppliers, guests, venues)
# Let us print out the files content to make sure it is correct
print("File content: ")
print(f"Employees: {system1.getEmployees()}")
print("")
print(f"Events: {system1.getEvents()}")
print("")
print(f"Suppliers: {system1.getSuppliers()}")
print("")
print(f"Guests: {system1.getGuests()}")
print("")
print(f"Venues: {system1.getVenues()}")
print("")
print(f"The info is correct")
print("")
print("")

# Now that we confirmed that it works lets try creating another employee, another guest, deleting the guest,
# then finding a guest after and before modifying them.
system1.createEmployee("E00002", "emp2", "Sales", "Salesperson", 15000,
                       19, "21/10/2004", "Passport", None)
system1.createGuest("G00003", "Human", 19, "25/5/2024", "home4",
                    "14314341")
print("After adding a guest and an employee: ")
print(f"Employees: {system1.getEmployees()}")
print("")
print(f"Guests: {system1.getGuests()}")
print("")
print("")
print("Before altering guest (and using the find function): ")
system1.findGuest("G00003")
# We alter using this same create function
# Leave an empty string if you don't want to alter
system1.createGuest("G00003", "", "", "", "Hotel 5",
                    "000000")
print("")
print("After altering guest: ")
system1.findGuest("G00003")
print("")
print("After deleting the new employee: ")
system1.deleteEmployee("E00002")
print(f"Employees: {system1.getEmployees()}")

# Here is the GUI to be able to test the same functions in the system
# It is fully functional
# If an entry is empty, it won't be modified
# Keep in mind, everything depends on the ID.
# The ID is the only thing that can't be modified
# An empty entry won't create an object
myGUI = GUI()