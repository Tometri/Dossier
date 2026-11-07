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

The first phase in which the dev team plans initial parts of the dev project. The team conducts threat analysis to determine the types of threats that could create problems for the project. They then plan the type of security scans, tools, and tests to be used throughout the lifecycle. Team members are issued identity and access managements (IAM) roles and permissions to ensure the correct access is granted to the correct people.

#### Code

In this phase, the software artifacts outlined in the plan phase are translated into source code. In DevSecOps culture, devs incorporate safe coding practices, like implementing code reviews and following secure code design practices. Dev tools use automation to compile code and integrate security features. Tools might include plugins that monitor for bugs or policy/compliance requirements. Devs should use automation within ther existing tools to streamline receiving security scan reports directly.

#### Build

In the build phase, the software starts taking a more structured form, while automated tools build artifacts and services from the source code. While the application is being built, the DevSecOps team incorporates automated security elements like vulnerability checks and security scans.

#### Test

Once the software application is built, the lifecycle moves into the test phase. During this phase, the software goes through several rounds of both manual and automated testing to ensure its build integrity. Tests assess software features ranging from integration and system capabilities, to functions and performance.

#### Release

During this phase, the configuration environment is evaluated against automated security checks to determine readiness for the production environment. The source code and software artifacts are reviewed and receive final sign offs. Once the config has met all requirements, it's ready to be released in the deploy phase.

#### Deploy

In this phase, the application goes live. Automations push the software into production to end users.

#### Operate

After the software is deployed, the operate phase monitors the deployment for any event or alert relating to functionality and vulnerabilities that need patching. A continous feedback loop of the software's performance keeps operations, development, and security teams up to date and consistent.

## Software Pipelines and Google's Cloud Build

### Software Pipelines

A software pipeline is a process that uses automation and tools to facilitate movement through each phase of the software dev lifecycle. Software pipelines are useful because they enable developers to release changes quickly.

Automation plays a critical role in a software pipelines. First, automation ensures consistency. Software in the pipeline is less prone to human error when tasks like security and functionality testing are automated. Second, testing is incorporated throughout the software development lifecycle, instead as being saved as a final step. This practice supports shifting left, or implementing security checks and practices at the beginning and throughout each phase of the software development lifecycle.

### CI/CD Pipelines

Continous Integration/Continous Delivery (CI/CD) pipeline is a commonly used software pipeline. CI/CD is a process DevSecOps teams use to create software and automate updates. Continous Integration iw when devs continously create and update code that's uploaded into a shared repository. Continous Delivery releases software builds into a testing enviornment. CD also stands for Continous Deployment, which automatically deploys builds into a production environment in real time. This means when devs finish an update, the update is released to end users immediately.

### Security in CI/CD

CICD pipelines support integrated and automated security testing. First the apps source code is uploaded to a shared repo. Uploading triggers a build, triggering a build is when the code starts taking shape as an actual application. At this stage, the build becomes an image. With the image created, automated scans check for vulnerabilities and policy violations. The image continues into the image/artifact repository if it passes this round of security tests.

With the images in the repo, pre-set identity and access management permissions ensure only authorized users are able to access the build image when needed. Automated vulnerability scans make sure the image is secure. If a scan detects a vulnerability, automation triggers a patch and redeploys the image. The redeployed image then goes through another scan.

Finally, automation enables only privileged service accounts access to the deployed builds. Service accounts are identities that are not tied to human users, but are used by an application, virtual machine, or service. They're also granted specific IAM permissions to provide more granular control over the builds. With access limited to service accounts, the builds are less susceptible to human error.

## Google's Cloud Build

Cloud Build is a google serverless service that helps build and protect software. Users can integrate code from cloud repos or storage and create builds for applications. These builds can result in artifacts like container images.

## Software Delivery Shield

SDS is a fully managed solution that strengthens software supply chain security in each stage of the software development lifecycle. It is a combination of google's best practice for securing software development, dashboards in the google cloud console that alert to the security health of resources, and a comparison of supply chain security to SLSA's guidelines.

The software supply chain has many elements that are crucial to secure. SDS supports shifting left by integrating best practices and trusted software packages throughout the software pipeline.

## Terraform as an IaC Tool

Infrastructure as code (IaC) is the practice of provisioning and managing infrastructure using reusable
