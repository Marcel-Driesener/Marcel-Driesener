import datetime

# YYYY,MM,DD
start_date = datetime.datetime(2003,4,13)
coding_start_date = datetime.datetime(2023, 8, 1)

# calculate exact date
def calculate_delta(start):
    now = datetime.datetime.now()
    delta = now - start
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    return years, months, days

# handle day - days
def pluralize(value, word):
    return f"{value} {word}{'' if value == 1 else 's'}"

# runtime
years, months, days = calculate_delta(start_date)

# coding Since
codingyears, codingmonths, codingdays = calculate_delta(coding_start_date)

# fill Markdown
markdown = f"""
### Marcel Driesener

---

<br>
<br>
<p align="right">gif from: Love, Chunibyo & Other Delusions</p>
<img align="right" height="300" src="assets/Rikka.gif" alt="Rikka Takanashi 'dance'" />

|                       |                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------- |
| OS                    | Windows, Linux, Android                                                                              |
| Runtime               | {pluralize(years, 'year')}, {pluralize(months, 'month')}, {pluralize(days, 'day')}                   |
| Coding Since          | {pluralize(codingyears, 'year')}, {pluralize(codingmonths, 'month')}, {pluralize(codingdays, 'day')} |
| Hobbies               | BMX, Building Keyboards, Gaming                                                                      |
| Fun Fact              | I have 4 Self build Keyboards from SplitKB.com                                                       |
| Fun Fact              | My Favorite from them is the Aurora Sweep                                                            |
| ‎                     | ‎                                                                                                    |
| Frameworks & tools    | React, Vite, Node.js                                                                                 |
| languages.programming | JavaScript, TypeScript, Python, Terraform                                                            |
| languages.real        | German, English                                                                                      |

"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown)
