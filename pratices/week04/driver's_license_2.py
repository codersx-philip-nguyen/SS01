def driver_exam():
    question = open('test.txt')
    answer = open('key.txt')
    score = 0
    check = ['A', 'B', 'C', 'D']
    i= 1
    while True:
        ques = ''
        ans = answer.readline()
        while True:
            current_line = question.readline()
            if (current_line).strip() == '*':
                break
            if not current_line:
                break
            print(current_line)

        while True:
            user_ans = str(input('Answer: '))
            if user_ans in check:
                if user_ans == str(ans.strip()):
                    score += 2
                    print("True")
                else:
                    print("False")
                break
            else:
                print("---Invalid answer.Try again!---")
        if not current_line:
            print('Score: ' + str(score))
            break
def main():
    driver_exam()

main()
