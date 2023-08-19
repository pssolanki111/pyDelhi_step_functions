provider "aws" {
  region = "ap-south-1"
}

resource "aws_lambda_function" "clean_raw_data" {
  filename         = "src/lambdas/clean_raw_data.py"
  function_name    = "cleanRawDataFunction"
  role             = aws_iam_role.lambda_role.arn
  handler          = "clean_raw_data.lambda_handler"
  source_code_hash = filebase64sha256("src/lambdas/clean_raw_data.py")
  runtime          = "python3.8"
}

resource "aws_lambda_function" "process_observations" {
  filename         = "src/lambdas/process_observations.py"
  function_name    = "processObservationsFunction"
  role             = aws_iam_role.lambda_role.arn
  handler          = "process_observations.lambda_handler"
  source_code_hash = filebase64sha256("src/lambdas/process_observations.py")
  runtime          = "python3.8"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_sfn_state_machine" "research_data_pipeline" {
  name     = "ResearchDataPipeline"
  role_arn = aws_iam_role.sfn_role.arn

  definition = jsonencode(file("src/state_machines/research_data_pipeline.json"))
}

resource "aws_iam_role" "sfn_role" {
  name = "step_function_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "states.amazonaws.com"
        }
      }
    ]
  })
}
