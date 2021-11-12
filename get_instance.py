from config import *
import oci
import json

def main():
	config = oci.config.from_file(config_file_path)
	# Initialize service client with default config file
	core_client = oci.core.ComputeClient(config)
	# API call
	get_instance_response = core_client.get_instance(instance_id=compute_instance_id)
	# parse the JSON
	data = json.loads(str(get_instance_response.data))
	return data["display_name"], data["region"]
