
import re

def evaluate_deployments(deployments):
    """
    Evaluate the deployment results and count the number of successes, failures, and errors.

    Args:
        deployments (list): A list of JSON objects with 'deployment_id' and 'status'.

    Returns:
        tuple: A tuple containing counts for success, failure, and error statuses.
    """
    # Correct regular expression for valid deployment_id
    valid_id_pattern = r'^d-[a-zA-Z0-9]{10}$'  # Updated pattern to only allow lowercase alphanumeric characters

    # Counters for statuses
    success_count = 0
    failure_count = 0
    error_count = 0

    for deployment in deployments:
        try:
            # Extract fields
            deployment_id = deployment.get("deployment_id")
            print(deployment_id)
            status = deployment.get("status", "").lower()
            print(status)

            # Validate deployment_id using the corrected pattern
            if not re.match(valid_id_pattern, deployment_id):
                error_count += 1
                continue

            # Categorize by status
            if status == "success":
                success_count += 1
            elif status == "failure":
                failure_count += 1
            else:
                error_count += 1
        except Exception:
            # Catch parsing or missing field errors
            error_count += 1

    # Return the counts as a tuple (success, failure, error)
    print(success_count, failure_count, error_count)

# Example Input
deployments = [
    {"deployment_id": "d-1234567890", "status": "success"},
    {"deployment_id": "d-0987654321", "status": "failure"},
    {"deployment_id": "invalid-id", "status": "success"},
    {"deployment_id": "d-abcdefghij", "status": "unknown"},
    {"deployment_id": "d-1234567890", "status": "error"}
]

# Evaluate deployments and return the counts
evaluate_deployments(deployments)
