import json

employees = [
    {
        "id": 1,
        "name": "John",
        "age": 28,
        "department": "Cloud",
        "designation": "Cloud Engineer",
        "experience": "4 Years"
    },
    {
        "id": 2,
        "name": "Alice",
        "age": 30,
        "department": "DevOps",
        "designation": "DevOps Engineer",
        "experience": "5 Years"
    }
]

departments = [
    "Cloud",
    "DevOps",
    "Cyber Security",
    "Web Development"
]

company = {
    "company": "ABC Technologies",
    "location": "Bangalore",
    "domain": "IT Services",
    "employees": 25
}

health = {
    "status": "Healthy",
    "api": "Employee API",
    "version": "1.0"
}

def lambda_handler(event, context):

    route = event["routeKey"]

    if route == "GET /employees":
        return {
            "statusCode": 200,
            "body": json.dumps(employees)
        }

    elif route == "GET /employees/{id}":
        emp_id = int(event["pathParameters"]["id"])

        for emp in employees:
            if emp["id"] == emp_id:
                return {
                    "statusCode": 200,
                    "body": json.dumps(emp)
                }

        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Employee not found"})
        }

    elif route == "GET /departments":
        return {
            "statusCode": 200,
            "body": json.dumps(departments)
        }

    elif route == "GET /company":
        return {
            "statusCode": 200,
            "body": json.dumps(company)
        }

    elif route == "GET /health":
        return {
            "statusCode": 200,
            "body": json.dumps(health)
        }

    return {
        "statusCode": 404,
        "body": json.dumps({"message": "Invalid Route"})
    }