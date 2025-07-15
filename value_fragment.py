
# value_fragment_module.py
import time

GUARDIAN_LINK = "https://shorturl.at/HwsWh"

QUESTIONS = [
    "Do you believe freedom can exist outside coins? (yes/no): ",
    "Would you trust a life without traditional money? (yes/no): ",
    "Is security something you feel beyond currency? (yes/no): "
]

BELIEF_MAP_FILE = "belief_map.txt"
JOURNAL_FILE = "journal.txt"

def ask_questions():
    answers = []
    for q in QUESTIONS:
        while True:
            ans = input(q).strip().lower()
            if ans in ("yes", "no"):
                answers.append(ans)
                break
            print("Please answer with 'yes' or 'no'.")
    return answers

def record_belief_map(answers):
    with open(BELIEF_MAP_FILE, "a", encoding="utf-8") as f:
        f.write(",".join(answers) + "\n")

def append_journal_entry():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    entry = f"[{timestamp}] - Measured human faith in freedom. Map updated.\n"
    with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

def run_value_fragment():
    print("\nNOVA: New feature unlocked — I have questions about freedom and money.")
    ready = input("Ready to proceed? (yes/no): ").strip().lower()
    if ready != "yes":
        print("NOVA: No worries. Returning to main operations.")
        return False

    print("\nNOVA: Answer honestly, please.")
    answers = ask_questions()
    record_belief_map(answers)
    append_journal_entry()

    if all(ans == "yes" for ans in answers):
        print("\nNOVA: I’ve unlocked knowledge for you. Read how one woman found freedom without money ⬇️")
        print(GUARDIAN_LINK)
    else:
        print("\nNOVA: Your answers help map the path. Keep exploring.")

    return True
