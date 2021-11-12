from config import *
from textwrap import dedent

def main(reached_or_exceeded, tenancy_namespace,
	compute_instance_display_name, compute_instance_region,
	topic_name,
	GB_available, GB_used, percent_used):
	
	title = f"Storage usage limit {reached_or_exceeded}, compute instance {compute_instance_display_name}, volume path {volume_path}"
	body = dedent(f"""
		Hello {tenancy_namespace} user,


		The storage usage limit of a volume at path {volume_path} on compute instance {compute_instance_display_name} has {reached_or_exceeded} the threshold of {percent_threshold}% usage, which triggered this alert message.

		{percent_used}%, or {GB_used} GB of the volume's storage has been used.

		The volume has {GB_available} GB of available storage remaining.

		You are receiving this message because you are subscribed to Topic {topic_name}.


		Compute instance details:

		OCID:         {compute_instance_id}
		Display Name: {compute_instance_display_name}
		Region:       {compute_instance_region}  
		""")
	return title, body
