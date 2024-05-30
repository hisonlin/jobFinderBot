from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

# Scrape jobs from Indeed
def scrape_indeed(query, location):
    options = Options()
    options.headless = True  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    url = f"https://ca.indeed.com/jobs?q={query}&l={location}&radius=50&fromage=1"
    driver.get(url)
    
    jobs = []
    cards = driver.find_elements(By.CLASS_NAME, 'result')
    for card in cards:
        title_element = card.find_element(By.CLASS_NAME, 'jobTitle')
        title = title_element.text.strip()
        
        company_element = card.find_element(By.CLASS_NAME, 'company_location')
        company = company_element.text.strip()

        summary_element = card.find_element(By.CLASS_NAME, 'heading6')
        summary = summary_element.text.strip()
        
        link_element = title_element.find_element(By.TAG_NAME, 'a')
        link = link_element.get_attribute('href')
        
        jobs.append({'title': title, 'company': company, 'summary': summary, 'link': link})
    
    
    return jobs

# Discord bot setup
# Load environment variables from .env file
load_dotenv()

# Get environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print("Starting job scraping...")
    main.start()  # Start the task loop

@tasks.loop(hours=24)  # Run the job search every 24 hours
async def main():
    webDev = scrape_indeed('web+developer', 'vancouver')
    fullStack = scrape_indeed('full+stack+developer', 'vancouver')

    print(f"Found {len(webDev)} webDev jobs")
    print(f"Found {len(fullStack)} fullStack jobs")

    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print(f"Channel with ID {CHANNEL_ID} not found")
        print("Available channels:")
        for guild in bot.guilds:
            for ch in guild.text_channels:
                print(f"{ch.name}: {ch.id}")
        return

    await channel.send("WebDev jobs listed last 24hrs:")
    for job in webDev:
        await channel.send(f"**{job['title']}**\n**{job['company']}**\n**{job['summary']}**\n[Apply here]({job['link']})\n")
        await channel.send("="*20)

    await channel.send("FullStack jobs listed last 24hrs:")
    for job in fullStack:
        await channel.send(f"**{job['title']}**\n**{job['company']}**\n**{job['summary']}**\n[Apply here]({job['link']})\n")
        await channel.send("="*20)

# Run the bot
bot.run(TOKEN)
