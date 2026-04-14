"""
Lecture 4 — Sorting Hat Demo
A participatory nested if/elif/else demo.

Ask a student for their name and answers to two yes/no questions,
then the Sorting Hat assigns them a house.

Points to remember:
  - Each condition is a boolean expression
  - Only ONE branch executes — trace through the logic live
  - The 'and' operator: both must be True
  - Chained elif vs nested if: what's the difference?
"""


def sort_student(name: str, adventurous: bool, competitive: bool) -> str:
    """Return the Hogwarts house for a student based on two traits."""
    if adventurous and competitive:
        house = "Slytherin"           # daring AND driven to win
        trait = "ambitious daring"
    elif adventurous:
        house = "Gryffindor"          # bold but motivated by courage, not competition
        trait = "bold courage"
    elif competitive:
        house = "Ravenclaw"           # driven and methodical, not reckless
        trait = "sharp ambition"
    else:
        house = "Hufflepuff"          # steady, collaborative, loyal
        trait = "steadfast loyalty"

    return (
        f"\n  *  {name}, the Sorting Hat sees... {trait}.\n"
        f"     --> HOUSE {house.upper()} <--\n"
    )


def ask_yes_no(question: str) -> bool:
    """Prompt until the user types 'yes' or 'no'. Returns a bool."""
    while True:
        answer = input(f"  {question} (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("  Please type 'yes' or 'no'.")


def main():
    print("=" * 52)
    print("     THE SORTING HAT — Lecture 4 Demo")
    print("=" * 52)
    print()

    name = input("  Enter a student's name: ").strip() or "Mystery Student"
    print()

    adventurous = ask_yes_no(f"Is {name} adventurous / likes trying new things?")
    competitive = ask_yes_no(f"Is {name} competitive / driven to excel?")

    # Show the boolean values before branching — make it visible
    print()
    print(f"  adventurous = {adventurous}")
    print(f"  competitive = {competitive}")

    result = sort_student(name, adventurous, competitive)
    print(result)

    # Discussion prompt
    print("-" * 52)
    print("  Which branch ran? Trace it together:")
    print(f"    adventurous and competitive  -> {adventurous and competitive}")
    print(f"    adventurous                  -> {adventurous}")
    print(f"    competitive                  -> {competitive}")
    print()
    print("  Try another student? Re-run the script.")
    print("=" * 52)


if __name__ == "__main__":
    main()
