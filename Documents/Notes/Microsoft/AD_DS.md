# Active Directory Domain Services (AD DS)

AD DS and related services form the foundation for enterprise networks that run Windows OS. The AD DS database is the central store for all of the domain objects, such as user accounts, computer accounts, and groups. AD DS provides a searchable, heirarchical directory and a method for applying configuration and security settings for objects in an enterprise.

AD DS contains both logical and physical components which work together so that you can manage infrastructure efficiently. You can also use AD DS to perform actions such as:

- Installing, configuring and updating apps.
- Managing the security infrastructure.
- Enabling Remote Access Service and DirectAccess
- Issuing and managing digital certificates.

## Logical Components

- Partition: A portion of the AD DS database.
- Schema: A schema is the set of definitions of the object types and attributes that you use to define the objects created in AD DS.
- Domain: A domain is a logical administrative container for objects such as users and computers. A domain maps to a specific partition and you can organize the domain with parent-child relationships to other domains.
- Domain tree: A heirarchical collection of domains that share a common root domain and a contigous Domain Name System (DNS) namespace.
- Forest: a collection of one or more domains that have a common AD DS root, a common schema, and a common global catalog.
- OU: An OU is a container object for users, groups, and computers that provides a framework for delegating administrative rights and administration by linking Group Policy Objects (GPOs).
- Container: An object that provides an organizational framework for use in AD DS. You can use default containers, or create custom containers. You cannot link GPOs to containers.

## Physical Components

- Domain Controller: A domain controller contains a copy of the AD DS database. For most operations, each domain controller can process changes and replicate the changes to all other domain controllers in the domain.
- Data Store: A copy of the data store exists on each domain controller. The AD DS database uses Microsoft Jet database technology and stores the directory information in the Ntds.dit file and associated log files. The C:\Windows\NTDS folder stores these files by default.
- Global Catalog Server: A global catalog server is a domain controller that hosts the global catalog, which is a partial, read-only copy of all the objects in a multiple-domain forest. A global catalog speeds up searches for objects that might be stored on domain controllers in a different domain in the forest.
- Read-Only Domain Controller (RODC): An RODC is a special read only installation of AD DS. RODCs are common in branch offices where physical security isn't optimal, IT support is less advanced than in the main corporate centers, or line-of-business applications need to run on domain controllers.
- Site: A site is a container for AD DS objects, such as computers and services that are specific to a physical location. This is in comparison to a domain, which represents the logical structure of objects, such as users and groups, in addition to computers.
- Subnet: A subnet is a portion of the network IP addresses of an organization assigned to computers in a site. A site can have more than one subnet.

## Users, Groups, and Computers

In AD DS, you must provide all users that require access to network resources with a user account. With this user account, users can authenticate to the AD DS domain and access network resources.

In a Windows Server, a user account is an object that contains all the information that defines a user. A user account includes:

- The username
- A user password
- Group memberships

A user account also contains settings that you can configure based on organizational requirements.

The username and password of a user account serve as the sign-in credentials. A user object also includes several other attributes that describe and manage the user. You can use the following to create and manage user objects in AD DS:

- Active Directory Administrative Center
- Active Directory Users and Computers
- Windows Admin Center
- Windows Powershell
- The 'dsadd' command-line tool

### Managed Service Accounts

Many apps contain services that you install on the server that hosts the program. These services typically run at server startup or are triggered by other events. Services often run in the background and don't require any user interaction. For a service to start up and authenticate, you use a service account. A service account might be an account that is local to the computer, such as the built-in Local Service, Network Service, or Local System accounts. You also can configure a service account to use a domain-based account located in AD DS.

Windows Server supports an AD DS object, named a managed service account, which you use to facilitate service-account management. A managed service account is an AD DS object class that enables:

- Simplified password management
- Simplified SPN management

### Group Managed Service Accounts

Group Managed Service Accounts (gMSA) enable you to extend the capabilities of standard managed service accounts to more than one server in your domain. In server farm scenarios with Network Load Balancing (NLB) clusters or IIS servers, there often is a need to run system or program services under the same service account. Standard managed service accounts can't provide managed service account functionality to services that are running on more than one server. By gMSA, you can configure multiple servers to use the same managed service account and still retain the benefits that managed service accounts provide, like automatic password maintenance and simplified SPN management.

### Delegated Managed Service Accounts

Windows Server 2025 introduces a new type of service account called the Delegated Managed Service Account (dMSA). The dMSA account type enables users to transition from traditional service accounts to machine accounts that have managed and fully randomized keys, while also disabling the original service account passwords. Authentication for dMSA is linked to the device identity, which means that only specified machine identities mapped in AD can access the account. By using dMSA, users can prevent the common issue of credential harvesting using a compromised account that is associated with traditional service accounts.

