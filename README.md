# Smart_Task_Analyzer

Smart Task Analyzer is a Django-based application that analyzes a list of tasks and identifies which tasks should be completed first based on urgency, importance, effort, and dependencies. It generates a score for each task and sorts them to help users plan their work intelligently. The UI allows users to paste tasks in JSON format and receive instant task prioritization and suggestions.

## Setup Instructions

1. Download or clone this repository.
2. Open terminal inside the project folder and create a virtual environment:
   python -m venv venv
3. Activate the virtual environment:
   venv\Scripts\activate    (Windows)
   source venv/bin/activate (Mac/Linux)
4. Install project dependencies:
   pip install -r requirements.txt
5. Apply migrations:
   python manage.py migrate
6. Start the Django server:
   python manage.py runserver
7. Open the frontend:
   frontend/index.html
8. Paste JSON input and click Analyze or Suggest Top 3.

## Algorithm Explanation

The Smart Task Analyzer calculates a numerical score for every task and ranks tasks from highest to lowest priority. Higher score means higher priority. The algorithm evaluates four major factors:

Urgency: This has the highest weight. Overdue or near-deadline tasks get a very high score because missing deadlines is the biggest real-world risk.  
Importance: Rated from 1–10 and multiplied by 5. This ensures tasks with high impact are not ignored even if deadlines are not immediate.  
Effort: Tasks estimated under two hours receive bonus points to encourage quick wins and momentum. Extremely long tasks receive a small penalty so they don’t dominate the list.  
Dependencies: Each dependency reduces score slightly. A task blocked by other tasks should not be ranked first.

Conceptual formula:
Priority Score = Urgency Boost + (Importance × 5) + Effort Adjustment – (Dependencies × 5)

This formula reflects real productivity behavior: deadlines first, high-impact tasks next, fast wins prioritized when possible, and blocked tasks deprioritized.

## Design Decisions

• Used JSON input instead of forms to support multiple tasks at once  
• Weighted urgency highest to prevent deadline failures  
• Added quick-win bonus for motivation and psychological momentum  
• Applied dependency penalty to prevent scheduling blocked tasks first

## Time Breakdown

Project Setup – 20 min  
Models and Scoring Algorithm – 150 min  
API Development – 70 min  
Frontend (HTML + CSS + JS) – 90 min  
Debugging and CORS Fixes – 60 min  
Documentation – 20 min  
Total Time: ~7 hours

## Bonus Challenges

The following optional extensions were suggested in the assignment. If completed, they allow additional depth and creativity:

• Dependency Graph Visualization: Detect and visually flag circular dependencies (30–45 min)  
• Date Intelligence: Consider weekends/holidays when calculating urgency (30 min)  
• Eisenhower Matrix View: Display tasks on a 2D grid (Urgent vs Important) (45 min)  
• Learning System: Allow users to mark if suggested tasks were helpful and adjust the algorithm (1 hour)  
• Unit Tests: Write comprehensive tests for your scoring algorithm (45 min)

(For this submission, the core assignment was fully completed. Bonus challenges were not implemented due to time constraints, but would be exciting improvements for future development.)

## Future Improvements

• Add user login and persistent task storage  
• Track task completion history and streaks  
• Export prioritized tasks to PDF/Excel  
• Add timeline / calendar / Gantt view  
• Use machine learning to learn user preference and automatically adjust scoring
