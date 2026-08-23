# Cloud Computing

## Cloud Deployment Types

### Cloud-Based

Existing resources can be migrated to the cloud, you can design and build new apps within the cloud, or use a combination of both.

### On-Premises

On-prem deployment uses virtualization and resource management tools does not provide many of the cloud benefits. However, it is able to provide dedicated resources and low latency 

### Hybrid

In a hybrid deployment, cloud and on-prem resources work together.

## Key Benefits of AWS Cloud

- Variable Expense: Expenses are aligned with actual usage.
- Scale: The vast infrastructure of AWS can result in lower costs.
- Dynamic Scaling: Cloud resources can be scaled up or down based on real time demand.
- Speed and Agility: Businesses can rapidly deploy apps and services with the cloud.
- Cloud eliminates the need to invest in infrastructure, reducing money spent on utilities and infrastructure.

## Intro to AWS Global Infrastructure

Global Infrastructure consists of physical locations around the world that contain groups of data centers.

AWS Regions are physical locations around the world that contain groups of data centers. These groups are called availability zones. Each AWS region consists of a minimum of three physically separate availability zones within a geographic region.

## AWS Shared Responsibility Model

Customer Responsibilities:

Customers are responsible for managing security requirements for their data, including whicb data they store on AWS and who has access to that data. Customers also control how access to the data is granted, managed, and revoked.

Shared Responsibilities:

Depending on the service used, responsibilities might shift between customers and AWS. Components such as platform, application, OS, network, firewall config, and etc may shift between who is responsible.

AWS Responsibilities:

AWS is responsible for protecting the infrastructure that runs all services offered in AWS cloud, including hardware, software, networking, and facilities that run AWS cloud services.