### gMSA vs. dMSA

dMSAs and gMSAs are two types of managed service accounts that are used to run services and applications in Windows Server. A dMSA is managed by an administrator and is used to run a service or application on a specific server. A gMSA is managed by AD and is used to run a service or application on multiple servers.

### Group Types

- Security: Security groups are security-enabled, and you use them to assign permissions to various resources. You can use security groups in permission entries in access control lists (ACLs) to help control security for resource access. If you want to use a group to manage security, it must be a security group.
- Distribution: Email applications typically use distribution groups, which aren't security-enabled. You also can use security groups as a means of distribution for email applications.

### Group Scopes

The scope of a group determines both the range of a group's abilities or permissions and the group membership. There are four group scopes:

- Local: You use this type of group for standalone servers or workstations, on domain-member servers that aren't domain controllers, or on domain-member workstations. Local groups are available only on the computer where they exist. The important characteristics of a local group are:
  - You can assign abilities and permissions on local resources only, meaning on the local computer.
  - Members can be from anywhere in the AD DS forest.
- Domain-Local: You use this type of group primarily to manage access to resources or to assign management rights and responsibilities. Domain-local groups exist on domain controllers in an AD DS domain, and so, the group’s scope is local to the domain in which it resides. The important characteristics of domain-local groups are:
  - You can assign abilities and permissions on domain-local resources only, which means on all computers in the local domain.
  - Members can be from anywhere in the AD DS forest.
- Global: You use this type of group primarily to consolidate users who have similar characteristics. For example, you might use global groups to join users who are part of a department or a geographic location. The important characteristics of global groups are:
  - You can assign abilities and permissions anywhere in the forest.
  - Members can be from the local domain only and can include users, computers, and global groups from the local domain.
- Universal: You use this type of group most often in multidomain networks because it combines the characteristics of both domain-local groups and global groups. Specifically, the important characteristics of universal groups are:
  - You can assign abilities and permissions anywhere in the forest similar to how you assign them for global groups.
  - Members can be from anywhere in the AD DS forest.

### Computer Objects

Computers:

- They have an account with a sign-in name and password that Windows changes automatically on a periodic basis.
- They authenticate with the domain.
- They can belong to groups and have access to resources, and you can configure them by using Group Policy.

A computer account begins its lifecycle when you create the computer object and join it to your domain. After you join the computer account to your domain, day-to-day administrative tasks include:

- Configuring computer properties.
- Moving the computer between OUs.
- Managing the computer itself.
- Renaming, resetting, disabling, enabling, and eventually deleting the computer object.

### Computers Container

Before you create a computer object in AD DS, you must have a place to put it. The Computers container is a built-in container in an AD DS domain. This container is the default location for the computer accounts when a computer joins the domain.

This container isn't an OU. Instead, it's an object of the Container class. Its common name is CN=Computers. There are subtle but important differences between a container and an OU. You can't create an OU within a container, so you can't subdivide the Computers container. You also can't link a Group Policy Object to a container. Therefore, we recommend that you create custom OUs to host computer objects, instead of using the Computers container.

## AD DS Forests and Domains

An AD DS forest is a collection of one or more AD DS trees that contain one or more AD DS domains. Domains in a forest share:

- A common root.
- A common schema.
- A global catalog.

An AD DS domain is a logical administrative container for objects such as:

- Users
- Groups
- Computers

### AD DS Forests

A forest is a top-level container in AD DS. Each forest is a collection of one or more domain trees that share a common directory schema and a global catalog. A domain tree is a collection of one or more domains that share a contiguous namespace. The forest root domain is the first domain that you create in the forest.

The forest root domain contains objects that don't exist in other domains in the forest. Because you always create these objects on the first domain controller, a forest can consist of as few as one domain with a single domain controller, or it can consist of several domains across multiple domain trees.

The following objects exist in the forest root domain:

- The schema master role.
- The domain naming master role.
- The Enterprise Admins group.
- The Schema Admins group.

>[!NOTE]
>Although the schema and domain naming master roles are assigned initially in the root domain on the first domain controller you create, you can move them to other domain controllers anywhere in the forest.

An AD DS forest is often described as:

- A security boundary. By default, no users from outside the forest can access any resources inside the forest. In addition, all the domains in a forest automatically trust the other domains in the forest. This makes it easy to enable access to resources for all the users in a forest, regardless of the domain to which they belong.
- A replication boundary. An AD DS forest is the replication boundary for the configuration and schema partitions in the AD DS database. Therefore, organizations that want to deploy applications with incompatible schemas must deploy additional forests. The forest is also the replication boundary for the global catalog. The global catalog makes it possible to find objects from any domain in the forest.

