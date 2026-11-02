# Hierarchy Overview

## Documents

Documents are the smallest unit in MongoDB.

They typically store information about an object and any of its related metadata.

Documents store data in field-value pairs. The values can be a variety of data types, including strings, numbers, dates, arrays, objects, and more.

## Collections

A collection is a group of documents that typically correspond to an entity in the data model.

MongoDB's flexible data model allows users to model collections based on the user's applications needs, supporting multiple entities and documents of different shapes.

## DataBase

A group of collections is referred to as a database in the context of MongoDB architecture.

## Nodes

A node is a single instance of MongoDB, whether it be running on a physical machine, a virtual machine, or within a container.

## Clusters

A cluster is a group of MongoDB nodes. There are two main types: Sharded and replica sets.

### Replica Sets

Replica sets achieve high availability through replication

### Sharded

Sharded clusters support scaling through a partitioning process called sharding

## CAP Theorem

The CAP theorem states that in a distributed system it's impossible to simutaneously guarantee consistency, availability, and partition tolerance.

Consistency meas that every read should have updated data from the most recent write or give an error, ensuring that all nodes in the system return all the same data at the same time.

Availability is met when every request, read or write, receives a response, even if it may not be the most recent or correct data.

Partition Tolerance is where the system continues to function despite communication breakdowns between nodes or partitions.

A distributed system can only achieve two of these three at any given time.

MongoDB supports partition tolerance via replication and sharding, meaning that users can manage the balance between consistency and availability.

## Replication

Replication is the process of storing multiple copies of data and keeping them synchronized across multiple nodes to provide redundancy.Mongo uses replica sets to perform replication.

### Replica Sets

Replica sets are a group of mongod instances maintaining the same data set. Mongod is the primary daemon process for the MongoDB database system. It handles data requests, manages data access, and performs background management operations.

## Read and Write

Data consistency is manged through Read and Write concerns.

Read concern controls the consistency and isolaton of the data read from replica sets or sharded clusters.

Write concern dictates the number of replica set members that must confirm a write operation for it to be considered successful.

Together, read and write concerns allow users to balance performance, availability, and consistency according to needs.

## Partition Tolerance and Scaling

With sharding, you partition/shard data in mongo across multiple nodes.

Each shard contains a subset of the sharded data. Together shards make up a single logical database, or sharded cluster.

Sharding provides horizontal scalability. As the dataset growsm more shards can be added to distribute the data load, ensuring the database continues to perform well.




