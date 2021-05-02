# A simple Kafla application

### A kafka application to simulate streaming events and store data into DynamoDB.

#### Step 1:

Clone this repository

git clone https://github.com/rsrrohit/kafka_netflix_project

Credit for the data goes to Mike Metzger.

#### Step 2:

Run the environment.sh file using the linux command
sudo ./environment.sh

#### Step 3:

Create the credentials file in the ~/.aws directory
~/.aws/credentials and store id-key pair. Follow this link to know the format
https://stackoverflow.com/questions/33297172/boto3-error-botocore-exceptions-nocredentialserror-unable-to-locate-credential

#### Step 4:

Create a table named "Movies" in your DynamoDB account

#### Step 5:

Set your region environment variable.

export AWS_DEFAULT_REGION=us-east-2

#### Step 6:

Use tmux or open four separate terminals to simulate Zookeeper, Kafka Consumer instance, Producer and Consumer for the kafka cluster.

sudo ~/kafka/bin/zookeeper-server-start.sh ~/kafka/config/zookeeper.properties

sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties

python3 ~/kafka_netflix_project/consumer.py

python3 ~/kafka_netflix_project/sendEvents.py
