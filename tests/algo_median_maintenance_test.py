from algorithms.median_maintenance import read_stream, calculate_medians


def test_calc_medians_short():
    meds = [1, 1, 8, 8, 8, 7, 7, 4, 6, 5]
    fn = 'algorithms/input-files/median_maintenance_input_test.txt'
    stream = read_stream(fn)
    assert calculate_medians(stream) == meds
