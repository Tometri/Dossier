# Google Cloud Cyber Security

## Security Controls

The National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF) can help achieve an improved security posture.

### Identify

Identify highlights the importance of understanding an organization's critical assets and systems, along with their associated risks. Risks include anything that can impact confidentiality, integrity, or availability (CIA), or availability of an asset. Orgs catalog their assets, data, and personally identifiable information (PII). Then, they rank severity of risks to each asset type, and identify gaps in scurity controls.

### Protect

Protective controls shield cloud resources.

### Detect

Detective controls identify potential threats and events. Both physical and logical environments should be monitored to alert for suspicious activities.

### Respond

Responsive controls involve many components, ranging from planning, to improving processes in the event of attacks, to disaster recovery.

### Recover

Recovery controls are important to restore access and performance when failures occur. Replicating resources and backing systems are forms of recovery controls.

## Identity and Access Management (IAM)

IAM controls who has access to what resources.

### Principals

In Google Cloud, you assign permissions and roles to users  or apps called principals. Principals represent a variety of identities, like google or service accounts, groups, or individual users.

### Groups

A group is a collection of principals, like users or applications, that can be grouped together and assigned roles.

### Service Accounts

A service account represents a non-human identity, like an app, service, or virtual machine.

### Federation

Federation is a method of granting external identities access to your cloud environment. Federation is what allows single sign-on (SSO).

## Firewalls for Network Secrity

### Firewalls in the Cloud

Firewalls in the cloud operate similarly to an on premises environment. Firewalls monitor traffic to or from networks, and can restrict specific incoming/outgoing network traffic. In the cloud, firewalls are software based and hosted by Cloud Service Providers (CSPs) They are maintained by the CSP and configured by the customer, and they are scaleable to demand.

### Firewall as a Service (FWaaS)

The FWaaS is a service model for cloud environments. Organizations can adopt FWaaS to help block unauthorized traffic on their network.

## The DevSecOps Lifecycle

DevSecOps supports a "security first" culture, where security shifts left. Shifting left means that security is incorporated at the beginning of the dev process rather than the end. The DevSecOps infinity loop is a common way to portray the dev and ops lifecycle with security intermixed throughout.

### The Seven Phases

#### Plan
#### Code
#### Build
#### Test
#### Release
#### Deploy
#### Operate
