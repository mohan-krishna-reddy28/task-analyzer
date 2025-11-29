from datetime import date, datetime

def calculate_task_score(task_data):
    """
    Calculates a priority score.
    Higher score = Higher priority.
    """

    score = 0
    today = date.today()

    # Convert string due_date to date
    if isinstance(task_data["due_date"], str):
        task_data["due_date"] = datetime.strptime(task_data["due_date"], "%Y-%m-%d").date()

    # 1. Urgency
    days_until_due = (task_data["due_date"] - today).days
    if days_until_due < 0:
        score += 100  # Overdue
    elif days_until_due <= 3:
        score += 50   # Due soon
    elif days_until_due <= 7:
        score += 30
    else:
        score += 10

    # 2. Importance
    score += task_data["importance"] * 5

    # 3. Effort
    if task_data["estimated_hours"] < 2:
        score += 10
    elif task_data["estimated_hours"] > 6:
        score -= 5

    # 4. Dependencies
    if len(task_data["dependencies"]) > 0:
        score -= len(task_data["dependencies"]) * 5

    return score
