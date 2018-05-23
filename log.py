# log book - open it when on the gym. PrintOut exercises and get results.

import time
# import menu


class LogBook:

    def __init__(self, workout_for_today,):
        self.workout_for_today = workout_for_today
        self.exercises_list = self.load_file()

    def load_file(self):

        with open(self.workout_for_today) as file:
            lines = file.readlines()

        exercises = []
        for i in range(len(lines)):
            exercise = lines[i].replace('\n', '').split('\t')
            exercises.append(exercise)

        return exercises

    def print_workout(self):
        print("\nHello! Today you have following exercises to do:\n")
        for i in range(len(self.exercises_list)):           
            print('Exercise no{0}\n\t{1}. Do {2} sets of {3} repetitions with {5}kg\n\tRest {4}sek between sets.'
                  'Your tempo should be {6}\n'
                  .format(i+1, self.exercises_list[i][1], self.exercises_list[i][2], self.exercises_list[i][3],
                          self.exercises_list[i][4], self.exercises_list[i][5], self.exercises_list[i][6]))
        self.start_exercise()

    def start_exercise(self):
        corect_input = False
        while not corect_input:
            try:
                lets_start = str.upper(input("Insert Y to start or N to quit to menu: "))
                if lets_start == 'Y':
                    self.get_workout_results()
                    corect_input = True
                    # self.workout_duration()
                elif lets_start == 'N':
                    print("stop")
                    exit()
                    # menu.start_module()
                else:
                    raise ValueError('{} is not corect choice.'.format(lets_start))
            except ValueError as err:
                print('You entered wrong input! {}'.format(err))

    def get_workout_results(self):

        for an_excercise in range(len(self.exercises_list)):
            print("Do excersise no{}\n\t-{}".format(an_excercise+1, self.load_file()[an_excercise][1]))
            no_of_sets = int(self.exercises_list[an_excercise][2])
            self.log_result_in(self.exercises_list[an_excercise][1])
            for a_set in range(no_of_sets):
                corect_input = False
                while not corect_input:
                    try:
                        result_of_set = int(input('Set no{}. Enter here no of reps: '.format(a_set + 1)))
                        self.log_result_in(result_of_set)
                    except ValueError:
                        print("Please enter number of reps!")
                    else:
                        corect_input = True
            self.log_result_in('\n')

    def log_result_in(self, an_input):
        with open('workoout_user_date', 'a') as file:
            file.write(str(an_input) + ' ')


def start_module():
    cwiczymy = LogBook('my_fbw.txt')

    cwiczymy.print_workout()


start_module()
