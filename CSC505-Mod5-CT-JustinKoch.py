# Module 5: Critical Thinking Assignment (PHTRS)
# Use Python to write a script that will print out the different actors and use cases.

# Create pothole report class and define the attributes the system will track
class PotholeReport:
  def __init__(self, citizen_name, address, size, location):
    self.citizen_name = citizen_name
    self.address = address
    self.size = size
    self.location = location

# Display the pothole report details in the console 
  def display_report(self):
    print("Pothole Report:")
    print(f"Citizen Name: {self.citizen_name}")
    print(f"Address: {self.address}")
    print(f"Size: {self.size}")
    print(f"Location: {self.location}")

# Capture user input to fill out details of the report attributes
  @classmethod
  def create_from_input(cls):
    citizen_name = input("Enter full name: ")
    address = input("Enter the address of the pothole: ")
    size = int(input("Enter the size of the pothole (1-10): "))
    location = input("Enter the location of the pothole (e.g., curb, street, sidewalk): ")
    return cls(citizen_name, address, size, location)

# Create workorder class and define the attributes the system will track
class WorkOrder:
  def __init__(self, pothole_report, pothole_id):
    self.pothole_id = pothole_id
    self.address = pothole_report.address
    self.size = pothole_report.size
    self.priority =  pothole_report.size
    if pothole_report.size <= 3:
        self.priority = "Small"
    elif pothole_report.size <= 6:
        self.priority = "Medium"
    else:
        self.priority = "Large"
    
# Display the work order details in the console
  def display_work_order(self):
    """Prints the work order information."""
    print("\nWork Order:")
    print(f"Pothole ID: {self.pothole_id}")
    print(f"Address: {self.address}")
    print(f"Size: {self.size}")
    print(f"Priority: {self.priority}")

# Example usage
pothole_report = PotholeReport.create_from_input()
pothole_report.display_report()

pothole_id = 1  # (replace with ID generation)
work_order = WorkOrder(pothole_report, pothole_id)
work_order.display_work_order()