from json import load

correct_answers = 0
with open('quiz.json') as questions_file:
    questions = load(questions_file)


    for question in questions:
        print(question['question'])
        for index, answer in enumerate(question['answers']):
            print(index, answer['text'])

        user_answer = int(input('How do you think which answer is correct?'))    
        try:
            is_correct_answer = question['answers'][user_answer]['correct']
            if is_correct_answer:
                correct_answers += 1
        except IndexError:
            pass
        
        print('--' * 10)

print(correct_answers, 'correct answers')
