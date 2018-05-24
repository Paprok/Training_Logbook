import os
# test functions


def start_module(user):
    answer = input('Do you want to attempt test?(Y/N)')
    if answer.lower() == 'y':
        print('Please enter scores of your test(Q to quit)! \n')
        # exercise_list = [
        #     'Squat',
        #     'Dead Lift',
        #     'Millitary Press',
        #     'Bench Press',
        #     'Pull Ups',
        #     'Run 5km'
        # ]
        escape = False
        for key in user.get_test_result():
            if not escape:
                answer = input('Your {0} result: '.format(key))
                if answer.lower().strip() == 'q':
                    escape = True
                else:
                    user.set_test_result(key, answer)
    os.system('clear')
