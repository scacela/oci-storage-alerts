import os
from os import popen
from config import *
from sys import exit
import get_namespace
import get_instance
import get_topic
import publish_message
import get_storage_statistics
import get_message

def main():
	if enable_alerts:
		# get the GB available, GB used, and percent used
		GB_available, GB_used, percent_used = get_storage_statistics.main(volume_path)
		
		# determine whether the storage usage limit has been reached or exceeded
		if int(percent_used) == percent_threshold:
			reached_or_exceeded = "reached"
		elif int(percent_used) > percent_threshold:
			reached_or_esceeded = "exceeded"
		else:
			exit()
	else:
		exit()
	# get the tenancy namespace
	tenancy_namespace = get_namespace.main()
	# get the compute instance nam and regione
	compute_instance_display_name, compute_instance_region = get_instance.main()
	# get the topic name
	topic_name = get_topic.main()
	# build a message
	title, body = get_message.main(reached_or_exceeded, tenancy_namespace,
					compute_instance_display_name, compute_instance_region,
					topic_name,
					GB_available, GB_used, percent_used)
	# publish the message
	publish_message.main(title, body)
main()
