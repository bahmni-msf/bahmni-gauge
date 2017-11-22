Roles and Privileges - Registration Read and Registration Write
===============================================================

   |username|
   |--------|
   |eman_f  |
   |majdi_s |
   |nabil_j |
   |weaam_a |

Login with the user which have Registration role (Registration-Read and Registration-Write) assigned and register a new patient
-------------------------------------------------------------------------------------------------------------------------------

tags: regression, sanity

* On the login page
* Login with user <username> and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Verify only the following application is available 

   |Application~ID(tagName)|Is Available|
   |-----------------------|------------|
   |Registration           |true        |

* Click on registration app
* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Albert   |Hassan  |أل             |حسن             |Male  |12 |Amman      |Jordan |+9898989898 |English        |Egyptian    |

Create Patient Under Age 18 and Fill Legal Rep
* Enter Legal Rep Details 

   |legalRepFullNameEnglish|legalRepFullNameArabic|legalRepRelationWithPatient|legalRepGender|legalRepNationality|
   |-----------------------|----------------------|---------------------------|--------------|-------------------|
   |Newton                 |حسن                   |Brother                    |Male          |Egyptian           |

* Save Patient and refresh page
* Verify Legal Rep Details after Save

Create Patient And Verify Legal Rep Same As Caretaker
* Enter Patient Details 

   |isCareTakerRequiredCheckBox|
   |---------------------------|
   |True                       |

* Enter Caretaker Details 

   |caretakerNameEnglish|caretakerNameArabic|caretakerGender|caretakerNationality|legalRepalsoCaretaker|
   |--------------------|-------------------|---------------|--------------------|---------------------|
   |Shruthi Hassan      |سن                 |Female         |Iraqi               |Yes                  |

* Verify Legal Rep Values for autocomplete

Create Patient and Fill ID Documents
* Enter Patient Details 

   |statusofOfficialIDdocuments|
   |---------------------------|
   |Received                   |

* Enter ID Document Details 

   |id1DocumentType|id1DocNumber|id1FullNameEnglish|
   |---------------|------------|------------------|
   |Passport       |1828DE0S    |Amitb Bachan      |

* Save Patient and refresh page
* Verify patient id documents after save
* Verify caretaker details after save
* Start "First Stage Validation" visit and navigate to Programs page
