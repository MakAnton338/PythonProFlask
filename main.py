from flask import Flask, request
from faker import Faker
app = Flask(__name__)


@app.route("/requirements/")
def requirements():
    with open(r'/requirements.txt', "r") as file:
        requirement = file.read()
    return '<pre>{}</pre>'.format(requirement)


@app.route("/generate-users/")
def generate_users():
    fake = Faker()
    list_name_mail = []
    users_count = request.args.get('count', 0, type=int)
    for i in range(users_count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}_{last_name.lower()}@example.com"
        list_name_mail.append(f"{first_name} {last_name}, {email}")
    res = '\n'.join(list_name_mail)
    return '<pre>{}</pre>'.format(res)


@app.route("/mean/")



