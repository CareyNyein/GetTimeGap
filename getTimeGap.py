import re
from datetime import datetime

def parse_srt_file(file_name):
    """Parses the subtitle file and returns a list of start and end times."""
    time_stamps = []
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            if re.match(r"^\d{2}:\d{2}:\d{2},\d{3}", line):
                time_stamps.append(line.strip().split(' --> '))
    return time_stamps

def find_gaps(time_stamps, gap_seconds):
    """Finds gaps in subtitles longer than the specified duration."""
    for index, (start, end) in enumerate(time_stamps[:-1]):
        before_end = datetime.strptime(end, '%H:%M:%S,%f')
        after_start = datetime.strptime(time_stamps[index + 1][0], '%H:%M:%S,%f')
        gap = (after_start - before_end).total_seconds()

        if gap >= gap_seconds:
            print(f"The {gap_seconds}-second gap found at line {index + 1}, starts from {end.replace(',', '.')}")

def main():
    """Main function to handle user input and find subtitle gaps."""
    srt_file_name = input("Enter subtitle file name (without extension):\n>>> ")
    total_gap = int(input("Enter total gap you want to find (in seconds):\n>>> "))

    try:
        time_stamps = parse_srt_file(srt_file_name + ".srt")
        find_gaps(time_stamps, total_gap)
    except FileNotFoundError:
        print(f"Error: File '{srt_file_name}.srt' not found. Please check the file name.")
    except Exception as e:
        print(f"An error occurred: {e}")

    input("=== DONE === Press Enter to exit...")

if __name__ == "__main__":
    main()