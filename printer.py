class PrinterError(RuntimeError):
    pass


class Printer:
    def __init__(self, pages_per_sec, capacity):
        self.pages_per_sec = pages_per_sec
        self.capacity = capacity

    def Print(self, pages):
        if pages > self.capacity:
            raise PrinterError("Printer does not have enough capacity for all these pages . ")

        self.capacity = self.capacity-pages

        return f"Printed {pages} pages in {pages/self.pages_per_sec:.2f} seconds ."
