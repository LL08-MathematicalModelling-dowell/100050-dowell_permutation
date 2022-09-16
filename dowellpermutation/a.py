import json
import requests
import pprint
from population import targeted_population



candidate_response = targeted_population('hr_hiring','dowelltraining',  ['full_name'], 'life_time')
print(candidate_response)