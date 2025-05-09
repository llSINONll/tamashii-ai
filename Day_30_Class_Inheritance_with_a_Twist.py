#Challenge_1 (Class Inheritance)

'''
🔮 Scenario:
You're tasked with modeling a simple hierarchy of electronic devices.
Start with a base class and extend it to more specific devices.

✅ Your Tasks:
Create a base class Device with:

Attributes: brand, power_status (default to False)

Methods:

turn_on() – sets power_status to True

turn_off() – sets power_status to False

status() – prints the current power status

Create a subclass Smartphone that inherits from Device and adds:

Attribute: phone_number

Method:

make_call(number) – prints a message indicating a call from phone_number
to number

Create another subclass Laptop that inherits from Device and adds:

Attribute: operating_system

Method:

run_program(program_name) – prints a message indicating that the program
is running on the laptop

Demonstrate the functionality by creating instances of Smartphone and
Laptop, turning them on, and invoking their specific methods.

🧪 Sample Output:

Device is now ON.
Calling 123-456-7890 from 987-654-3210...
Device is now ON.
Running Visual Studio Code on Windows 10...
'''

'''
class Device:
    def __init__(self, brand):
        self.brand = brand
        self.power_status = False

    def turn_on(self):
        self.power_status = True
        print("Device is now ON.")

    def turn_off(self):
        self.power_status = False
        print("Device is now OFF.")

    def status(self):
        state = "ON" if self.power_status else "OFF"
        print(f"The device is currently {state}.")

class Smartphone(Device):
    def __init__(self, brand, phone_number):
        super().__init__(brand)
        self.phone_number = phone_number

    def make_call(self, number):
        if self.power_status:
            print(f"Calling {number} from {self.phone_number}...")
        else:
            print("Cannot make a call. The device is OFF.")

class Laptop(Device):
    def __init__(self, brand, operating_system):
        super().__init__(brand)
        self.operating_system = operating_system

    def run_program(self, program_name):
        if self.power_status:
            print(f"Running {program_name} on {self.operating_system}...")
        else:
            print("Cannot run program. The device is OFF.")

# Demonstration
phone = Smartphone("TechBrand", "987-654-3210")
laptop = Laptop("CompTech", "Windows 10")

phone.turn_on()
phone.make_call("123-456-7890")

laptop.turn_on()
laptop.run_program("Visual Studio Code")
'''
