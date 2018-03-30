#Write import statements for classes invoice and invoice_item
'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''

from assignment9.invoice import Invoice
from assignment9.invoice_item import InvoiceItem

invoice = Invoice('ABC Company', '03282018')

    n = 'Y'
    while n == 'Y':

        invoice_item = InvoiceItem('Widget1', 10, 5)

        description = input('Description: ')
        quantity = int(input('Quantity: '))
        cost = float(input('Cost: '))

        invoice_item = InvoiceItem(description, quantity, cost)
        invoice.add_invoice_item(invoice_item)


        n = input("Press 'y' to enter another widget.. ")
        n = n.upper()

        if n != 'y':
            invoice.print_invoice()
