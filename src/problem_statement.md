## Context

There is a scientific research facility having a large number of equipments that each generate large amounts of data to be processed. The data produced represents observations made during the experiments.

## Desired flow

- The data from the equipments is generated async
- Data is accepted and filtered/cleaned
- Multiple data points (Batches) need to be processed in parallel
  - Based on the results of the processing, it is determined if the batch (part of it) qualifies for an alert to the facility operators.
- All qualifying batches are collected together and sent to an SNS topic as a broadcast message.

## Requirements 
- Resilience is a must. Observations are critical to scientific researches and even a small failure can cause a lot of damage.
- The order of operations must absolutely be maintained.
- The higher the performance, the better.

## Data Formats

Raw Data is a CSV. Please see `fixture/raw_data.csv` for an example.
Cleaned Data is a Dictionary that contains observations. Please see `fixtures/sample_cleaned_data.json`
