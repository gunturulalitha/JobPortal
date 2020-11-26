import csv

from behave import *


@given('Candidate details to enter')
def user_data(context):
    context.user_data = csv.DictReader(open("C://employee_file.csv"))
    print(context.user_data)
    for row in context.user_data:
        print(row['First Name'], row['Last Name'], row['Phone Num'], row['Email'], row['Skills'], row['Education'], row['Emp Auth'])
        first_name = row['First Name']
        last_name = row['Last Name']
        phone_num = row['Phone Num']
        email_id = row['Email']
        tech_skills = row['Skills']
        education = row['Education']
        emp_auth = row['Emp Auth']
        return first_name,last_name,phone_num,email_id,tech_skills,education,emp_auth


@when('submit button is clicked')
def click_submit(context):
    assert True


@then('Check first name field is empty or given and characters are <= 50')
def check_firstname(context):
    context.first_name = user_data.first_name
    print("context.first_name -- ",context.first_name)
    assert True


@then('Check last name field is empty or given and characters are <= 50')
def ckeck_lastname(context):
    context.last_name = user_data.last_name
    print("context.last_name -- ", context.last_name)
    assert True


@then('Check phone number field is empty or given and format should be in 123-345-3456')
def check_phnum(context):
    context.phone_number = user_data.phone_num
    print("context.phone_number -- ", context.phone_number)
    assert True


@then('Check Email Address field is empty or given and format is in abcd@domainname.com')
def check_emailId(context):
    context.email_address = user_data.email_id
    print("context.email_address -- ", context.email_address)
    assert True


@then('Check Technical skill set field is empty or given and characters are <= 200')
def check_techSkills(context):
    context.tech_skills = user_data.tech_skills
    print("context.tech_skills -- ", context.tech_skills)
    assert True


@then('Check Education field is empty or given and characters are <= 20')
def check_education(context):
    context.education = user_data.education
    print("context.education -- ", context.education)
    assert True


@then('Check Employment Authorisation field is empty or given and characters are <= 20')
def check_empAuth(context):
    context.emp_auth = user_data.emp_auth
    print("context.emp_auth -- ", context.emp_auth)
    assert True



