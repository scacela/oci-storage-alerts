from config import *
import oci
import json

def main():
	config = oci.config.from_file(config_file_path)
	# Initialize service client with default config file
	ons_client = oci.ons.NotificationControlPlaneClient(config)
	# API call
	get_topic_response = ons_client.get_topic(topic_id=topic_id)
	data = json.loads(str(get_topic_response.data))
	# Get the data from response
	return data["name"]
