# sky-api-python-client

A lightweight, easy to use, Python library for communicating with the Blackbaud Sky API

##### Loading Sky and load_dotenv
```python
>>> from sky import Sky
>>> from dotenv import load_dotenv
>>> # Loading BB_API_Key from .env file
>>> load_dotenv()
>>> client = Sky(
    api_key=None,
    file_path='sky_credentials.json',
    token_path=".sky-token"
  )
```

#### Sending a GET Request
```Python
>>> roles = client.get(endpoint='roles')
>>> roles['value'][:2]
[{'id': 67454, 
  'base_role_id': 1, 
  'hidden': False, 
  'name': 'Academic Chair'},
 {'id': 58802,
  'base_role_id': 523,
  'hidden': False,
  'name': 'Academic Group Manager'}]
```

#### Sending a POST Request
```Python
>>> new_user = client.post(data = {
      "first_name": "API",
      "last_name": "User"
    })
>>> id = int(new_user.text)
>>> id
5039522
```

#### Sending a PATCH Request
```Python
>>> update_user = client.patch(data={
      "id": id,
      "last_name": "NewUser"
    })
>>> update_user.satus_code
200
```

### About

This is a python library for connecting the [Blackbaud Sky API](https://developer.blackbaud.com/skyapi/). Behind the scenes the Blackbaud SKY API uses [Authorization Code Flow](https://developer.blackbaud.com/skyapi/docs/authorization/auth-code-flow), which requires the client ID and client secret to get a refresh token and make API calls. The goal of the sky-api-python-client is to abstract details from the OAuth2.0 process so the user can get to coding as quickly as possible.

In order to achieve this a json file with your Blackbaud Application client_id, client_secret, and redirect_uri are required. If you are unsure how to get that information please see the section on [SKY API requirements](https://github.com/LearnThinkCreate/sky-api-python-client#sky-api-requirements).

The library itself is a wrapper around the `authlib` and `requests` python libraries. Authlib is used to establish a OAuth2Session, while requests handle the calls to the SKY API. A binary file is used to store your OAuth2Token in between sessions so that this library can be used in non-interactive sessions.

To get or post data from the Sky API you first need to configure your working directory using the guidelines from the [Installing Sky](https://github.com/LearnThinkCreate/sky-api-python-client#instalation--configuration). Once that's done, import the Sky class from sky and pass in the value for your `sky_credentials` and `token_path` if necessary.See Blackbaud's documentations on specifiec [references](https://developer.blackbaud.com/skyapi/apis) and [endpoints](https://developer.sky.blackbaud.com/docs/services/school/operations/v1usersget) that can be passed as arguments in api calls.

### Installing sky-api-python-client and setting up your working directory
- Install the latest version of the sky-api-python-client by running `python -m pip install --upgrade sky-api-python-client`
- Configure a sky_credentials.json file in your working directory. You can use the [sky_credentials_template.json](https://github.com/LearnThinkCreate/sky-api-python-client/blob/main/template.json) file for reference. 
    - By default the Sky class looks for a sky_credentials.json file. You can name it something else but you must pass in the new value into the `file_path` argument when initializing `Sky`.
- I highly recommend saving the API key you'd like to use in an environment variable called `BB_API_KEY` to avoid exposing your credentials to any script you create. The easiest way to do this is to create a .env file in your working directory and use the `python-dotenv` library to load the .env values into your script. 
    - Please see the example above or go to the [python-dotenv documentation](https://pypi.org/project/python-dotenv/#getting-started).
    - When called Sky will automatically check if there's a value for `BB_API_KEY`


### Using sky-api-python-client 
- Once sky-api-python-client is installed you can go directly into coding, even if you have not authorized your app yet.
    - The first time that any Sky request is sent (get, post, patch or delete) the sky-api-python-client will check the `token_path` for a valid API token. If it finds one it will proceed with the HTTP request. Otherwise it will check the `file_path` for a valid .json file with your Blackbaud credentials. 
- If Blackbaud credentials are found your default web browser will open and you will be asked to authorize your application. If your sky_crendtials are valid (the client_id, client_secret, and redirect_uri matches what's on your [application page](https://developer.blackbaud.com/apps/)) the sky-api-python-client will retrieve a access & refresh token on your behalf and save them for future use in a binary file located on your `token_path`. Otherwise the call will be executed without needing any user interaction


### SKY API requirements

- **A Blackbaud Developer subscription key**
    - If you have not already done so, complete the [Getting started guide](https://developer.blackbaud.com/skyapi/docs/getting-started). This will walk you through the process of registering for a Blackbaud developer account and requesting a subscription to an API product.
    - Once approved, your subscription will contain a **primary key** and **secondary key**. You can either pass the value of the API key directly into your script or you can save it in a environment variable call **BB_API_KEY**.
    - You can view your subscription keys on your [Blackbaud Developer profile](https://developer.sky.blackbaud.com/developer).
- **A Blackbaud Developer application ID and application secret**
    - [Register your application](https://developer.blackbaud.com/apps/) in order to obtain the **application ID** (client ID) and **application secret** (client secret).
    - When you call the Blackbaud Authorization Service from your application, you pass the `redirect_uri` as part of the call. The Blackbaud Authorization Service redirects to this URI after the user grants or denies permission. Therefore, you must whitelist the web address(es) or the authorization will fail.
    - URIs must _exactly_ match the value your application uses in calls to the Blackbaud Authorization Service.

