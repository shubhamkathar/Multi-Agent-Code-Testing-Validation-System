from crewai import LLM

llm = LLM(
    model="deepseek-ai/deepseek-r1",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_API_KEY"
)
