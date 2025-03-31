import os
import re

# Define the VALARM block you want to insert
valarm_block = """BEGIN:VALARM
TRIGGER:-PT15M
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM

BEGIN:VALARM
TRIGGER:-PT1H
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM
"""

# Function to add VALARM to each VEVENT if not already present
def add_valarm_to_ics(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by VEVENTs
    events = re.split(r'(BEGIN:VEVENT.*?END:VEVENT)', content, flags=re.DOTALL)
    modified = False

    for i in range(len(events)):
        if events[i].startswith("BEGIN:VEVENT"):
            if "BEGIN:VALARM" not in events[i]:
                # Insert VALARM before END:VEVENT
                events[i] = re.sub(r'END:VEVENT', valarm_block + '\nEND:VEVENT', events[i])
                modified = True

    if modified:
        new_content = ''.join(events)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")
    else:
        print(f"No change: {file_path}")

# Directory to scan
directory = directory = r"~/dir"  # Change to your directory path

for filename in os.listdir(directory):
    if filename.endswith(".ics"):
        add_valarm_to_ics(os.path.join(directory, filename))
