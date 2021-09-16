from unittest import TestCase
from printer import Printer, PrinterError


class Test_printer(TestCase):
    def setUp(self):            # setup is like init function specially built which runs each time a test occurs .
        self.printer = Printer(2.0, 300)

    def test_printer_normal(self):
        message = self.printer.Print(25)
        self.assertEqual("Printed 25 pages in 12.50 seconds .", message)

    def test_printer_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.Print(350)

    def test_printer_exact(self):
        message = self.printer.Print(300)
        self.assertEqual("Printed 300 pages in 150.00 seconds .", message)

    def test_printer_speed(self):
        pages = 10
        message = "Printed 10 pages in 5.00 seconds ."
        result = self.printer.Print(pages)
        self.assertEqual(result, message)

    def test_printer_value_places(self):
        fast_printer = Printer(3.0, 300)
        pages = 11
        message = "Printed 11 pages in 3.67 seconds ."

        result = fast_printer.Print(pages)
        self.assertEqual(result, message)

    def test_printer_multiple_print(self):
        self.printer.Print(25)
        self.printer.Print(20)
        self.printer.Print(250)

    def test_printer_multiple_print_error(self):
        with self.assertRaises(PrinterError):
            self.printer.Print(25)
            self.printer.Print(50)
            self.printer.Print(250)