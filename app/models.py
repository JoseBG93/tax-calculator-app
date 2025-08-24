'''Import SQLAlchemy components for database modeling'''
from app import db # This imports the db object we created in __init__.py
from datetime import datetime # For handling dates and timestamps
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey, Text
# There are two ways to use relationships in SQLAlchemy with Flask:
# 1. Import directly from SQLAlchemy: 
#    from sqlalchemy.orm import relationship
#    Then use relationship() in your models.
# 2. Use the Flask-SQLAlchemy extension's db object:
#    Use db.relationship() in your models without importing relationship directly.
# Both approaches work, but it's best to be consistent. 
# If you use db.Model as your base class (as in Flask apps), prefer db.relationship for clarity and integration.


class People(db.Model): # We use db.Model to define a SQLAlchemy model. In this case, the model is a table called 'people'.
    """Represents people involved in the real estate transactions"""
    id = db.Column(db.Integer, primary_key=True) # Primary key is an unique identifier for each person, and it automatically includes 'unique=True', 'nullable=False' and auto-increment.
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.UTC)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.UTC, onupdate=datetime.UTC) # 'onupdate' means every time the record is modified, this timestamp is automatically updated.
    person_type = db.Column(db.String(20), nullable=False, default='Física')
    nif = db.Column(db.String(9), nullable=False, unique=True) # 'nullable=False' means it can't be empty, so every person must have a NIF. 'Unique=True' means duplicate NIFs are not allowed.
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    notification_address = db.Column(db.String(50), nullable=False, unique=False)

    def __repr__(self):
        return f"<Person: {self.name} {self.surname}>"


class Property(db.Model):
    """Represents real estate properties"""
    id = db.Column(db.Integer, primary_key=True) # Primary key is an unique identifier for each property, and it automatically includes 'unique=True', 'nullable=False' and auto-increment.
    town = db.Column(db.String(10), nullable=False, default='Alfafar')
    address = db.Column(db.String(50), nullable=False, unique=True)
    cadastral_reference = db.Column(db.String(20), nullable=False, unique=True)
    cadastral_value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.UTC)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.UTC, onupdate=datetime.UTC)

    def __repr__(self):
        return f"<Property with cadastral reference {self.cadastral_reference}, located in {self.address}>"


class Transaction(db.Model): # This is a table called 'transactions', which handles relationship between both tables 'people' and 'property'
    """Represents real estate transactions"""
    id = db.Column(db.Integer, primary_key=True) # Primary key is an unique identifier for each transaction, and it automatically includes 'unique=True', 'nullable=False' and auto-increment.
    transaction_type = db.Column(db.String(10), nullable=False) # Sale or inheritance
    transaction_date = db.Column(db.DateTime, nullable=False)
    transaction_value = db.Column(db.Float, nullable=False)

    # Add foreign keys to connect the tables.
    property_id = db.Column(db.Integer, ForeignKey('property.id'), nullable=False)
    grantor_id = db.Column(db.Integer, ForeignKey('people.id'), nullable=True) # Person selling (only for sales)
    grantee_id = db.Column(db.Integer, ForeignKey('people.id'), nullable=True) # Person buying (only for sales)
    decedent_id = db.Column(db.Integer, ForeignKey('people.id'), nullable=True) # Person who died (only for inheritances)
    heir_id = db.Column(db.Integer, ForeignKey('people.id'), nullable=True) # Person who inherits (only for inheritances)

    # Add relationships for an easy navigation between tables.
    property = db.relationship('Property', backref='transactions') # Forward: transaction.property gets the property. Reverse: property.transactions gets all transactions for that property.
    grantor = db.relationship('People', foreign_keys=[grantor_id], backref='selling') # FORWARD: transaction.grantor gets the seller from the 'people' table. REVERSE: people.selling gets all sales by that person.
    grantee = db.relationship('People', foreign_keys=[grantee_id], backref='buying') # FORWARD: transaction.grantee gets the buyer from the 'people' table. REVERSE: people.buying gets all purchases by that person.
    decedent = db.relationship('People', foreign_keys=[decedent_id], backref='deceasing') # FORWARD: transaction.decedent gets the deceased from the 'people' table. REVERSE: people.deceasing gets all deaths for that person.
    heir = db.relationship('People', foreign_keys=[heir_id], backref='inheriting') # FORWARD: transaction.heir gets the heir from the 'people' table. REVERSE: people.inheriting gets all inheritances by that person.

    def __repr__(self):
        return f"<Transaction id={self.id}, type={self.transaction_type}, date={self.transaction_date}>"

class TaxCalculation(db.Model):
    """IIVTNU tax calculations for transmissions"""
    id = db.Column(db.Integer, primary_key=True) # Primary key is an unique identifier for each tax calculation, and it automatically includes 'unique=True', 'nullable=False' and auto-increment.
    transaction_id = db.Column(db.Integer, ForeignKey('transaction.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.UTC)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.UTC, onupdate=datetime.UTC)

    """IIVTNU calculation results"""
    taxable_base = db.Column(db.Float, nullable=False)              # Base imponible - the calculated tax base
    gross_tax = db.Column(db.Float, nullable=False)                 # Cuota íntegra - gross tax amount before bonifications  
    bonification = db.Column(db.Float, nullable=False, default=0.0) # Bonificación - family discounts/reductions
    net_tax = db.Column(db.Float, nullable=False)                   # Cuota líquida - final amount taxpayer pays

    """Calculation parameters used"""
    tax_rate = db.Column(db.Float, nullable=False)               # Tipo gravamen - tax percentage applied (29% Alfafar)
    coefficients = db.Column(db.String(100), nullable=False)     # Coeficientes - calculation coefficients used
    
    # Add relationships for an easy navigation between tables.
    transaction = db.relationship('Transaction', backref='tax_calculation') # Forward: tax_calculation.transaction gets the transaction. Reverse: transaction.tax_calculation gets all tax calculations for that transaction.

    def __repr__(self):
        return f"<TaxCalculation for transaction {self.transaction_id}>"