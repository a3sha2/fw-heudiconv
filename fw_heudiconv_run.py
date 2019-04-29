#!/usr/bin/env python
import json
import flywheel

print('This is an example python script.')
invocation  = json.loads(open('config.json').read())
config      = invocation['config']
inputs      = invocation['inputs']
destination = invocation['destination']


# Display everything provided to the job
def display(section):
    print(json.dumps(section, indent=4, sort_keys=True))

print('\nConfig:')
display(config)
print('\nDestination:')
display(destination)
print('\nInputs:')
display(inputs)

# Make some simple calls to the API
fw = flywheel.Flywheel(inputs['api-key']['key'])
user = fw.get_current_user()
config = fw.get_config()

print('You are logged in as ' + user.firstname + ' ' + user.lastname +
      ' at ' + config.site.api_url[:-4])
