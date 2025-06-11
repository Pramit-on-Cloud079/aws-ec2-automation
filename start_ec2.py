import boto3

ec2 = boto3.client('ec2')

instance_id = 'i-0e4630fecd27e3e4d'  # Replace with your actual instance ID

response = ec2.start_instances(InstanceIds=[instance_id])

print(f"Starting EC2 instance: {instance_id}")
print(response)
