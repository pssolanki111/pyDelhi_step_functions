

STANDARD_OBSERVATION = {
    "data": [0.15, 0.09, 0.0, 0.2, 0.35, 0.18, 0.12],
    "wavelengths": [400, 450, 520, 550, 600, 650, 700, 750],
    "unit": "arb. units"
}


def handler(event, context):
    observations = event['observations_batch']
    qualified_observations = list(process_observations(observations))
    return {"qualified_observations": qualified_observations}


def process_observations(observations):
    """
    Compares the observations to a standard observation

    :param observations: A list of dictionary containing the observation data
    :return: list of qualified observations
    """
    for observation in observations:
        if observation["data"] != STANDARD_OBSERVATION["data"]:
            yield observation

