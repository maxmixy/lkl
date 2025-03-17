from my_flask_app import db

from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

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
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    purpose = db.Column(db.String(200), nullable=False)
    remarks = db.Column(db.Text, nullable=True)

class PurchaseOrder(db.Model):
    __tablename__ = 'purchaseorder'
    id = db.Column(db.Integer, primary_key=True)
    order_no = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    terms = db.Column(db.String(50), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

class PurchaseReceiving(db.Model):
    __tablename__ = 'purchasereceiving'
    id = db.Column(db.Integer, primary_key=True)
    transaction_no = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(100), nullable=False)

class PaymentRequest(db.Model):
    __tablename__ = 'paymentrequest'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    purpose = db.Column(db.String(200), nullable=False)
    remarks = db.Column(db.Text, nullable=True)

class CheckIssuance(db.Model):
    __tablename__ = 'checkissuance'
    id = db.Column(db.Integer, primary_key=True)
    check_number = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    bank = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
