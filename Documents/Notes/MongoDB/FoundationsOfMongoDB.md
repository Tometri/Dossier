# Foundations

## Distributed Databases

MongoDB, like many non-relational databases, has a distibuted system architecture.

A distributed db is where data is spread across multiple machines, or nodes. Each node may be in a different geographical location.

If one machine fails, the system can still function due to this redundancy.

The distributed system architecture ensures consistent service and reliability, even with a system failure. They can also store data closer to where it's generated or accessed. This reduces latency.

## Document Model

MongoDB stores data in JSON (JavaScript Object Notation) like documents.

JSON is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

A document can represent an entire object or entity.

 All or nearly all information about an object or entity can be contained in a single document, and a group of documents is contained in a collection.

This document model is unique because of its ability to handle polymorphic data and support flexible schemas.

## Polymorphic Data

Polymorphic data refers to data that can take on multiple forms or types within the same context or structure.

MongoDB allows for flexible schemas which allows polymorphic data.

With a flexible schema, each piece of data can have a unique structure, permitting various data types and fields within a single collection.

This is helpful for unstructured/semi-structured data that doesn't fit neatly into a table.

Given this flexibility, MongoDB is well-suited for a number of use-cases.


