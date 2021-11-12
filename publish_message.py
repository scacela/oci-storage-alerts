# import packages

import sys
import json
import oci
from config import *

from oci.ons import NotificationDataPlaneClient
from oci.ons.models import MessageDetails
from oci.retry import DEFAULT_RETRY_STRATEGY

def main(title, body):

	# authentication
	config = oci.config.from_file(config_file_path)
	# retry strategy
	retry_strategy = DEFAULT_RETRY_STRATEGY
	# creeate a client instance
	ons_client=NotificationDataPlaneClient(config, retry_strategy=retry_strategy)

	# payload
	message_details_obj = MessageDetails(title=title, body=body)

	# api call
	try:
		publish_message_response = ons_client.publish_message(topic_id, message_details_obj, retry_strategy=retry_strategy)
	except Exception as error:
		publish_message_response = error

	return publish_message_response
