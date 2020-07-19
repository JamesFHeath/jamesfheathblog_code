# Intro
Hi Everyone, SearingFrost here with an AWS Tutorial.
Today, we're going to set up logging to cloudwatch from an EC2 instance using a cloudformation template.
Setting up a Cloudwatch Agent on EC2 allows you to log files locally on your EC2 and have the Cloudwatch Agent send them to a specified Cloudwatch Group.
I found that setting up logging following the AWS guides was a little complicated and I wanted to boil it down and give a straightforward example. 
The cloudformation template and cloudwatch agent config file I used are both linked in the description. 

# Cloudwatch Configuration File
We're just creating a basic configuration file for logging.
Anything we log on our EC2 instance to /opt/aws/amazon-cloudwatch-agent/logs/*.log will be outputted in Cloudwatch under log group test.log and log stream test.log.
Put this config file into your desired S3 location. 


# Cloudformation Template
This cloudformation template contains a generic autoscaling group.
The important part is installing and running our cloudwatch agent in the userdata section. 
We first install the cloudwatch agent
Then we copy our configuration file over from S3
Then we start the cloudwatch agent with our configuration file
And then we just echo 'testlog' to a monitored file.

# Testing
All we do now is check the log group after an EC2 instance has started up, and we can see some generic cloudwatch agent logs and then our message 'testlog'. 

# Outro
Thanks for watching, I hope this helped simplify the process of logging with Cloudwatch.
The links to my template, blog post, and the AWS references are in the description. 
I'll see everyone next time!