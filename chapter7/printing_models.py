def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("completed as follow:")
    for completed_model in completed_models:
        print(completed_model)


if __name__ == '__main__':
    unprinted_designs = ['phone', 'robot', 'dodecahedron']
    completed_models = []

    # 使用引用传递
    # print_models(unprinted_designs, completed_models)
    # 使用副本，避免修改unprinted_designs，不过带来时间和内存的开销
    print_models(unprinted_designs[:], completed_models)
    show_completed_models(completed_models)
