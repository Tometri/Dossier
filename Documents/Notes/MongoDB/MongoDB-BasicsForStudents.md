# MongoDB Basics for Students

## DataBase Fundamentals

An application font-end is the portion that is interacted with.
To store and serve information to the front-end a database (or multiple) is used to store and serve information.

A database is a place to store data, an organized collection of structured/unstructured information stored on a machine/the cloud.

One of the key differentiators from a flat file, such as a spreadsheet, and a database is that a database includes a Database Management System (DBMS) to handle user requests and data protocols.

A DBMS is software that interacts with end users, apps, and the database to capture and analyze data.

It is a systematic way to perform essential actions often referred to as CRUD (Create/Retrieve/Update/Delete) operations. The DBMS is also responsible for key factors like managing the hardware running the database, managing users and their permissions, maintaining security and data integrity, as well as creating backup processes for recovery in the event of a database failure.

## Types of Databases

A popular way to organize types of databases is to separate them between SQL (Structured Query Language) and NoSQL.

SQL is used to query (search for data) relational databases.

NoSQL refers to Not Only SQL and is sometimes called "non-relational" database.

SQL = Relational, NoSQL = Non-Relational

### Key Value Database

Key Value databases use a unique key (any value in the db) and pair it with a collection of values.

### Key Value Database

Graph databases store information as a collection of nodes and edges. Edges represent relationships between nodes. 

### Column Database

Column databases use columns to store a record rather than rows.

### Document Database

Document databases store data in a single document, using markdown to identify fields and values within the text.

## Schemas and Data Modeling

A schema refers to a set of rules that govern how data is stored and organized in a database.

Data modeling refers to the organization of data within a database and the links between related entities.

Schema dictates the rules, a data model lays out the relationships between data. Data modeling is the concept of how a database is organized, and the schema is the rules that make data conform to the data model.

## Structured, Semi-Structured, and Unstructured Data

### Structured Data

This term refers to data that is highly organized. It is predictable.

### Semi-Structured Data

Data that is organized but doesn't follow a strict data model is semi-structured. There is a pattern to the data, though it isn't always predictable.

### Unstructured Data

The majority of data is not organized or categorized. Videos, image files, text documents, and anything similar is considered unstructured.

## Key Points

Databases: store data to power apps and uses a DBMS to perform essential functions.

SQL vs NoSQL: SQL are based on traditional tabular formats while Not only SQL databases offer more flexibiity in working with modern data.

Schemas: Are the rules governing how data is stored and organized in the database.

## Polymorphic Data

Polymorphic data is data that can take on multiple types within the same structure.

## Flexible Schema

Each data record can have a unique structure. Permits various data types. Unstructured/semi-structured data.

## MongoDB Hierarchy

### Document

Documents are the smallest unit of data in MongoDB. Typically store object and related metadata. Field-value pairs. Data types: strings, numbers, dates, arrays, objects, and more.

Document model: Similar to JavaScript Object Notation (JSON).

### Collection

A collection is a group of documents that correspond to an entity. Can support multiple entities and different shapes.

### Database

A group of collections.

### Node

An individual MongoDB instance.

### Cluster

A group of nodes. There are two cluster types: Replica set and sharded.

## Syntax

```Document Model Syntax (JSON)
{
  "_id": ObjectId(
"5f4f7fef2d4b45b7f11b6d7a"),
  "user_id": "Sean",
  "age": 29,
  "Status": "A"
}
```
This document represents a user, their id in the system, their age, and their status.

The "_id" field holds the ObjectID for the document. The _id is used as a primary key; its value must be unique in the collection, it is immutable, and may be of any type other than an array.

The JSON document syntax uses curly brackets to mark the start and end of the document. The fields (keys) are seperated from their values by a colon. The field values are wrapped in quotation marks, as are string values. Other values, like numbers, are not. Each field-value pair is separated by a comma within the document.

## Key Points 2

Flexibility: The document model has a flexible schema and can work well with structured and semi-structured data.

MongoDB's Hierarchy: Documents>Collections>Database>Node>Cluster

The Golden Rule: Data that is accessed together should be stored together.

Document Model Syntax

Scaling: adjusitng performance of a database using more performant hardware (vertical) or adding additional hardware (horizontal).

Replication: creating redundant nodes to ensurea vailability and protect from data loss in the event of node failure.

CAP Therorem: There is always tradeoff between Consistency, Availability, and Partition Tolerance.

## MongoDB Atlas Key Points

Self-managed vs Fully-managed: fully-managed systems offer a blend of convenience and customization so you can focus on your priorities.

MongoDB Atlas: DBaaS that works on all major cloud providers and supports a rich, modern set of features.

