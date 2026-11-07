# PowerShell

Start from cli with pwsh.exe

## A Scripting Language

Commands provide PS main functionality; cmdlets, functions, filters, scripts, applications, configurations, and workflows.
Cmdlets use veb-noun naming convention (Get-Command cmdlet lists all cmdlets and functions registered in the command shell).
Microsoft server apps and cloud services provide specialized cmdlets to manage the services. Some features are only managed via PS.

## Configuration management framework

PS incorporates PowerShell Desired State Configuration (DSC) management framework. This framework enables you to manager enterprise infrastructure with code to help with:

- Using delcarative configurations and repeatable scripts for repeatable deployments.
- Enforcing config settings and identifying when config drift takes place from standard requirements.
- Deploying config settings using push or pull models.

## Hosts

Windows PowerShell Console
Windows PowerShell Integrated Scripting Environment (ISE)

Console is similar to the CLI, the console provides the broadest Windows PS functionality
The ISE is a Windows Presentation Foundation (WPF) app that provides rich editing capabilities

## ExecutionPolicy

The execution policy in PS minimizes the possibility of a user unintentionally running PS scripts. To identify the effective execution policy run:

``` PowerShell
Get-ExecutionPolicy
```

You can configure the following policy settings:

- AllSigned, limits script execution on all signed scripts
- Bypass, nothing is blocked
- Default, sets default policy
- RemoteSigned, default execution policy for windows server computers
- Restricted, default execution policy for windows client computers
- Unrestricted, default policy for non-windows computers (can't be changed)
- Undefined, indicates a policy is not set

To change execution policy:

``` PowerShell
Set-ExecutionPolicy -ExecutionPolicy <PolicyName>
```

## Cmdlets

There are thousands of PS cmdlets. Since it is impossible to remember them all, they use a common format that helps predict a cmdlet's name and syntax.

### Cmdlet Verbs

The verb portion of a cmdlet indicates what the cmdlet does.

Common Verbs:

- Get, retrieve a resource (file, user, etc.)
- Set, changes data associated with a resource (file, user property)
- New, creates a resource (file,user)
- Add, adds a resource to a container of multiple resources
- Remove, deletes a resource from a container of multiple resources

### Cmdlet Nouns

The noun portion of a cmdlet name indicates what kinds of resources or objects the cmdlet affects. All cmdlets operating on the same resource should use the same noun.