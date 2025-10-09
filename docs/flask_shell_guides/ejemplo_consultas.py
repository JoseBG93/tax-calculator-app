"""
DATABASE QUERY EXAMPLES
=======================

This file demonstrates how to query database tables in your Flask application.
You can execute this code from Flask Shell or from any function in your app.

CREATED: October 2, 2025
AUTHOR: Tax Calculator Pro Team
"""

# ==============================================================================
# METHOD 1: FROM FLASK SHELL (INTERACTIVE MODE)
# ==============================================================================
# To use Flask Shell, open terminal in the project directory and run:
#
#   $ flask shell
#
# Flask Shell automatically loads your application and database context.
# Once inside, you can execute the commands below directly.


# --- IMPORT MODELS ---
from app.models import User, People, Property, Transaction, TaxCalculation


# ==============================================================================
# 📋 BASIC QUERIES
# ==============================================================================

# 1. GET ALL RECORDS
# ------------------
# .all() returns a LIST with all records from the table

users = User.query.all()
print(f"📊 Total users: {len(users)}")
print(users)  # Example: [<User: jose>, <User: admin>]

people = People.query.all()
print(f"📊 Total people: {len(people)}")

properties = Property.query.all()
print(f"📊 Total properties: {len(properties)}")

transactions = Transaction.query.all()
print(f"📊 Total transactions: {len(transactions)}")


# 2. GET A RECORD BY ID (Primary Key)
# ------------------------------------
# .get() searches by primary key (id) and returns ONE OBJECT or None

user = User.query.get(1)  # Find user with id=1
if user:
    print(f"✅ User found: {user.username}")
else:
    print("❌ User not found")

property_obj = Property.query.get(1)
if property_obj:
    print(f"🏠 Property: {property_obj.address}")


# 3. FILTER RECORDS
# -----------------
# .filter_by() allows filtering by any field
# Returns a QUERY OBJECT, you need .first() or .all() to get results

# Find a specific user
user = User.query.filter_by(username='jose').first()
# .first() returns the FIRST result or None

# Find a person by NIF
person = People.query.filter_by(nif='12345678A').first()

# Find property by cadastral reference
prop = Property.query.filter_by(cadastral_reference='1234567VH5797S').first()

# Find all "Sale" type transactions
sales = Transaction.query.filter_by(transaction_type='Venta').all()
print(f"💰 Total sales: {len(sales)}")


# 4. COUNT RECORDS
# ----------------
# .count() returns an INTEGER with the number of records

total_users = User.query.count()
print(f"👥 Total users in DB: {total_users}")

total_transactions = Transaction.query.count()
print(f"📝 Total transactions in DB: {total_transactions}")

# Count filtered transactions
total_sales = Transaction.query.filter_by(transaction_type='Venta').count()
print(f"💵 Total sales: {total_sales}")


# ==============================================================================
# 🔗 ADVANCED QUERIES (RELATIONSHIPS)
# ==============================================================================

# 5. NAVIGATE BETWEEN RELATED TABLES
# -----------------------------------
# Thanks to relationships defined in models.py, you can navigate easily

# Get a transaction
transaction = Transaction.query.first()

if transaction:
    # FORWARD: From Transaction to other tables
    print(f"🏠 Transaction property: {transaction.property.address}")
    print(f"👤 Buyer: {transaction.grantee.name if transaction.grantee else 'N/A'}")
    print(f"👤 Seller: {transaction.grantor.name if transaction.grantor else 'N/A'}")
    
    # REVERSE: From Property to Transaction
    property_obj = transaction.property
    print(f"📊 Transactions for this property: {len(property_obj.transactions)}")
    
    # View all transactions for a property
    for trans in property_obj.transactions:
        print(f"  ➜ {trans.transaction_type} on {trans.transaction_date}")


# 6. QUERIES WITH MULTIPLE CONDITIONS
# ------------------------------------
# You can chain multiple filters

# Active admin users
admin_users = User.query.filter_by(is_admin=True, is_active=True).all()
print(f"👑 Active admins: {len(admin_users)}")

# Properties in Alfafar with value greater than 100,000
expensive_properties = Property.query.filter_by(town='Alfafar').filter(
    Property.cadastral_value > 100000
).all()
print(f"💎 Expensive properties in Alfafar: {len(expensive_properties)}")


# ==============================================================================
# 📊 QUERIES WITH SORTING
# ==============================================================================

# 7. SORT RESULTS
# ---------------
from sqlalchemy import desc

# Sort users by creation date (most recent first)
recent_users = User.query.order_by(desc(User.created_at)).all()

# Sort properties by cadastral value (lowest to highest)
properties_by_value = Property.query.order_by(Property.cadastral_value).all()

# Sort transactions by date (oldest first)
transactions_by_date = Transaction.query.order_by(Transaction.transaction_date).all()


# ==============================================================================
# 🔢 QUERIES WITH LIMITS
# ==============================================================================

# 8. LIMIT RESULTS
# ----------------
# .limit() limits the number of results returned

# Get the first 5 users
first_five_users = User.query.limit(5).all()

# Get the 10 most recent transactions
recent_transactions = Transaction.query.order_by(
    desc(Transaction.transaction_date)
).limit(10).all()


