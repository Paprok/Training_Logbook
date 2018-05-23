# training module
def load_file():
    with open('training_list.txt', 'r+') as training_file:
        training_list = training_file.readlines()
        to_be_dict = []
        for line in training_list:
            to_be_dict.append(line.replace('\n', '').split('|'))
        # print(to_be_dict)
        training_dict = dict(to_be_dict)
    return training_dict


def format_dict(training_dict):
    for key in training_dict:
        training_dict[key] = training_dict[key].split('#')
        training_dict[key][0] = training_dict[key][0].split('\t')
        training_dict[key][1] = training_dict[key][1].split('\t')
        # print(training_dict)
    return training_dict


def create_training_dict():
    training_dict = load_file()
    training_dict = format_dict(training_dict)
    print(training_dict)
    return training_dict


def generate_training(training_dict, test_result):
    pass



def start_module(user):
    training_dict = create_training_dict()
    test_result = user.get_test_result()
    generate_training(training_dict, test_result)


create_training_dict()
