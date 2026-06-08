from crewai import Crew, Process, Task
from agents import *
from analyzer import analyze_code

def run_crew(code):

    analysis = analyze_code(code)

    analysis_task = Task(
        description=f"Analyze code: {analysis}",
        agent=code_agent,
        expected_output="structured analysis"
    )

    test_task = Task(
        description=f"Generate test cases for code:\n{code}",
        agent=test_agent,
        expected_output="list of test cases"
    )

    security_task = Task(
        description=f"Find vulnerabilities in:\n{code}",
        agent=security_agent,
        expected_output="security report"
    )

    unit_task = Task(
        description="Generate pytest code from test cases",
        agent=unit_test_agent,
        expected_output="pytest code"
    )

    crew = Crew(
        agents=[code_agent, test_agent, security_agent, unit_test_agent],
        tasks=[analysis_task, test_task, security_task, unit_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()
