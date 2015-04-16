import boto.ec2
import os

class Main:

	def __init__(self):
		self.aws_access_key_id = os.environ['INFRA_1_ID']
		self.aws_secret_access_key = os.environ['INFRA_1_SECRET']
		self.aws_region = os.environ['INFRA_1_REGION']

	def connect(self):
		conn = boto.ec2.connect_to_region(self.aws_region, aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key)
		reservations = conn.get_all_instances()
		instances = []
		for reservation in reservations:
			instances.append(reservation.instances[0].id)
		print instances

	def demotest(self):
		return 2

if __name__ == '__main__':
	main = Main()
	main.connect()
	print main.demotest()