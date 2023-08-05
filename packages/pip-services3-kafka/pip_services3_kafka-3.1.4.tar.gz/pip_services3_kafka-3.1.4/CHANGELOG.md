# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> Kafka components for Pip.Services in Python Changelog

## <a name="3.1.3-3.1.4"></a> 3.1.3-3.1.4 (2021-11-10)

### Bug fixes
* Fixed timeout producer publish

### Features
* Added create_queue, delete_queue for KafkaConnection

## <a name="3.1.1-3.1.2"></a> 3.1.1-3.1.2 (2021-11-03)

### Bug fixes
* Added flushing for kafka producer
* Fixed setup file

## <a name="3.1.0"></a> 3.1.0 (2021-11-02)

### Features
* Migrated from kafka-python on confluent_kafka
* Changed seconds on millisecond in timestamps

## <a name="3.0.0"></a> 3.0.0 (2021-09-09)

Initial release

### Features

* Added KafkaMessageQueueFactory component
* Added KafkaConnection component
* Added DefaultKafkaFactory component
* Added KafkaConnectionResolver component
* Added KafkaMessageQueue component

