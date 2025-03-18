from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Invoice, Items, PurchaseRequest, PurchaseOrder, PurchaseReceiving, PaymentRequest, CheckIssuance

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



from datetime import datetime

@views.route('/purchasing', methods=['GET', 'POST'])

def purchasing():
    date = datetime.now()
    date = date.strftime("%Y-%m-%d")
    print("initial")
    if request.method == 'POST':
        request_id = request.form.get('request_id')
        if request_id:
            # Query the database for the corresponding record
            purchase_request = PurchaseRequest.query.filter_by(request_id=request_id).first()

            if purchase_request:
                # Render the template with the found purchase request
                # Insert the new purchase request into the database
                print(date)
                return redirect(url_for('views.purchasing'))

            
            
        else:
            print("insert")
            new_request = PurchaseRequest(
                date=request.form['date'],
                type=request.form['type'],
                ref_no=request.form['ref_no'],
                date_needed=request.form['date_needed'],
                requested_by=request.form['requested_by'],
                department=request.form['department'],
                purpose=request.form['purpose'],
                remarks=request.form['remarks']
            )
            db.session.add(new_request)
            db.session.commit()
            flash('Purchase request submitted successfully!', 'success')
            return render_template('Purchasing.html', error="No record found for the given Request ID.")
    
    # Query data for Purchase Requests
    purchase_request = PurchaseRequest.query.all()  # Assuming a model named PurchaseRequest exists
    print(purchase_request)
    # Query data for Purchase Orders
    purchase_orders = PurchaseOrder.query.all()  # Assuming a model named PurchaseOrder exists

    # Query data for Purchase Receiving
    purchase_receiving = PurchaseReceiving.query.all()  # Assuming a model named PurchaseReceiving exists
    
    print("final")
    return render_template('Purchasing.html', 
                           purchase_request=purchase_request,
                           purchase_orders=purchase_orders,
                           purchase_receiving=purchase_receiving, current_date=date)




@views.route('/disbursement', methods=['GET', 'POST'])
def disbursement():
    if request.method == 'POST':
        # Process form data here
        form_data = request.form
        # Add your form processing logic here
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('views.disbursement'))

    # Query data for Payment Requests
    payment_requests = PaymentRequest.query.all()  # Assuming a model named PaymentRequest exists

    # Query data for Check Issuance
    check_issuance = CheckIssuance.query.all()  # Assuming a model named CheckIssuance exists

    # Query data for Check Clearing
    check_clearing = CheckIssuance.query.all()  # Assuming a model named CheckClearing exists

    return render_template('Disbursement.html', 
                           payment_requests=payment_requests,
                           check_issuance=check_issuance,
                           check_clearing=check_clearing)