>[!TIP]
>Typically, an organization creates only one forest.

The following objects exist in each domain (including the forest root):

- The RID master role.
- The Infrastructure master role.
- The PDC emulator master role.
- The Domain Admins group.

### AD DS Domains

An AD DS domain is a logical container for managing user, computer, group, and other objects. The AD DS database stores all domain objects, and each domain controller stores a copy of the database.

The most commonly used objects are described in the following table:

Object | Description
 -|-
User Accounts | User accounts contain information about users, including the information required to authenticate a user during the sign-in process and build the user's access token.
Computer Accounts | Each domain-joined computer has an account in AD DS. You can use computer accounts for domain-joined computers in the same way that you use user accounts for users.
Groups | Groups organize users or computers to simplify the management of permissions and Group Policy Objects in the domain.

>[!NOTE]
>AD DS allows a single domain to contain nearly two billion objects. This means that most organizations need only deploy a single domain.

An AD DS domain is often described as:

- A replication boundary. When you make changes to any object in the domain, the domain controller where the change occurred replicates that change to all other domain controllers in the domain. If multiple domains exist in the forest, only subsets of the changes replicate to other domains. AD DS uses a multi-master replication model that allows every domain controller to make changes to objects in the domain.
- An administrative unit. The AD DS domain contains an Administrator account and a Domain Admins group. By default, the Administrator account is a member of the Domain Admins group, and the Domain Admins group is a member of every local Administrators group of domain-joined computers. Also, by default, the Domain Admins group members have full control over every object in the domain.

>[!NOTE]
>The Administrator account in the forest root domain has additional rights.

An AD DS domain provides:

- Authentication. Whenever a domain-joined computer starts or a user signs in to a domain-joined computer, AD DS authenticates it. Authentication verifies that computer or user has the proper identity in AD DS by verifying its credentials.
- Authorization. Windows uses authorization and access control technologies to determine whether to allow authenticated users to access resources.

>[!TIP]
>Organizations with decentralized administrative structures or multiple locations might consider implementing multiple domains in the same forest to accommodate their administrative needs.

### Trust Relationships

AD DS trusts enable access to resources in a complex AD DS environment. When you deploy a single domain, you can easily grant access to resources within the domain to users and groups from the domain. When you implement multiple domains or forests, you should ensure that the appropriate trusts are in place to enable the same access to resources.

In a multiple-domain AD DS forest, two-way transitive trust relationships generate automatically between AD DS domains so that a path of trust exists between all the AD DS domains.

>[!NOTE]
>The trusts that create automatically in the forest are all transitive trusts, which means that if domain A trusts domain B, and domain B trusts domain C, then domain A trusts domain C.

Trust Type | Description | Direction | Description
 -|-|-|- 
Parent and Child | Transitive | Two-way |When you add a new AD DS domain to an existing AD DS tree, you create new parent and child trusts.
Tree-root | Transitive | Two-way | When you create a new AD DS tree in an existing AD DS forest, you automatically create a new tree-root trust.
External | Nontransitive | One-way or two-way | External trusts enable resource access with a Windows NT 4.0 domain or an AD DS domain in another forest. You also can set these up to provide a framework for a migration.
Realm | Transitie or nontransitive | One-way or two-way| Realm trusts establish an authentication path between a Windows Server AD DS domain and a Kerberos version 5 (v5) protocol realm that implements by using a directory service other than AD DS.
Forest (complete or selective) | Transitive | One-way or two-way | Trusts between AD DS forests allow two forests to share resources.
Shortcut | Nontransitive | One-way or two-way | Configure shortcut trusts to reduce the time taken to authenticate between AD DS domains that are in different parts of an AD DS forest. No shortcut trusts exist by default, and an administrator must create them if they're required.

When you set up trusts between domains within the same forest, across forests, or with an external realm, Windows Server creates a trusted domain object to store the trusts' information, such as transitivity and type, in AD DS. Windows Server stores this trusted domain object in the System container in AD DS.

## Organizational Units (OUs)

An OU is a container object within a domain that you can use to consolidate users, computers, groups, and other objects. You can link Group Policy Objects (GPOs) directly to an OU to manage the users and computers contained in the OU. You can also assign an OU manager and associate a COM+ partition with an OU.

You can create new OUs in AD DS by using:

- Active Directory Administrative Center.
- Active Directory Users and Computers.
- Windows Admin Center.
- Windows PowerShell with the Active Directory PowerShell module.

There are two reasons to create an OU:

