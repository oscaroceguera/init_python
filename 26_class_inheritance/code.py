class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_apges = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_apges} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("your printer is not connected!")
            return
        print('Printing {pages} pages.')
        self.remaining_apges -= pages


printer = Printer("printer", "USB", 500)

printer.print(20)

print(printer)

printer.disconnect()
printer.print(30)
