import datetime
import json
from pathlib import Path

PROMPTS_PATH = Path("./static/prompts/data.json")
TOTAL_PROMPTS = 365


def _get_day_of_year(date: datetime.date = None) -> int:
    """Returns the day of the year (1–365), clamped for leap years."""
    date = date or datetime.date.today()
    day_of_year = date.timetuple().tm_yday
    return min(day_of_year, 365)


def load_all_prompts():
    """Loads all prompts from the JSON file."""
    if not PROMPTS_PATH.exists():
        raise FileNotFoundError(f"Prompt file not found at {PROMPTS_PATH}")
    with open(PROMPTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_daily_prompt(date: datetime.date = None) -> dict:
    """Returns the prompt for the current day of the year (1–365)."""
    all_prompts = load_all_prompts()
    if len(all_prompts) != TOTAL_PROMPTS:
        raise ValueError(f"Expected {TOTAL_PROMPTS} prompts, but found {len(all_prompts)}")

    # Calculate the day_index by using _get_day_of_year(date) and subtracting 1 (to make it 0-indexed)
    day_index = _get_day_of_year(date) - 1  # 0-indexed
    # Return the prompt at the calculated index from all_prompts
    return all_prompts[day_index]