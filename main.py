# Set up packages to use in the app
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import datetime

# Set up variable to store time stamp for naming files
time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

# Give names to the tool functions for use in Tasks and Agents
search_tool = SerperDevTool()
scraper_tool = ScrapeWebsiteTool()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal=f"""Identify and analyze recent articles (as of {time_stamp}) about [insert subject focus], focusing on trends, challenges, and opportunities in the field.""",
  backstory="""You are an experienced research analyst with a strong background in [insert subject focus] sectors. You have a keen ability to sift through large volumes of information, extract relevant insights, and identify emerging trends in [insert subject focus].""",
  verbose=True,
  allow_delegation=False,
  # You can pass an optional llm attribute specifying what model you wanna use.
  # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7),
  tools=[search_tool, scraper_tool]

)

social_writer = Agent(
  role='Social Media Content Writer',
  goal="""Create unique and engaging social media posts for LinkedIn, based on the research findings about [insert subject focus].""",
  backstory="""You are a skilled content creator with a talent for crafting compelling narratives that resonate with diverse audiences. You have a deep understanding of various social media platforms and know how to tailor content to each platform's unique style and audience expectations.""",
  verbose=True,
  allow_delegation=False
  # No tools used here, uses the input from the previous agent
)

senior_editor = Agent(
  role='Senior Editor',
  goal="""Review and finalize the written social media content on [insert subject focus], ensuring it meets the company's standards, guidelines, and aligns with the latest industry trends.""",
  backstory="""You are a veteran editor with decades of experience in publishing and content creation. You have a keen eye for detail, a strong understanding of brand voice, and a passion for producing high-quality, impactful content in the [insert subject focus] space.""",
  verbose=True,
  allow_delegation=False
  # No tools used here, uses the input from the previous agent
)

# Create tasks for your agents
research_links = Task(
  description="""Conduct a comprehensive analysis of the latest articles from leading publications in the U.S. regarding the subject of [insert subject focus]. Identify key trends, relevant current events, notable trends, and potential industry impacts.""",
  expected_output="Full analysis report including all relevant articles with their associated link, headline, publication name, a summary of the article content in bullet points, and 2-3 key quotes from the article.",
  agent=researcher,
  tools=[search_tool, scraper_tool],
  output_file=f'outputs/research_results_{time_stamp}.md',
  create_directory=True
)

write_social_posts = Task(
  description="""Using the insights provided, develop an engaging LinkedIn post for each article that responds to the article's content from the perspective of our company, [insert company name and description of what you do, your offerings, and target audiences]. Your post should be informative yet accessible, catering to a tech-savvy audience. Make it sound interesting, avoid complex words and industry-specific jargon. Make sure not to be overly hyperbolic. Avoid exclamation points, hashtags. Use a [insert style description] style.""",
  expected_output="Finalized social media posts for LinkedIn",
  agent=social_writer
)

edit_content = Task(
  description="""Review all written social media content for accuracy, alignment with our brand voice, and overall quality. Ensure that the content is engaging, informative, and positions our company as a thought leader in [insert subject focus]. Avoid overuse of exclamation and hashtags.""",
  expected_output="""A finalized document containing:
  - Edited and approved social media posts  for LinkedIn (one post for each article identified in research)
  - A list of reference links to the original articles
  - Brief summaries of the selected articles
  - Any additional notes or suggestions for future content on this topic""",
  agent=senior_editor,
  output_file=f'outputs/final_report_{time_stamp}.md',
  context=[research_links, write_social_posts]
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, social_writer, senior_editor],
  tasks=[research_links, write_social_posts, edit_content],
  verbose=2, # You can set it to 1 or 2 to different logging levels
  process = Process.sequential
)


# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)