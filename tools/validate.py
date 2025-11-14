#!/usr/bin/env python3
"""
Validator for 100 Days of DevOps
Simple validation helper for checking solutions
"""

import argparse
import subprocess
import sys
from pathlib import Path


def check_file_exists(filepath):
    """Check if a file exists"""
    return Path(filepath).exists()


def run_command(command, shell=True):
    """Run a command and return the result"""
    try:
        result = subprocess.run(
            command,
            shell=shell,
            capture_output=True,
            text=True,
            timeout=30
        )
        return {
            'success': result.returncode == 0,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'Command timed out'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def validate_day(day_number):
    """Validate a specific day's challenge"""
    print(f"\n🔍 Validating Day {day_number}...")
    print("-" * 60)

    # Basic validation - check if the challenge file exists
    week_number = ((day_number - 1) // 7) + 1
    root_dir = Path(__file__).parent.parent
    challenge_file = root_dir / "challenges" / f"week-{week_number:02d}" / f"day-{day_number:02d}.md"

    if not challenge_file.exists():
        print(f"❌ Challenge file not found: {challenge_file}")
        return False

    print(f"✅ Challenge file exists: {challenge_file.name}")

    # Additional validation can be added here based on day-specific requirements
    print("\nℹ️  For detailed validation, please:")
    print("   1. Review the challenge requirements")
    print("   2. Run the verification commands from the challenge")
    print("   3. Test your solution manually")

    return True


def check_environment():
    """Check if the environment is properly set up"""
    print("\n🔍 ENVIRONMENT CHECK")
    print("="*60)

    checks = []

    # Check if we're in the right directory
    root_dir = Path(__file__).parent.parent
    if (root_dir / "challenges").exists():
        print("✅ Repository structure is correct")
        checks.append(True)
    else:
        print("❌ Repository structure is incorrect")
        checks.append(False)

    # Check for progress tracker
    if (root_dir / "tools" / "progress.py").exists():
        print("✅ Progress tracker is available")
        checks.append(True)
    else:
        print("❌ Progress tracker is missing")
        checks.append(False)

    # Check for tasks data
    if (root_dir / "tools" / "tasks.json").exists():
        print("✅ Tasks data is available")
        checks.append(True)
    else:
        print("❌ Tasks data is missing")
        checks.append(False)

    print("="*60)

    if all(checks):
        print("\n✅ Environment is properly configured!")
        return True
    else:
        print("\n⚠️  Some components are missing. Run setup.py --init")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Validate your 100 Days of DevOps solutions',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate.py --day 5           Validate day 5 solution
  python validate.py --env             Check environment setup
        """
    )

    parser.add_argument('--day', type=int, metavar='DAY', help='Validate a specific day')
    parser.add_argument('--env', action='store_true', help='Check environment setup')

    args = parser.parse_args()

    if args.day:
        if args.day < 1 or args.day > 100:
            print("❌ Invalid day number. Must be between 1 and 100.")
            sys.exit(1)
        validate_day(args.day)
    elif args.env:
        check_environment()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
