Create EndTB Patient Scenarios
===============================



CREATE PATIENT AND VERIFY
-------------------------

Tags: sanity

* On the login page
* Login to the application
* Verify Login Page
* Click on registration app
* Click on create new patient link
* Create the following patient

    |prefix|firstName|lastName|gender|dateOfBirth|district|nationalIdentificationNumber|
    |EMR|Super|Woman|Female|20/01/2011|Bilaspur|13892|

* Logout the user


VALIDATE PATIENT CREATE FAILS WITH SAME ID
------------------------------------------

Tags: sanity

* On the login page
* Login to the application
* Verify Login Page
* Click on registration app
* Click on create new patient link
* Create the following patient

    |prefix|firstName|lastName|gender|dateOfBirth|district|nationalIdentificationNumber|
    |EMR|John|Smith|Male|20/01/2011|Bilaspur|13892|

* Click on create new patient link
* Create the following patient with ID as recently created Patient

    |prefix|firstName|lastName|gender|dateOfBirth|district|nationalIdentificationNumber|
    |EMR|John|Smith|Male|20/01/2011|Bilaspur|13892|
* Verify the patient creation fails
* Logout the user





