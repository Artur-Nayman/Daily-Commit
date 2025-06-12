from datetime import datetime

with open("log.txt", "a") as file:
    file.write(f"Daily commit: {datetime.now()}\n")

START_DATE = datetime(2025, 6, 1)

def update_readme_counter():
    today = datetime.now()
    days_passed = (today - START_DATE).days

    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    start_tag = '<!-- START_COUNTER -->'
    end_tag = '<!-- END_COUNTER -->'

    before = content.split(start_tag)[0]
    after = content.split(end_tag)[1]

    new_content = f"{before}{start_tag}\n**{days_passed}** days\n{end_tag}{after}"

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme_counter()
