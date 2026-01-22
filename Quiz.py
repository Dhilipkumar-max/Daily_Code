def run_quiz():
    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which programming language is known as the 'snake' language?",
            "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
            "answer": "C"
        }
    ]

    score = 0

    print("--- Welcome to the Python Quiz! ---")

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Get user input and convert to uppercase
        guess = input("Your answer (A, B, C, or D): ").upper()

        if guess == q['answer']:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was {q['answer']}.")

    # Final result
    print("\n" + "="*20)
    print(f"Quiz Finished!")
    print(f"Your Final Score: {score}/{len(questions)}")
    print("="*20)

if __name__ == "__main__":
    run_quiz()
