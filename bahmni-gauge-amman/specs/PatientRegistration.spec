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
* Verify search result contains "Test New" in column "Name"
* Verify previous patient details is listed in search result
* Click on previous patient id link from search results
* Verify the patient details
* Logout the user

Create Patient Under Age 18 and Fill Legal Rep
----------------------------------------------

tags: regression

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

Create Patient And Verify Legal Rep Same As Caretaker, Search by Identifier, fetch & validate patient details
-------------------------------------------------------------------------------------------------------------

tags: regression

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
* Click on search patient link
* Search previously created patient with identifier
* Verify the patient details
* Logout the user

Create Patient and Fill ID Documents, Search by Name in Arabic, fetch & validate patient details
------------------------------------------------------------------------------------------------

tags: regression

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
* Click on search patient link
* Search previously created patient with Name in Arabic
* Verify search result contains "أل" in column "Given Name Local"
* Verify previous patient details is listed in search result
* Click on previous patient id link from search results
* Verify the patient details
* Logout the user

Edit patient details, Search by Country, fetch & validate patient details
-------------------------------------------------------------------------

tags: regression

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
* Search previously created patient with Country
* Verify search result contains "Jordan" in column "Country"
* Verify previous patient details is listed in search result
* Click on previous patient id link from search results
* Edit previous patient details 

   |age|phoneNumber1|spokenLanguages|
   |---|------------|---------------|
   |30 |+9898980000 |New Language   |
* Save Patient
* Verify the patient details
* Logout the user

Verify auto generated patient identifier
----------------------------------------

tags: regression

* On the login page
* Login with username "BAHMNI_GAUGE_OPD_REGISTER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on registration app
* Click on create new patient link
* Enter Patient Details 

   |firstName |lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |----------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test Egypt|Patient |أل             |حسن             |Male  |20 |Red Sea    |Egypt  |+9898989898 |English        |Egyptian    |

* Save Patient
* Verify patient identifier begins with nationality code "EG" and ends with gender code "M"

* Click on create new patient link
* Enter Patient Details 

   |firstName|lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |---------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test Iraq|Patient |أل             |حسن             |Female|25 |Najaf      |Iraq   |+9898989898 |English        |Iraqi       |

* Save Patient
* Verify patient identifier begins with nationality code "IQ" and ends with gender code "F"

* Click on create new patient link
* Enter Patient Details 

   |firstName     |lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |--------------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test Palestine|Patient |أل             |حسن             |Male  |20 |Murzuq     |Libya  |+9898989898 |English        |Palestinian |

* Save Patient
* Verify patient identifier begins with nationality code "PS" and ends with gender code "M"

* Click on create new patient link
* Enter Patient Details 

   |firstName  |lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |-----------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test Jordan|Patient |أل             |حسن             |Male  |20 |Amman      |Jordan |+9898989898 |English        |Jordanian   |

* Save Patient
* Verify patient identifier begins with nationality code "JO" and ends with gender code "M"

* Click on create new patient link
* Enter Patient Details 

   |firstName   |lastName|givenNameArabic|familyNameArabic|gender|age|governorate      |country|phoneNumber1|spokenLanguages|nationality1|
   |------------|--------|---------------|----------------|------|---|-----------------|-------|------------|---------------|------------|
   |Test Lebanon|Patient |أل             |حسن             |Male  |20 |Baalbek-El-Hermel|Lebanon|+9898989898 |English        |Lebanese    |

* Save Patient
* Verify patient identifier begins with nationality code "LB" and ends with gender code "M"

* Click on create new patient link
* Enter Patient Details 

   |firstName |lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |----------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test Libya|Patient |أل             |حسن             |Male  |20 |Darnah     |Libya  |+9898989898 |English        |Libyan      |

* Save Patient
* Verify patient identifier begins with nationality code "LY" and ends with gender code "M"

