# q3.py
# This file simulates a simple task processing system.
# - process_tasks() moves tasks from pending -> completed
# - show_completed() displays all completed tasks
#
# Note:
# * We RETURN lists when we want reusable values.
# * We PRINT inside loops here to give the user feedback.

def process_tasks(pending, completed):
    """
    Move tasks from pending to completed.
    Mutates both lists in-place.
    """
    while pending:  # continue until pending is empty
        current_task = pending.pop(0)  # take first task
        print(f"Processing: {current_task}")
        completed.append(current_task)

def show_completed(completed):
    """
    Print all completed tasks.
    """
    print("\nCompleted tasks:")
    for task in completed:
        print(f"- {task}")


if __name__ == "__main__":
    # --- Demo 1: normal processing (mutates original lists) ---
    tasks = ["write report", "fix bug", "study python", "walk the dog"]
    done = []

    print("=== Demo 1: Processing tasks normally ===")
    process_tasks(tasks, done)
    show_completed(done)

    # --- Demo 2: preserve original pending list using a copy ---
    tasks2 = ["cook dinner", "read book", "call mom", "exercise"]
    done2 = []

    print("\n=== Demo 2: Preserving original pending list ===")
    process_tasks(tasks2[:], done2)  # pass a copy of pending
    show_completed(done2)

    # Prove that original tasks2 is unchanged
    print("\nOriginal pending list is still intact:", tasks2)
    print("Completed list contains:", done2)
