wget https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
tar -xzf kafka_2.13-2.8.0.tgz
mv kafka_2.13-2.8.0 kafka
echo "PATH=$PATH:~/kafka/bin" >> .bashrc
source ~/.bashrc
sudo apt update
sudo apt -y install openjdk-14-jdk htop
sudo apt -y install python3-dev python3-pip
pip3 install boto3 kafka-python pandas