* Click on create new patient link
* Enter Patient Details 

   |firstName |lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |----------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test Sudan|Patient |أل             |حسن             |Male  |20 |Sanliurfa  |Turkey |+9898989898 |English        |Sudan       |

* Save Patient
* Verify patient identifier begins with nationality code "SD" and ends with gender code "M"

* Click on create new patient link
* Enter Patient Details 

   |firstName        |lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country     |phoneNumber1|spokenLanguages|nationality1 |
   |-----------------|--------|---------------|----------------|------|---|-----------|------------|------------|---------------|-------------|
   |Test Saudi Arabia|Patient |أل             |حسن             |Male  |20 |Baha       |Saudi Arabia|+9898989898 |English        |Saudi Arabian|

* Save Patient
* Verify patient identifier begins with nationality code "SA" and ends with gender code "M"

* Click on create new patient link
* Enter Patient Details 

   |firstName |lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |----------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test Yemen|Patient |أل             |حسن             |Male  |20 |Marib      |Yemen  |+9898989898 |English        |Yemeni      |

* Save Patient
* Verify patient identifier begins with nationality code "YE" and ends with gender code "M"

* Click on create new patient link
* Enter Patient Details 

   |firstName |lastName|givenNameArabic|familyNameArabic|gender|age|governorate|country|phoneNumber1|spokenLanguages|nationality1|
   |----------|--------|---------------|----------------|------|---|-----------|-------|------------|---------------|------------|
   |Test Syria|Patient |أل             |حسن             |Male  |20 |Hama       |Syria  |+9898989898 |English        |Syrian      |

* Save Patient
* Verify patient identifier begins with nationality code "SY" and ends with gender code "M"

Verify visibility of sections in registration page
--------------------------------------------------

tags: regression

* On the login page
* Login with username "BAHMNI_GAUGE_OPD_REGISTER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on registration app
* Click on create new patient link
* Verify below sections are visible by default in Registration page 

   |SECTION                    |
   |---------------------------|
   |NEW PATIENT                |
   |Camp Address               |
   |Patient Contact Details    |
   |Other Information          |
   |Emergency Contact Details  |
   |Patient Arrival Information|
   |Relationships              |

* Verify below sections are hidden by default in Registration page 

   |SECTION                                               |
   |------------------------------------------------------|
   |Caretaker Details                                     |
   |Caretaker Contact Details                             |
   |Caretaker ID Documents                                |
   |Patient ID Documents 1                                |
   |Patient ID Documents 2                                |
   |Legal Representative (for patient under 18 years only)|

* Enter Patient Details 

   |isCareTakerRequiredCheckBox|
   |---------------------------|
   |True                       |

* Verify below sections are visible in Registration page 

   |SECTION                    |
   |---------------------------|
   |NEW PATIENT                |
   |Camp Address               |
   |Patient Contact Details    |
   |Other Information          |
   |Emergency Contact Details  |
   |Patient Arrival Information|
   |Relationships              |
   |Caretaker Details          |
   |Caretaker Contact Details  |
   |Caretaker ID Documents     |

* Verify below sections are hidden in Registration page 

   |SECTION                                               |
   |------------------------------------------------------|
   |Patient ID Documents 1                                |
   |Patient ID Documents 2                                |
   |Legal Representative (for patient under 18 years only)|

* Enter Patient Details 

   |isCareTakerRequiredCheckBox|
   |---------------------------|
   |False                      |

* Verify below sections are visible in Registration page 

   |SECTION                    |
   |---------------------------|
   |NEW PATIENT                |
   |Camp Address               |
   |Patient Contact Details    |
   |Other Information          |
   |Emergency Contact Details  |
   |Patient Arrival Information|
   |Relationships              |

* Verify below sections are hidden in Registration page 

   |SECTION                                               |
   |------------------------------------------------------|
   |Caretaker Details                                     |
   |Caretaker Contact Details                             |
   |Caretaker ID Documents                                |
   |Patient ID Documents 1                                |
   |Patient ID Documents 2                                |
   |Legal Representative (for patient under 18 years only)|

