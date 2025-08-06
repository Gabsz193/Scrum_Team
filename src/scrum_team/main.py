#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from scrum_team.crew import ScrumTeamCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be scrum_team way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'project_name': 'Customer Management System',
        'requirements': '''
            1. User authentication system with roles (admin, manager, customer)
            2. Customer profile management with contact information
            3. Order tracking functionality
            4. Reporting dashboard with sales analytics
            5. Integration with payment gateway
            6. Email notification system
            7. Mobile-responsive design
        ''',
        'current_year': str(datetime.now().year)
    }
    
    try:
        ScrumTeamCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for scrum_team given number of iterations.
    """
    inputs = {
        'project_name': 'Customer Management System',
        'requirements': '''
            1. User authentication system with roles (admin, manager, customer)
            2. Customer profile management with contact information
            3. Order tracking functionality
            4. Reporting dashboard with sales analytics
            5. Integration with payment gateway
            6. Email notification system
            7. Mobile-responsive design
        ''',
        'current_year': str(datetime.now().year)
    }
    try:
        ScrumTeamCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from scrum_team specific task.
    """
    try:
        ScrumTeamCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'project_name': 'Customer Management System',
        'requirements': '''
            1. User authentication system with roles (admin, manager, customer)
            2. Customer profile management with contact information
            3. Order tracking functionality
            4. Reporting dashboard with sales analytics
            5. Integration with payment gateway
            6. Email notification system
            7. Mobile-responsive design
        ''',
        'current_year': str(datetime.now().year)
    }
    
    try:
        ScrumTeamCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
