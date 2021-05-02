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

Use tmux or open four separate terminals to simulate Zookeeper, Kafka Consumer instance, Producer and Consumer for the kafka cluster.

~/bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
python ./sendEvents.py
python ./consumer.py

