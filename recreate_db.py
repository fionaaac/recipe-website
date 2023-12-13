from recipemain import db, model

def clear_tables():
    # Clear data from each table
    db.session.query(model.Recipe).delete()
    db.session.query(model.User).delete()
    # Add more delete statements for other models

    # Commit the changes
    db.session.commit()

if __name__ == "__main__":
    clear_tables()