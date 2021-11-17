# oci-storage-alerts

## Get alerted when a user-defined volume has reached or exceeded a user-defined storage threshold.

#### Prerequisites:
* In the [Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/home.htm) service, a Topic is set up with at least one Subscription, and your OCI user has at least [use](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm)-level access to the service.
* A compute instance is running, it has internet access, and you are able to access its CLI.

#### Getting Started:
1. Setup OCI SDK and CLI config file, OCI API public and private keys on the compute instance, and register the OCI API public key with your OCI user account. Instructions are available [here](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/installation.html#install).
2. Install this project to the home directory of your compute instance:
```
sudo yum -y install git
git clone https://github.com/scacela/oci-storage-alerts.git ~/oci-storage-alerts
```
3. Edit your configuration variables by editing their assigned values in <b>~/oci-storage-alerts/config.py</b>. Change the value assigned to variable <b>enable_alerts</b> to <b>True</b> when ready to enable the alerts.
```
vi ~/oci-storage-alerts/config.py
```
4. Set the schedule that determines how frequently the storage usage of the user-defined is measured.\
Open the cron table in edit mode with the following command:
```
crontab -e
```
And paste the scheduled command into it, shown in the code snippet below.\
\
To customize the frequency with which the storage usage of the user-defined volume is measured, refer to [this site](https://crontab.guru/) as a reference for cron expressions.\
\
You will also be able to find the output of the most recent execution of the program in <b>~/oci-storage-alerts/out.log</b>.
```
*/30 * * * * python3 ~/oci-storage-alerts/main.py &> ~/oci-storage-alerts/out.log
```