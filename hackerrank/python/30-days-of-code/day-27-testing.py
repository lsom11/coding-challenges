class TestDataEmptyArray():

    @staticmethod
    def get_array():
        return list()


class TestDataUniqueValues():

    @staticmethod
    def get_array():
        return [5, 2, 8, 3, 1, -6, 9]

    @staticmethod
    def get_expected_result():
        return 5


class TestDataExactlyTwoDifferentMinimums():

    @staticmethod
    def get_array():
        return [5, 2, 8, 3, 1, -6, 9, -6, 10]

    @staticmethod
    def get_expected_result():
        return 5
