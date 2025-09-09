"""Q3 — List Processing (mutation vs copies + while loop)

Functions:
- process_tasks(pending, completed): move tasks from pending -> completed using a while loop,
  printing 'Processing: <task>' for each item. MUTATES both lists.
- show_completed(completed): print each completed task on its own line.

Demo:
1) Process a sample list of 4+ tasks and show the completed list.
2) Process using a COPY of the pending list (pending[:] ) to prove the original pending stays unchanged.
"""

from typing import List

def process_tasks(pending: List[str], completed: List[str]) -> None:
    """
    Mutate both lists by moving items from pending to completed,
    printing a progress line for each item.
    """
    # We'll pop from the front to preserve the original order of tasks.
    while pending:
        current = pending.pop(0)
        print(f"Processing: {current}")
        completed.append(current)


def show_completed(completed: List[str]) -> None:
    """Print all completed tasks, one per line."""
    for task in completed:
        print(task)


if __name__ == "__main__":
    # --- Demo 1: normal mutation ---
    pending = ["set up repo", "write Q1", "write Q2", "review code"]
    completed = []
    process_tasks(pending, completed)
    print("\nCompleted tasks:")
    show_completed(completed)

    # --- Demo 2: preserve the original pending using a copy (slice) ---
    original_pending = ["draft README", "lint code", "run tests", "submit PR"]
    completed_copy_run = []

    # Pass a COPY of pending so the original remains unchanged
    process_tasks(original_pending[:], completed_copy_run)

    print("\nOriginal pending (should be unchanged):")
    print(original_pending)
    print("Completed from copy-run:")
    print(completed_copy_run)
