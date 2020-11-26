from sys import path

from behave import given, when, then
import os


@given('Home page opened')
def home_page(context):
    assert True


@when('User browses and uploads the resume and clicks Upload button')
def click_button(context):
    assert True


@then('Uploaded file should be of type .doc/.docx "{path}"')
def file_type(context, path):
    context.path = path
    file_name, file_extension = os.path.splitext(context.path)
    if file_extension == ".doc" or ".docx":
        # print("File type ==== ", file_extension)
        assert True
    else:
        assert False


@then('Maximum uploaded file size should be less than 20KB "{path}" , "{size}"')
def file_size(context, path,size):
    context.path = path
    context.size = size
    st = os.stat(path)
    if (round(st.st_size / 1000)) < 20:
        # print("In If condition " , round(st.st_size / 1000))
        assert True
    else:
        assert False

