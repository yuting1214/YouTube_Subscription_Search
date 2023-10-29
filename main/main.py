import click
import subprocess
import os
from db_operations import create_db, update_db

@click.group()
def cli():
    """
    YouTube Subscription Search CLI:
    
    A command-line tool that provides various operations related to 
    the YouTube Subscription Search project. Use the commands below 
    to interact with the project.
    """
    pass

@cli.command()
def createdb():
    """
    Create Database:
    
    This command initializes the database required for the project. 
    It should be executed before any other operations if you're running 
    the project for the first time or if you want to reset the database.
    """
    create_db.run()

@cli.command()
def updatedb():
    """
    Update Database:
    
    This command updates the database with new data. It's useful to 
    periodically refresh the stored data to keep the application's 
    results up-to-date.
    """
    update_db.run()

@cli.command()
def runapp():
    """
    Run App:
    
    This command launches the Streamlit-based front-end application 
    of the YouTube Subscription Search project. Make sure you have 
    created and/or updated the database before running this command.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    front_end_path = os.path.join(current_dir, "..", "app", "front_end.py")
    subprocess.run(["streamlit", "run", front_end_path])

if __name__ == "__main__":
    cli()
