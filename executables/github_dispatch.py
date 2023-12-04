import requests, json, sys, argparse

def show_response(dispatch, resp):
    #print('response code for {} is: {}'.format(dispatch, resp.status_code))
    response_msg = 'response code for {} is: {}'.format(dispatch, resp.status_code)
    if resp.status_code != 204:
        status_code = resp.status_code
        resp = json.loads(resp.text)
        for key, value in resp.items():
            print(f'{key} : {value}')
        response_msg = str(status_code) + ' '.join([f'{key} : {value}\n' for key, value in resp.items()])
        print(f'Request returned with response:\n{response_msg}')
    else:
        print(f'Dispatch for action {dispatch} was received successfully.')

def send_dispatch(dispatch:str):
    #send request to git api
    url = 'https://api.github.com/repos/justinli00/leviathan/dispatches'
    payload = {
        'event_type' : dispatch,
        'client_payload' : {}
    }

    #create client payload
    if start is not None and end is not None:
        payload['client_payload']['start-revision'] = start
        payload['client_payload']['end-revision'] = end
    if test_revision is not None:
        payload['client_payload']['test-revision'] = test_revision

    header = {
        'Accept' : 'application/vnd.github+json',
        'Authorization' : f'token {git_token}'
    }
    payload = json.dumps(payload)
    resp = requests.post(url=url, headers=header, data=payload)
    
    #show response
    show_response(dispatch, resp)

def get_registration():
    #send request to git api
    url = 'https://api.github.com/repos/justinli00/leviathan/actions/runners/registration-token'
    header = {
        'Accept' : 'application/vnd.github+json',
        'Authorization' : f'token {git_token}'
    }
    resp = requests.post(url=url, headers=header)
    
    #show response
    show_response('register', resp)

if __name__ == "__main__":
    #get the token
    with open('repo_dispatch.token', 'r') as f:
        git_token = f.read()
        
    parser = argparse.ArgumentParser(description='Sends a dispatch to the leviathan git repository.')
    parser.add_argument('--type', type=str,
                        help='The type of the dispatch to send out.')
    parser.add_argument('--start', type=int, required=False,
                        help='For dispatches to check-tests.yaml. Specifies when to start testing. Must be supplied with end.')
    parser.add_argument('--end', type=int, required=False,
                        help='For dispatches to check-tests.yaml. Specifies when to stop testing. Must be supplied with start.')
    parser.add_argument('--test_revision', type=int, required=False,
                        help='For dispatches to check-tests.yaml. NOT SUPPORTED FOR DISPATCHES TO run-tests.yaml! Specifies which revision of testing scripts to use.' + 
                             'If not supplied, then the testing folder of the revision being tested will be used.')
    args = parser.parse_args()
    args = parser.parse_args()
    dispatch_type = args.type
    start = args.start 
    end = args.end
    test_revision = args.test_revision
    
    print(f'Sending out dispatch for: {dispatch_type}')
    if dispatch_type == 'register': get_registration()
    else:                           send_dispatch(dispatch_type)
