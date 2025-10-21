# insert_VALARM

Automatically add calendar reminders (VALARM blocks) to your iCalendar `.ics` files. This script scans a directory of `.ics` files and injects a standard alarm into every event, so you never miss an appointment.

## Features

- **Batch Processing:** Process one or multiple `.ics` files in a specified directory.
- **Standard Reminder:** Inserts a VALARM block that triggers a notification before each event (default is 30 minutes before start).
- **Customizable Directory:** Change the `directory` variable to point to the folder containing your `.ics` files.
- **Cross‑platform:** Written in pure Python with no external dependencies; tested on macOS but should work on any system with Python installed.

## Requirements

- Python 3 (tested with Python 3.10)
- `.ics` files exported from your calendar application.

## Usage

1. Clone this repository or download `insert_VALARM.py`.
2. Open the script in a text editor and modify the `directory` variable to point to the folder containing your `.ics` files.
3. Optionally, adjust the `valarm_block` variable to change the reminder trigger time or description. The default alarm looks like:
   ```
   BEGIN:VALARM
   ACTION:DISPLAY
   DESCRIPTION:Reminder
   TRIGGER:-PT30M
   END:VALARM
   ```
4. Run the script from your terminal:
   ```bash
   python3 insert_VALARM.py
   ```
   Each `.ics` file in the directory will be updated in place with a VALARM block added to every event.

## How It Works

The script iterates over every `.ics` file in the specified directory, reads each line, and injects the `VALARM` block immediately after each `END:VEVENT` line. The original event data is preserved; the alarm simply adds a pop‑up notification.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
