import main

def test_select_from_matrix_option():
    option = "5"
    matrix = main.select_from_matrix_option(option)
    ground_truth_matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]] + [[0 for _ in range(10)] for _ in range(7)]

    assert matrix == ground_truth_matrix

def test_implement_game_of_life():
    matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]] + [[0 for _ in range(10)] for _ in range(7)]
    output_matrix = main.implement_game_of_life(matrix)
    ground_truth_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]] + [[0 for _ in range(10)] for _ in range(6)]

    assert output_matrix == ground_truth_matrix

if __name__ == "__main__":
    test_select_from_matrix_option()
    test_implement_game_of_life()