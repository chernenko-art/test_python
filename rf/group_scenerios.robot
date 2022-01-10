*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    append to list  ${old_list}  ${group}
    Group List Should Be Equal  ${new_list}  ${old_list}

Delete group
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  get from list  ${old_list}  ${index}
    Delete group  ${group}
    ${new_list}=  Get Group List
    remove values from list  ${old_list}  ${group}
    Group List Should Be Equal  ${new_list}  ${old_list}

Modify group
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  get from list  ${old_list}  ${index}
    Modify group  ${group}
    ${new_list}=  Get Group List
    remove values from list  ${old_list}  ${group}
    ${group}=  get from list  ${new_list}  ${index}
    append to list  ${old_list}  ${group}
    Group List Should Be Equal  ${new_list}  ${old_list}