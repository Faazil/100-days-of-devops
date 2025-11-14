#!/usr/bin/env python3
"""
Progress Tracker for 100 Days of DevOps
Track your learning progress through the KodeKloud DevOps challenges
"""

import json
import os
from pathlib import Path
from datetime import datetime
import argparse

# Get the root directory
ROOT_DIR = Path(__file__).parent.parent
PROGRESS_FILE = ROOT_DIR / ".progress.json"
TASKS_FILE = ROOT_DIR / "tools" / "tasks.json"


def init_progress():
    """Initialize progress tracking file"""
    if not PROGRESS_FILE.exists():
        progress = {
            "started_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "completed_days": [],
            "total_days": 100,
            "notes": {}
        }
        save_progress(progress)
        return progress
    return load_progress()


def load_progress():
    """Load progress from file"""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return init_progress()


def save_progress(progress):
    """Save progress to file"""
    progress["last_updated"] = datetime.now().isoformat()
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)


def load_tasks():
    """Load task information"""
    if TASKS_FILE.exists():
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []


def mark_complete(day_number):
    """Mark a day as complete"""
    progress = load_progress()
    day_number = int(day_number)

    if day_number < 1 or day_number > 100:
        print(f"❌ Invalid day number. Must be between 1 and 100.")
        return

    if day_number not in progress["completed_days"]:
        progress["completed_days"].append(day_number)
        progress["completed_days"].sort()
        save_progress(progress)
        print(f"✅ Day {day_number} marked as complete!")
        show_stats()
    else:
        print(f"ℹ️  Day {day_number} was already marked as complete.")


def mark_incomplete(day_number):
    """Mark a day as incomplete"""
    progress = load_progress()
    day_number = int(day_number)

    if day_number in progress["completed_days"]:
        progress["completed_days"].remove(day_number)
        save_progress(progress)
        print(f"↩️  Day {day_number} marked as incomplete.")
    else:
        print(f"ℹ️  Day {day_number} was not marked as complete.")


def show_progress():
    """Display current progress"""
    progress = load_progress()
    tasks = load_tasks()

    completed = len(progress["completed_days"])
    total = progress["total_days"]
    percentage = (completed / total) * 100

    print("\n" + "="*60)
    print("📊 100 DAYS OF DEVOPS - PROGRESS TRACKER")
    print("="*60)

    # Progress bar
    bar_length = 40
    filled = int(bar_length * completed / total)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n{bar} {percentage:.1f}%")
    print(f"Completed: {completed}/{total} challenges\n")

    # Category breakdown
    if tasks:
        categories = {}
        for task in tasks:
            cat = task.get('category', 'Unknown')
            if cat not in categories:
                categories[cat] = {"total": 0, "completed": 0}
            categories[cat]["total"] += 1
            if task['day'] in progress["completed_days"]:
                categories[cat]["completed"] += 1

        print("📚 Progress by Category:")
        print("-" * 60)
        for cat, stats in sorted(categories.items()):
            cat_pct = (stats["completed"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            cat_bar_length = 20
            cat_filled = int(cat_bar_length * stats["completed"] / stats["total"]) if stats["total"] > 0 else 0
            cat_bar = "▓" * cat_filled + "░" * (cat_bar_length - cat_filled)
            print(f"{cat:15} {cat_bar} {stats['completed']:2}/{stats['total']:2} ({cat_pct:5.1f}%)")

    print("\n" + "="*60 + "\n")


def show_stats():
    """Show detailed statistics"""
    progress = load_progress()
    completed = len(progress["completed_days"])
    total = progress["total_days"]
    percentage = (completed / total) * 100

    print(f"\n📈 Statistics:")
    print(f"   Completed: {completed}/{total} ({percentage:.1f}%)")
    print(f"   Remaining: {total - completed}")

    if completed > 0:
        start_date = datetime.fromisoformat(progress["started_at"])
        days_elapsed = (datetime.now() - start_date).days
        if days_elapsed > 0:
            pace = completed / days_elapsed
            estimated_days = (total - completed) / pace if pace > 0 else 0
            print(f"   Current pace: {pace:.2f} challenges/day")
            print(f"   Estimated completion: {estimated_days:.0f} days")


def list_completed():
    """List all completed days"""
    progress = load_progress()
    tasks = load_tasks()

    if not progress["completed_days"]:
        print("No challenges completed yet. Start with Day 1!")
        return

    print("\n✅ Completed Challenges:")
    print("-" * 60)

    task_dict = {task['day']: task for task in tasks}

    for day in progress["completed_days"]:
        if day in task_dict:
            task = task_dict[day]
            print(f"Day {day:3}: {task['title'][:50]}")
        else:
            print(f"Day {day:3}: Unknown")


def list_remaining():
    """List remaining days"""
    progress = load_progress()
    tasks = load_tasks()

    remaining = [task for task in tasks if task['day'] not in progress["completed_days"]]

    if not remaining:
        print("🎉 Congratulations! All challenges completed!")
        return

    print(f"\n📝 Remaining Challenges ({len(remaining)}):")
    print("-" * 60)

    for task in remaining[:10]:  # Show first 10
        print(f"Day {task['day']:3}: {task['title'][:50]} [{task['category']}]")

    if len(remaining) > 10:
        print(f"... and {len(remaining) - 10} more")


def reset_progress():
    """Reset all progress"""
    confirm = input("⚠️  Are you sure you want to reset all progress? (yes/no): ")
    if confirm.lower() == 'yes':
        if PROGRESS_FILE.exists():
            PROGRESS_FILE.unlink()
        init_progress()
        print("✅ Progress reset successfully!")
    else:
        print("❌ Reset cancelled.")


def main():
    parser = argparse.ArgumentParser(
        description='Track your progress through 100 Days of DevOps',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python progress.py --show              Show current progress
  python progress.py --complete 5        Mark day 5 as complete
  python progress.py --incomplete 5      Mark day 5 as incomplete
  python progress.py --stats             Show detailed statistics
  python progress.py --list-completed    List all completed days
  python progress.py --list-remaining    List remaining days
        """
    )

    parser.add_argument('--show', action='store_true', help='Show progress overview')
    parser.add_argument('--complete', type=int, metavar='DAY', help='Mark a day as complete')
    parser.add_argument('--incomplete', type=int, metavar='DAY', help='Mark a day as incomplete')
    parser.add_argument('--stats', action='store_true', help='Show detailed statistics')
    parser.add_argument('--list-completed', action='store_true', help='List completed challenges')
    parser.add_argument('--list-remaining', action='store_true', help='List remaining challenges')
    parser.add_argument('--reset', action='store_true', help='Reset all progress')

    args = parser.parse_args()

    # Initialize progress file if it doesn't exist
    init_progress()

    if args.complete:
        mark_complete(args.complete)
    elif args.incomplete:
        mark_incomplete(args.incomplete)
    elif args.stats:
        show_stats()
    elif args.list_completed:
        list_completed()
    elif args.list_remaining:
        list_remaining()
    elif args.reset:
        reset_progress()
    elif args.show:
        show_progress()
    else:
        # Default: show progress
        show_progress()


if __name__ == "__main__":
    main()
