# log book - open it when on the gym. PrintOut exercises and get results.

import time


class LogBook:

    def __init__(self, workout_for_today,):
        self.workout_for_today = workout_for_today
        self.exercises_list = self.load_file()

        # self.set =

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
            print('\tExercise no{}. {}. Do {} sets of {} repetitions. Rest {}sek betweene sets. Your tempo should be {}'
                  .format(i+1, self.load_file()[i][1], self.load_file()[i][2], self.load_file()[i][3],
                          self.load_file()[i][4], self.load_file()[i][6]))

    def start_exercise(self):

        try:
            lest_start = input("")
        for i in range(len(self.exercises_list)):
            print("Do excersise no{}\n\t-{}".format(i+1, self.load_file()[i][1]))

    def get_workout_results(self):
        pass


def start_module():
    cwiczymy = LogBook('exercises.txt')

    cwiczymy.print_workout()
    cwiczymy.start_exercise()


start_module()


