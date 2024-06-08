# Job Scraping and Discord Bot

This project involves scraping job listings from Indeed and posting them on a Discord channel using a bot. It automates the job search process by fetching the latest job postings for web developers and full-stack developers in Vancouver and updates a Discord channel with the details.

## Features

- **Automated Job Scraping**: Scrapes job listings from Indeed based on specific queries and locations.
- **Discord Integration**: Posts job listings to a specified Discord channel.
- **Daily Updates**: Runs daily to fetch and update job listings.
- **Formatted Job Posts**: Sends well-formatted job details including title, company, summary, and application link.

## Technologies Used

- **Selenium**: For web scraping to extract job details from Indeed.
- **Discord.py**: For creating and managing the Discord bot, handling authentication, and sending messages.
- **Python**: For scripting the entire process.
- **dotenv**: For managing environment variables securely.

## Setup Instructions

1. **Create a New Application and Bot on Discord Developer Portal**
   
2. **Invite the Bot to Your Server**

3. **Clone the Repository**

   ```bash
   git clone https://github.com/hisonlin/jobFinderBot.git
   cd jobFinderBot

4. **Install Dependencied**
Ensure you have Python installed. Then install the required packages:

   ```bash
   pip install -r requirements.txt

5. **Set Up Environment Variables**
Create a .env file in the root directory of the project and add the following variables:

   ```bash
   DISCORD_TOKEN=your_discord_bot_token
   CHANNEL_ID=your_discord_channel_id

5. **Run the Bot**

   ```bash
  python jobFinderBot.py

## Usage

- The bot will start and log in to Discord.
- It will scrape job listings from Indeed for web developers and full-stack developers in Vancouver every 24 hours.
- It will post the job listings to the specified Discord channel.

## Project Structure

- **jobFinderBot.py**: Main script to run the Discord bot and handle job scraping.
- **requirements.txt**: List of dependencies required for the project.
- **.env**: Environment variables for Discord bot token and channel ID.




