from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import Invoice, Items, PurchaseRequest, PurchaseOrder, PurchaseReceiving, PaymentRequest, CheckIssuance, Supplier

from my_flask_app import db


views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('login.html') 

@views.route('/home')   
def home():
    print('Session:', session)
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


@views.route('/purchasing/purchase_request', methods=['POST'])
def submit_purchase_request():
    suppliers = Supplier.query.all()
    active_tab = 'purchase_request'

    # Compute new ref_no as the largest ref_no + 1
    from .models import PurchaseRequestItems, PurchaseRequest
    last_ref = db.session.query(PurchaseRequest.ref_no).order_by(PurchaseRequest.ref_no.desc()).first()
    try:
        new_ref_no = str(int(last_ref[0]) + 1) if last_ref and last_ref[0] and last_ref[0].isdigit() else '1'
    except Exception:
        new_ref_no = '1'
    ref_no = new_ref_no

    # Get all product details from the form
    product_ids = request.form.getlist('product_id[]')
    product_names = request.form.getlist('product_name[]')
    item_types = request.form.getlist('item_type[]')
    product_types = request.form.getlist('product_type[]')
    descriptions = request.form.getlist('description[]')
    units = request.form.getlist('unit[]')
    quantities = request.form.getlist('quantity[]')

    # Insert items into purchaserequestitems first
    for i in range(len(product_ids)):
        if product_ids[i] and product_names[i]:
            item = PurchaseRequestItems(
                ref_no=ref_no,
                product_id=product_ids[i],
                product_name=product_names[i],
                item_type=item_types[i],
                product_type=product_types[i],
                description=descriptions[i],
                unit=units[i],
                quantity=quantities[i]
            )
            db.session.add(item)
    db.session.flush()  # Ensure items are staged before the request

    # Now insert the purchase request record
    new_request = PurchaseRequest(
        request_date=request.form['date'],
        request_type=request.form['type'],
        date_needed=request.form['date_needed'],
        requestor=request.form['requested_by'],
        department=request.form['department'],
        purpose=request.form['purpose'],
        remarks=request.form['remarks'],
        ref_no=ref_no,
        request_status='Approved'
    )
    db.session.add(new_request)
    db.session.commit()
    flash(f'Purchase request submitted successfully! Reference No: {ref_no}', 'success')
    return redirect(url_for('views.purchasing', activeTab=active_tab))

@views.route('/purchasing', methods=['GET', 'POST'])
def purchasing():
    if request.method == 'POST':
        active_tab = request.form.get('activeTab')
    else:
        active_tab = request.args.get('activeTab')

    print(active_tab)
    flash(f"Active Tab: {active_tab}", 'info')
    purchase_request_details = None  # Initialize variable to hold purchase request details

    date = datetime.now()
    date = date.strftime("%Y-%m-%d")

    # Query supplier data from the Supplier model
    suppliers = Supplier.query.all()

    # Query products for the purchase request dropdown
    from .models import Product, PurchaseRequest
    products = Product.query.all()
    products_dicts = []
    for p in products:
        products_dicts.append({
            'product_id': p.product_id,
            'product_name': p.product_name,
            'type': p.type,
            'product_type': p.product_type,
            'description': p.description,
            'unit': p.unit,
            'quantity': p.quantity
        })

    # Query reference_nos for purchase order dropdown (filterable)
    reference_nos = db.session.query(
        PurchaseRequest.ref_no,
        PurchaseRequest.request_type.label('type'),
        PurchaseRequest.purpose.label('product_type'),
        PurchaseRequest.department.label('supplier_id')
    ).all()

    # Remove the purchase_request POST logic from here
    if active_tab == 'purchase_order':
        print("purchorder")
    elif active_tab == 'purchase_receiving':
        print("purcheceiving")
    # Query data for Purchase Orders
    purchase_orders = PurchaseOrder.query.all()  # Assuming a model named PurchaseOrder exists
    # Query data for Purchase Receiving
    purchase_receiving = PurchaseReceiving.query.all()  # Assuming a model named PurchaseReceiving exists
    return render_template('Purchasing.html',
                           purchase_request_details=purchase_request_details,  # Pass the details to the template
                           suppliers=suppliers,  # Pass suppliers to the template
                           purchase_orders=purchase_orders,
                           purchase_receiving=purchase_receiving, current_date=date, active_tab=active_tab, products=products_dicts, reference_nos=reference_nos)


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

@views.route('/get_supplier_info/<int:supplier_id>', methods=['GET'])
def get_supplier_info(supplier_id):
    supplier = Supplier.query.get(supplier_id)
    if supplier:
        return {
            'address': supplier.address,
            'attention': supplier.attention
        }
    return {'error': 'Supplier not found'}, 404

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        from .models import db, Users
        user = Users.query.filter_by(username=username).first()
        
        if user and hasattr(user, 'password') and user.password == password:
            flash('Login successful!', 'success')
            # Set user info in session
            session['first_name'] = user.first_name
            session['last_name'] = user.last_name
            session['department'] = user.department
            session['position'] = user.position
            return redirect(url_for('views.home'))
        else:
            flash('Invalid username or password.', 'error')
            return render_template('login.html')
    return render_template('login.html')
