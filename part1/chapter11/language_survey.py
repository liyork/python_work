from survey import AnonymousSurvey

if __name__ == '__main__':
    question = "what language did you first learn to speak? "
    my_survey = AnonymousSurvey(question)

    my_survey.show_question()
    print("enter 'q' at any time to quit.\n")
    while True:
        response = input("language: ")
        if response == 'q':
            break
        my_survey.store_response(response)

    print("thank you to everyone who participated in the survey")
    my_survey.show_results()
