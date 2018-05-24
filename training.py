# training module
class Training:
    def __init__(self, stats_file, exercise_file):
        self.stats_list = self.load_stats(stats_file)
        self.strength = self.stats_list[0]
        self.hypertrophy = self.stats_list[1]
        self.fat_burn = self.stats_list[2]
        self.exercise_dict = self.load_exercise(exercise_file)

    def load_stats(self, stats_file):
        stats_list = []
        with open(stats_file, 'r') as stats:
            for line in stats:
                stats_list.append(line[:-1].split('\t'))
        return stats_list

    def load_exercise(self, exercise_file):
        with open(exercise_file, 'r') as exercise:
            exercise = exercise.readlines()
            exercise_list = exercise[0][:-1].split('\t')
            exercise_list_of_lists = []
            for item in exercise_list:
                temp = item.split('!')
                temp[1] = float(temp[1])
                exercise_list_of_lists.append(temp)
            exercise_dict = dict(exercise_list_of_lists)
            print(exercise_dict)
        return exercise_dict

    def get_random_exercise(self):
        for exercise_name in self.exercise_dict:
            weight_scale = self.exercise_dict[exercise_name]
            print(exercise_name, weight_scale)
            return exercise_name, weight_scale

    def get_stats(self, goal):
        if goal == 'strength':
            return self.strength
        elif goal == 'hypertrophy':
            return self.hypertrophy
        else:
            return self.fat_burn

class Programm:
    def __init__():
        pass

# def load_file():
#     with open('training_list.txt', 'r+') as training_file:
#         training_list = training_file.readlines()
#         to_be_dict = []
#         for line in training_list:
#             to_be_dict.append(line.replace('\n', '').split('|'))
#         # print(to_be_dict)
#         training_dict = dict(to_be_dict)
#     return training_dict


# def format_dict(training_dict):
#     for key in training_dict:
#         training_dict[key] = training_dict[key].split('#')
#         training_dict[key][0] = training_dict[key][0].split('\t')
#         training_dict[key][1] = training_dict[key][1].split('\t')
#         # print(training_dict)
#     return training_dict


# def create_training_dict():
    
#     print(training_dict)
#     return training_dict


def generate_program(user, training_dict):
    training_to_test = {
        'chest': 'Bench Press',
        'biceps': 'Dead Lift',
        'triceps': 'Bench Press',
        'delts': 'Military Press',
        'back': 'Dead Lift',
        'quads': 'Squat',
        'hams and glutes': 'Squat',
    }
    file_name = 'training_program.txt'
    clear_program_log(file_name)

    for training in training_dict:
        exercise_name, weight_scale = training_dict[training].get_random_exercise()
        test = training_to_test[training]
        weight = user.get_test_result()[test]
        print(weight)
        goal = user.get_goal()
        stats = training_dict[training].get_stats(goal)
        print(stats)
        add_program_log(training, exercise_name, weight_scale, weight, stats, file_name)


def create_training_dict():
    exercise_dict = {}
    exercise_names = ['chest', 'biceps']
    for exercise in exercise_names:
        stats_file = 'trainings/{0}_stats.txt'.format(exercise)
        exercise_file = 'trainings/{0}.txt'.format(exercise)
        exercise_dict[exercise] = Training(stats_file, exercise_file)
    print(exercise_dict)
    print(exercise_dict['chest'].strength)
    return exercise_dict


def add_program_log(training, exercise_name, weight_scale, weight, stats, file_name):
    '''Marked to refactory!!! Deadline 05.2010'''
    finall_weight = int(round(float(weight)*float(stats[3])*float(weight_scale)))
    line_to_save = training + '\t'
    line_to_save += exercise_name.strip() + '\t'
    line_to_save += stats[0] + '\t' + stats[1] + '\t' + stats[2] + '\t'
    line_to_save += str(finall_weight) + '\t'
    line_to_save += stats[4] + '\n'
    
    with open(file_name, 'a') as log:
        log.write(line_to_save)


def clear_program_log(file_name):
    with open(file_name, 'w') as clear:
        clear.write('')


def start_module(user):     # dodać user jako argument
    training_dict = create_training_dict()
    generate_program(user, training_dict)



# start_module()
