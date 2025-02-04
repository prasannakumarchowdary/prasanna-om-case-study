# Assessment 

This assessment consists of 4 parts, and the themes are as follows:

Containers
Infrastructure as Code
Scripting
Extra

They are each designed to asses the capability with the given theme or concept.

Containers -> Docker, Containerisation 

IAC - Terraform, infrastructure mananegment, declaritive configuration code

Scripting -> general scripting automation

Extra -> a (Hopefully) new problem and domain, that will be used to assess novel problem solving, information gathering and synthethis, and execution of new knowledge


Knowledge and tools required to complete:
- Git
- Docker
- Node.js
- One Of: Python, Bash, Ruby, Powershell, etc for scripting

## 1. Scripting

write a script that will take `tfplan.json` file ( A terraform plan file converted to json) and parse it and then determine whether the apply should proceed or not based on the following:

- The plan must only contain `create` or `modify` steps
- the `modify` step must ONLY modify the resource's `tags` attribute and then only the `GitCommitHash` tag
- if anything else is being modified or destroyed the plan must not proceed (Print out the action then must be taken)

Add code to the `script.py` file in the `scripting` folder.
script will be tested agains the `*.tfplan` files in that directory.


## 2. Infrastructure As Code

You have a Terraform configuration that deploys a set of resources using the count meta argument. Currently, you have deployed 5 resources.

You need to delete the "2nd" resource without affecting the other resources.
The count variable is part of the resource naming convention.

How would you go about deleting the "2nd" resource while ensuring that the other resources remain unchanged? Please provide a detailed explanation of the steps you would take and any Terraform features or commands you would use to achieve this. Please add these steps/actiosn to the `steps-to-fix.md` file in the `infrastructure-as-code` folder.

Manually deleting and renaming resources may work but is not the optimal solution.
You must be able to run `terraform apply` at the end and it must report "no changes".

## 3. Containers

Dockerise the express.js app and write a dockercompose file that will spin up and expose the app on port 4567.
Needed Files are in the `express-app` folder.


## 4. Dev/Problem Solving

All of the following actions must be taken in the "wild" directory:

Create a new instance of backstage

https://backstage.io/docs/getting-started/

Create a custom action that will create a new file
the custom action must have an id of "my:custom:action"

https://backstage.io/docs/features/software-templates/writing-custom-actions

add the custom action to the example template in the repo
make sure it is the only action/step in the ecxample template

commit your code to a github repository and give acces to "adamaucamp"
(or make the repo public if you want.)