* Enter Patient Details 

   |statusofOfficialIDdocuments|
   |---------------------------|
   |Received                   |

* Verify below sections are visible in Registration page 

   |SECTION                    |
   |---------------------------|
   |NEW PATIENT                |
   |Camp Address               |
   |Patient Contact Details    |
   |Other Information          |
   |Emergency Contact Details  |
   |Patient Arrival Information|
   |Relationships              |
   |Patient ID Documents 1     |
   |Patient ID Documents 2     |

* Verify below sections are hidden in Registration page 

   |SECTION                                               |
   |------------------------------------------------------|
   |Caretaker Details                                     |
   |Caretaker Contact Details                             |
   |Caretaker ID Documents                                |
   |Legal Representative (for patient under 18 years only)|

* Enter Patient Details 

   |statusofOfficialIDdocuments|
   |---------------------------|
   |Waiting                    |

* Verify below sections are visible in Registration page 

   |SECTION                    |
   |---------------------------|
   |NEW PATIENT                |
   |Camp Address               |
   |Patient Contact Details    |
   |Other Information          |
   |Emergency Contact Details  |
   |Patient Arrival Information|
   |Relationships              |

* Verify below sections are hidden in Registration page 

   |SECTION                                               |
   |------------------------------------------------------|
   |Patient ID Documents 1                                |
   |Patient ID Documents 2                                |
   |Caretaker Details                                     |
   |Caretaker Contact Details                             |
   |Caretaker ID Documents                                |
   |Legal Representative (for patient under 18 years only)|

* Enter Patient Details 

   |statusofOfficialIDdocuments|
   |---------------------------|
   |Unknown                    |

* Verify below sections are visible in Registration page 

   |SECTION                    |
   |---------------------------|
   |NEW PATIENT                |
   |Camp Address               |
   |Patient Contact Details    |
   |Other Information          |
   |Emergency Contact Details  |
   |Patient Arrival Information|
   |Relationships              |

* Verify below sections are hidden in Registration page 

   |SECTION                                               |
   |------------------------------------------------------|
   |Patient ID Documents 1                                |
   |Patient ID Documents 2                                |
   |Caretaker Details                                     |
   |Caretaker Contact Details                             |
   |Caretaker ID Documents                                |
   |Legal Representative (for patient under 18 years only)|

* Enter Patient Details 

   |age|gender|
   |---|------|
   |17 |Male  |

* Verify below sections are visible in Registration page 

   |SECTION                                               |
   |------------------------------------------------------|
   |NEW PATIENT                                           |
   |Camp Address                                          |
   |Patient Contact Details                               |
   |Other Information                                     |
   |Emergency Contact Details                             |
   |Patient Arrival Information                           |
   |Relationships                                         |
   |Legal Representative (for patient under 18 years only)|

* Verify below sections are hidden in Registration page 

   |SECTION                  |
   |-------------------------|
   |Caretaker Details        |
   |Caretaker Contact Details|
   |Caretaker ID Documents   |
   |Patient ID Documents 1   |
   |Patient ID Documents 2   |

* Enter Patient Details 

   |age|gender|
   |---|------|
   |18 |Female|

* Verify below sections are visible in Registration page 

   |SECTION                    |
   |---------------------------|
   |NEW PATIENT                |
   |Camp Address               |
   |Patient Contact Details    |
   |Other Information          |
   |Emergency Contact Details  |
   |Patient Arrival Information|
   |Relationships              |

* Verify below sections are hidden in Registration page 

   |SECTION                                               |
   |------------------------------------------------------|
   |Caretaker Details                                     |
   |Caretaker Contact Details                             |
   |Caretaker ID Documents                                |
   |Patient ID Documents 1                                |
   |Patient ID Documents 2                                |
   |Legal Representative (for patient under 18 years only)|
