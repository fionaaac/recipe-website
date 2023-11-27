from recipemain import db

def clear_tables():
    # Clear data from each table
    db.session.query(Recipe).delete()
    db.session.query(User).delete()
    # Add more delete statements for other models

    # Commit the changes
    db.session.commit()

if __name__ == "__main__":
    clear_tables()