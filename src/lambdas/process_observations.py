

STANDARD_OBSERVATION = {
    "data": [0.15, 0.09, 0.0, 0.2, 0.35, 0.18, 0.12],
    "wavelengths": [400, 450, 520, 550, 600, 650, 700, 750],
    "unit": "arb. units"
}


def handler(event, context):
    qualified_observation = process_observation(event["qualified_observations"][0])
    return {
        "qualified_observations":
            [qualified_observation] if qualified_observation else []
    }


def process_observation(observation) -> dict | None:
    """
    Compares the observations to a standard observation

    :param observation: A dictionary containing the observation data
    :return: observation if it is qualified, else None
    """
    if observation["data"] != STANDARD_OBSERVATION["data"]:
        return observation

    return None

