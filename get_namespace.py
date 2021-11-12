from config import *
import oci

def main():
	config = oci.config.from_file(config_file_path)
	# Initialize service client with default config file
	object_storage_client = oci.object_storage.ObjectStorageClient(config)
	# API call
	get_namespace_response = object_storage_client.get_namespace()
	# Get the data from response
	return get_namespace_response.data
