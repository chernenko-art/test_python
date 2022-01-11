*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get User List
    ${user}=  New User  firstname1  middlename1  lastname1
    Create User  ${user}
    ${new_list}=  Get User List
    append to list  ${old_list}  ${user}
    User List Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get User List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${user}=  get from list  ${old_list}  ${index}
    Delete user  ${user}
    ${new_list}=  Get User List
    remove values from list  ${old_list}  ${user}
    User List Should Be Equal  ${new_list}  ${old_list}

Modofy contact
    ${old_list}=  Get User List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${user}=  get from list  ${old_list}  ${index}
    Modify user  ${user}
    ${new_list}=  Get User List
    remove values from list  ${old_list}  ${user}
    ${user}=  get from list  ${new_list}  ${index}
    append to list  ${old_list}  ${user}
    User List Should Be Equal  ${new_list}  ${old_list}
