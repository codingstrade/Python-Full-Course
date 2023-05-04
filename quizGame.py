questions = {
    "What is the capital of France?": "Paris",
    "What is the largest country in the world by area?": "Russia",
    "What is the currency of Japan?": "Yen",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the largest organ in the human body?": "Skin",
    "added question ?": "python"
}

score = 0

print("Welcome to the quiz Game!")
print("Answer the following questions correctly to increase your score.")

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print('Correct!')
        score += 1
    else:
        print("Incorrect. The Correct answer is", answer, ".")
print("quiz complete. your final score is", score, "out of", len(questions))
