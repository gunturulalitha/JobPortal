from behave import *
import re


@then('Check first name field is empty or given and characters "{FirstName}" are <= 50')
def check_firstname(context, FirstName):
    context.first_name = FirstName
    first_name_len = len(context.first_name)
    if first_name_len != 0:
        if first_name_len <= 50:
            assert True, "Test Passed"
        else:
            assert False
    else:
        assert False


@then('Check last name field is empty or given and characters "{LastName}" are <= 50')
def check_lastname(context, LastName):
    context.last_name = LastName
    last_name_len = len(context.last_name)
    if last_name_len != 0:
        if last_name_len <= 50:
            assert True
        else:
            assert False
    else:
        assert False


@then('Check phone number field is empty or given and format should be "{PhNum}" in 123-345-3456')
def check_phNum(context,PhNum):
    context.phone_number = PhNum
    if len(context.phone_number) != 0:
        if len(context.phone_number) != 12:
            assert False
        for i in range(12):
            if i in [3, 7]:
                if context.phone_number[i] != '-':
                    assert False
            elif not context.phone_number[i].isalnum():
                assert True
        assert True
    else:
        assert False


@then('Check Email Address field is empty or given and format "{EmailId}" is in abcd@domainname.com')
def email_format(context, EmailId):
    context.email_id = EmailId
    if(len(context.email_id)) != 0:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, context.email_id):
            assert True, "Test Passed"
        else:
            assert False
    else:
        assert False


@then('Check Technical skill set field is empty or given and characters "{TechSkills}" are <= 200')
def tech_skills(context,TechSkills):
    context.tech_skills = TechSkills
    if len(context.tech_skills) != 0:
        if len(context.tech_skills) <= 200:
            assert True, "Test Passed"
        else:
            assert False
    else:
        assert False


@then('Check Education field is empty or given and characters "{Education}" are <= 20')
def check_edu(context,Education):
    context.education = Education
    if len(context.education) != 0:
        if len(context.education) <= 20:
            assert True, "Test Passed"
        else:
            assert False
    else:
        assert False


@then('Check Employment Authorisation field is empty or given and characters "{EmpAuth}" are <= 20')
def check_emp_auth(context,EmpAuth):
    context.emp_auth = EmpAuth
    if len(context.emp_auth) != 0:
        if len(context.emp_auth) <= 20:
            assert True
        else:
            assert False
    else:
        assert False