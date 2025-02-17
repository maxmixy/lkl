from my_flask_app import create_app, db
from sqlalchemy import inspect

app = create_app()
with app.app_context():
    # Create tables in correct order
    try:
        # Create Invoice table first
        with db.engine.connect() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS invoice (

                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                invoice_no VARCHAR(50) UNIQUE NOT NULL,
                date DATETIME NOT NULL,
                invoice_type VARCHAR(50),
                project_id VARCHAR(50),
                customer VARCHAR(100),
                acct_manager VARCHAR(100),
                lead_division VARCHAR(100),
                remarks TEXT,
                internal_terms VARCHAR(50),
                customer_terms VARCHAR(50),
                payment_type VARCHAR(50),
                tpc_contact VARCHAR(100),
                tpc_gross FLOAT,
                gross FLOAT,
                debit FLOAT,
                returns FLOAT,
                credit FLOAT,
                payment FLOAT,
                balance FLOAT
            )
        """)
        
        # Create Service table with foreign key
        with db.engine.connect() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS service (

                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                service_id VARCHAR(50) NOT NULL,
                description TEXT,
                accepted BOOL DEFAULT FALSE,
                gross FLOAT,
                billed FLOAT,
                amount FLOAT,
                invoice_id INTEGER,
                FOREIGN KEY (invoice_id) REFERENCES invoice(id) ON DELETE CASCADE
            )
        """)
        
        # Verify tables exist
        inspector = inspect(db.engine)
        if 'invoice' in inspector.get_table_names() and 'service' in inspector.get_table_names():
            print("Database tables created successfully")
        else:
            print("Error: Failed to create all tables")
            
    except Exception as e:
        print(f"Error creating tables: {str(e)}")
