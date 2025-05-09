from my_flask_app import db

from datetime import datetime

class Employee(db.Model):

    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.Integer, nullable=True)


class Invoice(db.Model):
    GroupID = db.Column(db.Integer, primary_key=True)
    InvoiceID = db.Column(db.Integer, primary_key=True)
    InvDate = db.Column(db.Date, nullable=False)
    InvType = db.Column(db.String(20), nullable=False)
    ProjID = db.Column(db.Integer, nullable=False)
    CustomerID = db.Column(db.Integer, nullable=False)
    AccManID = db.Column(db.Integer, nullable=False)
    LeadDiv = db.Column(db.String(20), nullable=False)
    Remarks = db.Column(db.Text, nullable=False)
    IntTerms = db.Column(db.Integer, nullable=False)
    CusTerms = db.Column(db.Integer, nullable=False)
    PaymentType = db.Column(db.String(20), nullable=False)
    ItemID = db.Column(db.Integer, primary_key=True)
    TPCContact = db.Column(db.Text, nullable=False)
    TPCGross = db.Column(db.Float, nullable=False)
    Gross = db.Column(db.Float, nullable=False)
    Returns = db.Column(db.Float, nullable=False)
    Payment = db.Column(db.Float, nullable=False)
    Debit = db.Column(db.Float, nullable=False)
    Credit = db.Column(db.Float, nullable=False)
    Balance = db.Column(db.Float, nullable=False)


class Items(db.Model):
    ItemID = db.Column(db.Integer, primary_key=True)
    ItemName = db.Column(db.String(50), nullable=False)
    Status = db.Column(db.String(20), nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Accepted = db.Column(db.Float, nullable=False)
    Gross = db.Column(db.Float, nullable=False)
    Billed = db.Column(db.Float, nullable=False)
    Amount = db.Column(db.Float, nullable=False)

class PurchaseRequest(db.Model):
    __tablename__ = 'purchaserequests'
    request_id = db.Column(db.Integer, primary_key=True)
    request_date = db.Column(db.Date, nullable=False)
    request_type = db.Column(db.String(100), nullable=False)
    ref_no = db.Column(db.String(100), nullable=False)
    requestor = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    purpose = db.Column(db.String(200), nullable=False)
    remarks = db.Column(db.Text, nullable=True)
    request_status = db.Column(db.String(100), nullable=False)
    date_needed = db.Column(db.Date, nullable=False)

class PurchaseOrder(db.Model):
    __tablename__ = 'purchaseorder'
    OrderID = db.Column(db.Integer, primary_key=True)
    SupplierID = db.Column(db.Integer, nullable=True)
    OrderDate = db.Column(db.Date, nullable=True)
    TotalAmount = db.Column(db.Numeric(10, 2), nullable=True)
    order_id = db.Column(db.String(255), nullable=False)
    order_date = db.Column(db.Date, nullable=True)
    order_type = db.Column(db.String(255), nullable=False)
    product_type = db.Column(db.String(255), nullable=False)
    supplier = db.Column(db.String(255), nullable=False)
    terms = db.Column(db.Enum('1', '30', '60'), nullable=True)
    order_address = db.Column(db.String(255), nullable=False)
    currency = db.Column(db.Enum('Php', 'Usd', 'Cny'), nullable=True)
    attention = db.Column(db.String(255), nullable=False)
    currency_rate = db.Column(db.Numeric(10, 2), nullable=True)
    delivery_instructions = db.Column(db.Text, nullable=True)
    remarks = db.Column(db.Text, nullable=True)


class PurchaseReceiving(db.Model):
    __tablename__ = 'purchasereceiving'
    transactionNo = db.Column(db.String(255), nullable=False, primary_key=True)
    date = db.Column(db.Date, nullable=True)
    supplierCode = db.Column(db.String(255), nullable=False)
    supplierName = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(255), nullable=False)
    profitCenter = db.Column(db.String(255), nullable=False)
    receivedBy = db.Column(db.String(255), nullable=False)
    receivedDate = db.Column(db.Date, nullable=True)
    terms = db.Column(db.String(255), nullable=False)
    taxType = db.Column(db.String(255), nullable=False)
    ewt = db.Column(db.Numeric(10, 2), nullable=True)
    gross = db.Column(db.Numeric(10, 2), nullable=True)
    debit = db.Column(db.Numeric(10, 2), nullable=True)
    credit = db.Column(db.Numeric(10, 2), nullable=True)
    payment = db.Column(db.Numeric(10, 2), nullable=True)
    balance = db.Column(db.Numeric(10, 2), nullable=True)


class PaymentRequest(db.Model):
    __tablename__ = 'paymentrequest'
    request_id = db.Column(db.String(255), nullable=True, primary_key=True)
    date = db.Column(db.Date, nullable=True)
    supplier = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=False)
    purpose = db.Column(db.String(255), nullable=False)
    remarks = db.Column(db.Text, nullable=True)


class CheckIssuance(db.Model):
    __tablename__ = 'checkissuance'
    check_number = db.Column(db.String(255), primary_key=True, nullable=False)
    date_cleared = db.Column(db.Date, nullable=False)
    bank = db.Column(db.String(255), nullable=False)
    check_date = db.Column(db.Date, nullable=False)
    paid_to = db.Column(db.String(255), nullable=False)
    account_no = db.Column(db.String(255), nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    total_applied = db.Column(db.Numeric(10, 2), nullable=False)
    clearing_no = db.Column(db.String(255), nullable=False)
    clearing_date = db.Column(db.Date, nullable=False)
    company = db.Column(db.String(255), nullable=False)
    total_gross = db.Column(db.Numeric(10, 2), nullable=True)


class Supplier(db.Model):
    __tablename__ = 'suppliers'
    supplier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.Text, nullable=False)
    attention = db.Column(db.String(200), nullable=False)
