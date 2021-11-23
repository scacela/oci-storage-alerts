import subprocess

def main(volume_path):
	process = subprocess.Popen(["df", "-h", volume_path], stdout=subprocess.PIPE)
	output = process.stdout.read()
	pruned = output.decode("ascii")
	output_array = pruned.split()

	GB_used = output_array[9].replace("G", "")
	GB_available = output_array[10].replace("G", "")
	percent_used = output_array[11].replace("%", "")
	return GB_used, GB_available, percent_used