# ==============================================================================
# 🚀 CUSTOM QUERIES (ADVANCED SQL)
# ==============================================================================

# 9. QUERIES WITH .filter() (More Flexible than .filter_by())
# ------------------------------------------------------------
# .filter() allows more complex conditions

# Find properties with value between 50,000 and 150,000
mid_range_properties = Property.query.filter(
    Property.cadastral_value >= 50000,
    Property.cadastral_value <= 150000
).all()

# Find users whose username contains "jose"
users_with_jose = User.query.filter(User.username.like('%jose%')).all()

# Find physical persons (not legal entities)
physical_persons = People.query.filter(People.person_type == 'Física').all()


# ==============================================================================
# 📚 SUMMARY OF MAIN METHODS
# ==============================================================================
"""
╔═════════════════════╦══════════════════════╦═════════════════════════╗
║ METHOD              ║ RETURNS              ║ EXAMPLE                 ║
╠═════════════════════╬══════════════════════╬═════════════════════════╣
║ .all()              ║ List of objects      ║ User.query.all()        ║
║ .first()            ║ One object or None   ║ User.query.first()      ║
║ .get(id)            ║ One object or None   ║ User.query.get(1)       ║
║ .count()            ║ Integer number       ║ User.query.count()      ║
║ .filter_by(field=x) ║ Query object         ║ User.query.filter_by()  ║
║ .filter(condition)  ║ Query object         ║ User.query.filter()     ║
║ .order_by(field)    ║ Query object         ║ User.query.order_by()   ║
║ .limit(n)           ║ Query object         ║ User.query.limit(5)     ║
╚═════════════════════╩══════════════════════╩═════════════════════════╝

⚠️  IMPORTANT:
   • .filter_by() and .filter() return a QUERY OBJECT, not direct data
   • You must add .all(), .first() or .count() at the end to get results
   • You can chain multiple methods:
     User.query.filter_by(...).order_by(...).limit(5).all()
"""


# ==============================================================================
# 💡 PRACTICAL EXAMPLES: COMBINING METHODS
# ==============================================================================

# Example 1: Get the 5 most recent active admin users
recent_admins = (
    User.query
    .filter_by(is_admin=True, is_active=True)
    .order_by(desc(User.created_at))
    .limit(5)
    .all()
)

# Example 2: Find properties in a specific town, sorted by value
alfafar_properties = (
    Property.query
    .filter_by(town='Alfafar')
    .order_by(Property.cadastral_value)
    .all()
)

# Example 3: Get total number of sales in the current year
from datetime import datetime

current_year = datetime.now().year
sales_this_year = (
    Transaction.query
    .filter_by(transaction_type='Venta')
    .filter(Transaction.transaction_date >= f'{current_year}-01-01')
    .count()
)
print(f"📅 Sales in {current_year}: {sales_this_year}")


# ==============================================================================
# 🔍 ADVANCED: JOIN QUERIES
# ==============================================================================

# Example: Get all transactions with property and people details
from sqlalchemy.orm import joinedload

# Eager loading to avoid N+1 query problem
transactions_with_relations = (
    Transaction.query
    .options(
        joinedload(Transaction.property),
        joinedload(Transaction.grantee),
        joinedload(Transaction.grantor)
    )
    .all()
)

# This loads all related data in a single query instead of multiple queries


# ==============================================================================
# 📖 HOW TO USE THIS FILE
# ==============================================================================
"""
OPTION 1: From Flask Shell
--------------------------
$ flask shell
>>> exec(open('ejemplo_consultas.py').read())

OPTION 2: Copy individual commands
-----------------------------------
$ flask shell
>>> from app.models import User
>>> users = User.query.all()
>>> print(users)

OPTION 3: From a route/function in your application
----------------------------------------------------
def my_route():
    from app.models import User
    users = User.query.all()
    return render_template('users.html', users=users)

OPTION 4: Create a custom management command
---------------------------------------------
# In app/cli.py
import click
from flask.cli import with_appcontext

@click.command('query-stats')
@with_appcontext
def query_stats():
    '''Display database statistics'''
    from app.models import User, Property, Transaction
    
    print(f"Users: {User.query.count()}")
    print(f"Properties: {Property.query.count()}")
    print(f"Transactions: {Transaction.query.count()}")

# Then run: $ flask query-stats
"""


# ==============================================================================
# 🎯 BEST PRACTICES
# ==============================================================================
"""
✅ DO:
   • Use .filter_by() for simple equality comparisons
   • Use .filter() for complex conditions (>, <, >=, <=, LIKE, etc.)
   • Always handle None values when using .first() or .get()
   • Use eager loading (.options(joinedload())) to avoid N+1 queries
   • Use .count() instead of len(.all()) for better performance
   • Chain methods for readable, expressive queries

❌ DON'T:
   • Don't forget to add .all() or .first() after .filter_by()/.filter()
   • Don't use .all() when you only need one record (use .first() instead)
   • Don't access relationships in loops without eager loading
   • Don't execute queries in templates (query in views/routes)
   • Don't use raw SQL unless absolutely necessary
"""
