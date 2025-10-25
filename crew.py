from crewai import Crew,Process
from tasks import research_task,write_task, fact_task
from agents import news_researcher,news_writer, fact_checker

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer, fact_checker],
    tasks=[research_task,write_task, fact_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Synthetic data generation'})
print(result)