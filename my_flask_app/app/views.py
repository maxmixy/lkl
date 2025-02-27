from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Invoice, Items

from my_flask_app import db


views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html') 

@views.route('/invoice', methods=['GET', 'POST'])
def invoice():
    group_no = request.args.get('group_no')
    invoice_no = request.args.get('invoice_no')
    invoice_data = None
    items = []
    invoices = []
    current_index = 0
    
    if group_no:
        try:
            group_no = int(group_no)
            invoices = Invoice.query.filter_by(GroupID=group_no).all()
            if invoices:
                if invoice_no:
                    invoice_no = int(invoice_no)
                    invoice_data = next((inv for inv in invoices if inv.InvoiceID == invoice_no), None)
                else:
                    invoice_data = invoices[0]
                    invoice_no = invoice_data.InvoiceID
                
                if invoice_data:
                    items = Items.query.join(Invoice, Items.ItemID == Invoice.ItemID)\
                                    .filter(Invoice.InvoiceID == invoice_no)\
                                    .all()
                    
                    current_index = next((i for i, inv in enumerate(invoices) if inv.InvoiceID == invoice_no), 0)


                flash('Invoice found successfully!', 'success')
            else:
                flash('Invoice not found', 'error')
        except ValueError:
            flash('Invalid invoice number format', 'error')
    
    # Pass all invoice fields to template
    return render_template('InvoiceForm.html', 
                         invoice=invoice_data,
                         items=items,
                         invoices=invoices,
                         current_index=current_index,
                         invoice_id=invoice_data.InvoiceID if invoice_data else None,

                         inv_date=invoice_data.InvDate.strftime('%Y-%m-%d') if invoice_data else None,
                         inv_type=invoice_data.InvType if invoice_data else None,
                         proj_id=invoice_data.ProjID if invoice_data else None,
                         customer_id=invoice_data.CustomerID if invoice_data else None,
                         acc_man_id=invoice_data.AccManID if invoice_data else None,
                         lead_div=invoice_data.LeadDiv if invoice_data else None,
                         remarks=invoice_data.Remarks if invoice_data else None,
                         int_terms=invoice_data.IntTerms if invoice_data else None,
                         cus_terms=invoice_data.CusTerms if invoice_data else None,
                         payment_type=invoice_data.PaymentType if invoice_data else None,
                         tpc_contact=invoice_data.TPCContact if invoice_data else None,
                         tpc_gross=invoice_data.TPCGross if invoice_data else None,
                         gross=invoice_data.Gross if invoice_data else None,
                         debit=invoice_data.Debit if invoice_data else None,
                         returns=invoice_data.Returns if invoice_data else None,
                         credit=invoice_data.Credit if invoice_data else None,
                         payment=invoice_data.Payment if invoice_data else None,
                         balance=invoice_data.Balance if invoice_data else None)



    
@views.route('/receipt')
def receipt():
    return render_template('InvoiceReceipt.html')

@views.route('/submit_invoice', methods=['POST'])
def submit_invoice():
    # Process form data here
    invoice_data = request.form
    # Add your invoice processing logic
    return redirect(url_for('views.invoice'))

@views.route('/main')
def main():
    return render_template('index.html')

@views.route('/sales-and-collection')
def sales_and_collection():
    current_index = 0
    invoices = []  # Default values for the variables

    group_no = request.args.get('group_no')
    invoice_no = request.args.get('invoice_no')
    invoice_data = None
    items = []
    invoices = []
    current_index = 0
    
    if group_no:
        try:
            group_no = int(group_no)
            invoices = Invoice.query.filter_by(GroupID=group_no).all()
            if invoices:
                if invoice_no:
                    invoice_no = int(invoice_no)
                    invoice_data = next((inv for inv in invoices if inv.InvoiceID == invoice_no), None)
                else:
                    invoice_data = invoices[0]
                    invoice_no = invoice_data.InvoiceID
                
                if invoice_data:
                    items = Items.query.join(Invoice, Items.ItemID == Invoice.ItemID)\
                                    .filter(Invoice.InvoiceID == invoice_no)\
                                    .all()
                    
                    current_index = next((i for i, inv in enumerate(invoices) if inv.InvoiceID == invoice_no), 0)


                flash('Invoice found successfully!', 'success')
            else:
                flash('Invoice not found', 'error')
        except ValueError:
            flash('Invalid invoice number format', 'error')
    
    # Pass all invoice fields to template
    return render_template('SalesAndCollection.html', 
                         invoice=invoice_data,
                         items=items,
                         invoices=invoices,
                         current_index=current_index,
                         invoice_id=invoice_data.InvoiceID if invoice_data else None,

                         inv_date=invoice_data.InvDate.strftime('%Y-%m-%d') if invoice_data else None,
                         inv_type=invoice_data.InvType if invoice_data else None,
                         proj_id=invoice_data.ProjID if invoice_data else None,
                         customer_id=invoice_data.CustomerID if invoice_data else None,
                         acc_man_id=invoice_data.AccManID if invoice_data else None,
                         lead_div=invoice_data.LeadDiv if invoice_data else None,
                         remarks=invoice_data.Remarks if invoice_data else None,
                         int_terms=invoice_data.IntTerms if invoice_data else None,
                         cus_terms=invoice_data.CusTerms if invoice_data else None,
                         payment_type=invoice_data.PaymentType if invoice_data else None,
                         tpc_contact=invoice_data.TPCContact if invoice_data else None,
                         tpc_gross=invoice_data.TPCGross if invoice_data else None,
                         gross=invoice_data.Gross if invoice_data else None,
                         debit=invoice_data.Debit if invoice_data else None,
                         returns=invoice_data.Returns if invoice_data else None,
                         credit=invoice_data.Credit if invoice_data else None,
                         payment=invoice_data.Payment if invoice_data else None,
                         balance=invoice_data.Balance if invoice_data else None)

    return render_template('SalesAndCollection.html', current_index=current_index, invoices=invoices)