- To consolidate objects to make it easier to manage them by applying GPOs to the collective. When you assign GPOs to an OU, the settings apply to all the objects within the OU. GPOs are policies that administrators create to manage and configure settings for computers or users. You deploy the GPOs by linking them to OUs, domains, or sites.
- To delegate administrative control of objects within the OU. You can assign management permissions on an OU, thereby delegating control of that OU to a user or a group within AD DS, in addition to the Domain Admins group.

You can use OUs to represent the hierarchical, logical structures within your organization. For example, you can create OUs that represent the departments within your organization, the geographic regions within your organization, or a combination of both departmental and geographic regions. You can use OUs to manage the configuration and use of user, group, and computer accounts based on your organizational model.

### Generic Containers

AD DS has several built-in containers, or generic containers, such as Users and Computers. These containers store system objects or function as the default parent objects to new objects that you create. Don't confuse these generic container objects with OUs. The primary difference between OUs and containers is the management capabilities. Containers have limited management capabilities. For example, you can't apply a GPO directly to a container.

Installing AD DS creates the Domain Controllers OU and several generic container objects by default. AD DS primarily uses some of these default objects, which are also hidden by default. The following objects are displayed by default:

- Domain. The top level of the domain organizational hierarchy.
- Builtin container. A container that stores several default groups.
- Computers container. The default location for new computer accounts that you create in the domain.
- Foreign Security Principals container. The default location for trusted objects from domains outside the local AD DS domain that you add to a group in the local AD DS domain.
- Managed Service Accounts container. The default location for managed service accounts. AD DS provides automatic password management in managed service accounts.
- Users container. The default location for new user accounts and groups that you create in the domain. The Users container also holds the administrator, the guest accounts for the domain, and some default groups.
- Domain Controllers OU. The default location for domain controllers' computer accounts. This is the only OU that is present in a new installation of AD DS.

### Hierarchical Design

The administrative needs of the organization dictate the design of an OU hierarchy. Geographic, functional, resource, or user classifications could all influence the design. Whatever the order, the hierarchy should make it possible to administer AD DS resources as effectively and flexibly as possible. For example, if you need to configure all IT administrators’ computers in a certain way, you can group all the computers in an OU and then assign a GPO to manage those computers.

You also can create OUs within other OUs. For example, your organization might have multiple offices, each with its own IT administrator who is responsible for managing user and computer accounts. In addition, each office might have different departments with different computer-configuration requirements. In this situation, you can create an OU for each office, and then within each of those OUs, create an OU for the IT administrators and an OU for each of the other departments.

Although there's no limit to the number of levels in your OU structure, limit your OU structure to a depth of no more than 10 levels to ensure manageability. Most organizations use five levels or fewer to simplify administration.

## Active Directory Administrative Center

The Active Directory Administrative Center provides a GUI that is based on Windows PowerShell. This enhanced interface allows you to perform AD DS object management by using task-oriented navigation, and it replaces the functionality of Active Directory Users and Computers.

Tasks that you can perform by using the Active Directory Administrative Center include:

- Creating and managing user, computer, and group accounts.
- Creating and managing OUs.
- Connecting to and managing multiple domains within a single instance of the Active Directory Administrative Center.
- Searching and filtering AD DS data by building queries.
- Creating and managing fine-grained password policies.
- Recovering objects from the Active Directory Recycle Bin.
- Managing objects that the Dynamic Access Control feature requires.

## Windows Admin Center

Windows Admin Center is a web-based console that you can use to manage server computers and computers that are running Windows 10. Typically, you use Windows Admin Center to manage servers instead of using Remote Server Administration Tools (RSAT).

Windows Admin Center works with any browser that is compliant with modern standards, and you can install it on computers that run Windows 10 and Windows Server with Desktop Experience.

With a decreasing number of exceptions, Windows Admin Center supports most current Windows Server and Windows 10 administrative functionality. However, Microsoft intends that Windows Admin Center will eventually support all the administrative functionality that is presently available through RSAT.

To use Windows Admin Center, you must first download and install it. You can download Windows Admin Center from the Microsoft download website. After downloading and installing Windows Admin Center, you must enable the appropriate TCP port on the local firewall. On a Windows 10 computer (in standalone mode), this defaults to 6516. On Windows Server (in gateway mode), this defaults to TCP 443. In both cases, you can change it during setup.

## Remote Server Administration Tools

RSAT is a collection of tools which enables you to manage Windows Server roles and features remotely.

You can install the consoles available within RSAT on computers running Windows 10 or on server computers that are running the Server with Desktop Experience option of a Windows Server installation. Until the introduction of Windows Admin Center, RSAT consoles were the primary graphical tools for administering the Windows Server operating system.