Create EndTB Patient Scenarios
===============================


CREATE PATIENT AND VERIFY
-------------------------

Tags: regression, sanity

* On the login page
* Login with username "superman" and password "Admin123"
* Click on registration app
* Click on create new patient link
* Create the following patient
    |EMR_ID_PREFIX|FirstName|Last Name|Gender|Date Of Birth|Address1|nationalIdentificationNumber|
    |EMR|Emily|Bond|Female|20/01/2011|Bilaspur|13892|

* Logout the user


VALIDATE PATIENT CREATE FAILS WITH SAME ID
------------------------------------------

Tags: regression, sanity

* On the login page
* Login with username "superman" and password "Admin123"
* Click on registration app
* Click on create new patient link
* Create the following patient
    |EMR_ID_PREFIX|FirstName|Last Name|Gender|Date Of Birth|Address1|nationalIdentificationNumber|
    |EMR1101614870|John|Smith|Male|20/01/2011|Bilaspur|13892|

* Verify the patient creation fails
* Logout the user

SEARCH PATIENT WITH FILTERS
---------------------------

Tags: regression, sanity

* On the login page
* Login with username "msfuser1" and password "endTB@123"
* Click on registration app
* Click on search patient link
* Search previously created patient with exact identifier
* Ensure that the patient edit page is opened for previously created patient
* Click on search patient link
* Search previously created patient with name
* Select the patient from the search results
* Ensure that the patient edit page is opened for previously created patient
* Logout the user
* Delete the patient

