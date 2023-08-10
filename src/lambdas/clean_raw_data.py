
def handler(event, context):
    csv_text = event['csv_text']
    lines = csv_text.strip().split('\n')
    cleaned_data, observations = None, []

    for line in lines[1:]:
        parts = line.split(',')
        timestamp, equipment_id, measurement_type, observation_id, data, wavelengths, unit = parts

        if not all([timestamp, equipment_id, measurement_type, observation_id]):
            continue  # Skip empty lines

        if not cleaned_data:
            cleaned_data = {
                'timestamp': timestamp,
                'equipment_id': equipment_id,
                'measurement_type': measurement_type
            }

        if measurement_type == 'spectral_analysis':
            observation = {
                'observation_id': observation_id,
                'data': [float(val) if val != 'null' and val != 'error' and val != 'invalid' else 0.0 for val in
                         data.split(',')],
                'wavelengths': [int(val) if val != '' else 0 for val in wavelengths.split(',')],
                'unit': unit
            }
            observations.append(observation)

    cleaned_data['observations'] = observations
    cleaned_data['number_of_observations'] = len(observations)
    return {"cleaned_data": cleaned_data}
