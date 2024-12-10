import random

# Question data (store in a file or database in a real app)
questions = [
    {
        "question": "What is phishing?",
        "options": ["A type of social engineering attack", "A virus that infects your computer", "A type of malware",
                    "A security breach"],
        "answer": "A type of social engineering attack",
        "tips": "Phishing emails or websites often look legitimate to trick you into giving away your personal information, such as passwords or credit card numbers."
    },
    {
        "question": "Which of these is a strong password?",
        "options": ["password123", "rEaDyPa$$wOrd", "MyDogIsFluffy123", "r@nd0mP@$$wOrd"],
        "answer": "r@nd0mP@$$wOrd",
        "tips": "Strong passwords use a combination of uppercase and lowercase letters, numbers, and symbols."
    },
    {
        "question": "What does HTTPS mean?",
        "options": ["Hyper Text Transfer Secure Protocol", "Hyper Text Transfer Secure Packet",
                    "Hyper Transfer Secure Protocol", "Hyper Transmission Secure Protocol"],
        "answer": "Hyper Text Transfer Secure Protocol",
        "tips": "HTTPS indicates that a website uses encryption to protect your data during transmission. Look for the padlock icon in your browser's address bar."
    },

    # Add more questions here...
]


def ask_question(question_data):
    question = question_data["question"]
    options = question_data["options"]
    answer = question_data["answer"]
    tips = question_data["tips"]

    print(question)
    for i, option in enumerate(options):
        print(f"{chr(ord('A') + i)}. {option}")

    while True:
        try:
            user_answer = input("Enter your answer (A-D): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        except EOFError:
            print("Exiting quiz.")
            return None

    if user_answer == get_letter_of_answer(answer, options):  # Corrected here
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {get_letter_of_answer(answer, options)} - {answer}")
    print(tips)
    print("-" * 20)  # Separator
    return user_answer == get_letter_of_answer(answer, options)


def get_letter_of_answer(answer, options):
    return chr(ord('A') + options.index(answer))


def run_quiz():
    random.shuffle(questions)  # Shuffle questions for randomness
    score = 0
    total_questions = len(questions)
    for question in questions:
        if ask_question(question):
            score += 1
    print(f"\nQuiz finished. Your score is {score} out of {total_questions}.")


if __name__ == "__main__":
    run_quiz()