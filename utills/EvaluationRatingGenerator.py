import random

RATING_VALUES_IDS = ["Unsatisfactory", "Improvement_Required", "Developing_Performer", "Solid_Performer",
                     "Exceeds_Expectations", "Outstanding"]


# TODO: put it in a separate file
# @pytest.fixture(scope="module")
def generate_evaluation_rating(table_rows=18):
    # TODO: make it auto according to table row num
    result = []
    for index in range(table_rows):
        # result.append(RATING_VALUES_IDS[3])
        result.append(random.choice(RATING_VALUES_IDS))
    return result


class EmployeeEvaluationRatingGenerator:
    _instance = None
    evaluationSelections = []
    dislikesText = "dislikes_text"
    likesText = "likes_text"
    improvementsText = "improvements_text"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.evaluationSelections = generate_evaluation_rating()

        return cls._instance


class SupervisorEvaluationRatingGenerator:
    _instance = None
    evaluationSelections = []
    strengthsText = "strengths_text"
    improvementsText = "improvements_text"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.evaluationSelections = generate_evaluation_rating()

        return cls._instance
