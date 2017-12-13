Patient Registration Scenarios
==============================

Create a new patient, search by name & validate patient details
---------------------------------------------------------------

tags: regression, sanity

* On the login page
* Login to the application
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test New |Patient |أل             |حسن             |Male  |20 |Amman      |Jordan |+9898989898 |English        |Egyptian    |

* Save Patient
* Verify the patient details
* Click on search patient link
* Search previously created patient with patient name
* Verify previous patient details is listed in search result
* Click on previous patient id link from search results
* Verify the patient details
* Logout the user

Create Patient Under Age 18 and Fill Legal Rep
----------------------------------------------

tags: regression, sanity

* On the login page
* Login with username "BAHMNI_GAUGE_OPD_REGISTER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on registration app
* Verify Create New button is displayed
* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Albert   |Hassan  |أل             |حسن             |Male  |12 |Amman      |Jordan |+9898989898 |English        |Egyptian    |

* Enter Legal Rep Details 

   |legalRepFullNameEnglish|legalRepFullNameArabic|legalRepRelationWithPatient|legalRepGender|legalRepNationality|
   |-----------------------|----------------------|---------------------------|--------------|-------------------|
   |Newton                 |حسن                   |Brother                    |Male          |Egyptian           |

* Save Patient and refresh page
* Verify Legal Rep Details after Save

Create Patient And Verify Legal Rep Same As Caretaker
-----------------------------------------------------

tags: regression, sanity

* On the login page
* Login with username "BAHMNI_GAUGE_OPD_REGISTER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Albert   |Hassan  |أل             |حسن             |Male  |12 |Amman      |Jordan |+9898989898 |English        |Egyptian    |

* Enter Patient Details 

   |isCareTakerRequiredCheckBox|
   |---------------------------|
   |True                       |

* Enter Caretaker Details 

   |caretakerNameEnglish|caretakerNameArabic|caretakerGender|caretakerNationality|legalRepalsoCaretaker|
   |--------------------|-------------------|---------------|--------------------|---------------------|
   |Shruthi Hassan      |سن                 |Female         |Iraqi               |Yes                  |

* Verify Legal Rep Values for autocomplete
* Save Patient and refresh page
* Verify caretaker details after save

Create Patient and Fill ID Documents
------------------------------------

tags: regression, sanity

* On the login page
* Login with username "BAHMNI_GAUGE_OPD_REGISTER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Albert   |Hassan  |أل             |حسن             |Male  |12 |Amman      |Jordan |+9898989898 |English        |Egyptian    |

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
