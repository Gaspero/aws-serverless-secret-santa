import requests
from behave import *


@given(u'{request_type} request is sent to the service')
def step_impl(context, request_type):
    context.request_type = request_type
    request_method = request_type.lower()
    request_call = 'requests.' + request_method
    api_endpoint = 'https://aiq9hcvn0m.execute-api.us-east-1.amazonaws.com/Prod/addUser'
    context.api_endpoint = api_endpoint
    context.request_call = request_call


@given(u'the name is {name}')
def step_impl(context, name):
    context.name = name


@given(u'the email is {email}')
def step_impl(context, email):
    context.email = email


@when("request is executed")
def step_impl(context):
    payload = {"name": context.name, "email": context.email}
    if context.request_type in ("POST", "PUT"):
        context.response = eval(context.request_call + '(context.api_endpoint, json=payload)')
    else:
        context.response = eval(context.request_call + '(context.api_endpoint)')


@then("response name is {name}")
def step_impl(context, name):
    try:
        resp_name = context.response.json()['name']
        assert resp_name == name
    except Exception as e:
        assert False, e


@then("response email is {email}")
def step_impl(context, email):
    try:
        resp_email = context.response.json()['email']
        assert resp_email == email
    except Exception as e:
        assert False, e


@then("response id is provided")
def step_impl(context):
    try:
        resp_id = context.response.json()['id']
        assert isinstance(resp_id, int)
    except Exception as e:
        assert False, e


@then("response code is {code:d}")
def step_impl(context, code):
    assert (context.response.status_code == code), (code, context.response.status_code, context.response.json())

