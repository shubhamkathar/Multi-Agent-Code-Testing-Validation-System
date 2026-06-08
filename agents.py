from crewai import Agent
from config import llm

code_agent = Agent(
    role="Code Analyzer",
    goal="Analyze Python code structure",
    backstory="Expert in AST and code parsing",
    llm=llm,
    verbose=True
)

test_agent = Agent(
    role="Test Designer",
    goal="Generate edge-case test scenarios",
    backstory="Senior QA engineer",
    llm=llm,
    verbose=True
)

security_agent = Agent(
    role="Security Reviewer",
    goal="Find vulnerabilities in code",
    backstory="Cybersecurity expert",
    llm=llm,
    verbose=True
)

unit_test_agent = Agent(
    role="Pytest Engineer",
    goal="Generate executable pytest code",
    backstory="Python testing expert",
    llm=llm,
    verbose=True
)

feedback_agent = Agent(
    role="Debugging Agent",
    goal="Fix failing tests using logs",
    backstory="Expert debugger",
    llm=llm,
    verbose=True
)
