import csv


def handler(event, context):
    csv_text = event['csv_text']
    reader = csv.reader(csv_text.split('\n'), delimiter=',')
    cleaned_data, observations = {}, []

    for row in reader:
        try:
            timestamp, equipment_id, measurement_type, observation_id, data, wavelengths, unit = row
        except ValueError:
            continue

        if not all([timestamp, equipment_id, measurement_type, observation_id]):
            continue

        final_data_values, final_wavelengths = [], []
        for datum in data:
            try:
                final_data_values.append(float(datum))
            except (ValueError, TypeError):
                final_data_values.append(0.0)
        for wavelength in wavelengths:
            try:
                final_wavelengths.append(int(wavelength))
            except (ValueError, TypeError):
                final_wavelengths.append(0)

        if not cleaned_data:
            cleaned_data = {
                'timestamp': timestamp,
                'equipment_id': equipment_id,
                'measurement_type': measurement_type
            }

        if measurement_type == 'spectral_analysis':
            observation = {
                'observation_id': observation_id,
                'data': data,
                'wavelengths': wavelengths,
                'unit': unit
            }
            observations.append(observation)

    cleaned_data['observations'] = observations
    cleaned_data['number_of_observations'] = len(observations)
    return cleaned_data
