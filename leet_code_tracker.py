import requests
import json
import datetime
import os

# Function to fetch a random LeetCode problem
def get_random_problem():
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    data = response.json()
    questions = data["stat_status_pairs"]
    
    # Pick a random problem
    problem = questions[datetime.datetime.now().day % len(questions)]
    title = problem["stat"]["question__title"]
    slug = problem["stat"]["question__title_slug"]
    difficulty = ["Easy", "Medium", "Hard"][problem["difficulty"]["level"] - 1]
    link = f"https://leetcode.com/problems/{slug}/"

    return title, difficulty, link

# Create or update a Markdown log file
def update_log():
    title, difficulty, link = get_random_problem()
    
    log_file = "daily_log.md"
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    log_entry = f"### {today}\n- **Problem**: [{title}]({link})\n- **Difficulty**: {difficulty}\n- **Solution**: _Pending_\n\n"
    
    if os.path.exists(log_file):
        with open(log_file, "a") as f:
            f.write(log_entry)
    else:
        with open(log_file, "w") as f:
            f.write("# Daily LeetCode Challenge Log\n\n" + log_entry)
    
    print(f"Logged: {title} ({difficulty})")

# Run the script
if __name__ == "__main__":
    update_log()
