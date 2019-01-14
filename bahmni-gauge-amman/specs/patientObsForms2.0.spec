Patient Obs in Forms 2.0
=====================


Created by bsantosh on 14/11/18

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To use AddMore on different control follow below symantics -
 -- If AddMore for obs is required [currently supported for only text and date inputs], in the same column separate the values with ": :"

For Example :
// |LLA, Pain Severity|
    12: :11

 -- If AddMore for ObsGroup or Section is required, have different columns for each value & suffix the column name with number of occurance.
 // |LLA ROM, Left : Abduction|LLA ROM, Left : Abduction_1|
 // |test|test1

 where LLA ROM, Left : Abduction is in a section with addMore and you want click on addMore and fill both values.
     
Validate forms display control for forms 2.0
-----------------------
Tags: formBuilder, displayControls

* Login and create the "display test form" form by form builder
* Save "display test form" form using "labelObs" by API
* Navigate to form list
* Enter version "1" of "display test form" form details
* Click on publish
* Navigate to dashboard
* Create patient "Deadpool" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* Click on programs app
* Search and select patient "Deadpool" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Add the "display test form" existing form
* Expand "display test form" obs form
* Enter "display test form" template with all observation details
|Weight|
|11|
* Save the consultation
* Navigate to dashboard link
* Verify display control "Edit Forms (2.0)" on dashboard, has the following details
|details|
|display test form|


Add a mix of combination of section controls, obs controls and obsGroup controls
--------------------------------------------------------------------------------
tags: regression, sanity , InTest

* Login and create the "Observation test form" form by form builder
* Save "Observation test form" form using "threeObsInnerSectionObsGroups" by API
* Navigate to form list
* Enter version "1" of "Observation test form" form details
* Click on publish
* Navigate to dashboard
* Create patient "Nasim" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* Click on programs app
* Search and select patient "Nasim" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Add the "Observation test form" existing form
* Click on AddMore for obs "LLA, Pain Severity"
* Click add Note button
* Enter "Observation test form" template with all observation details with hide label and addMore "LLA, Pain Severity"
|LLA, Pain Severity|FSTG, Date received|PPN, Site of wound|MH, Name of MLO|VS, Systolic blood pressure (mmHg)|VS, Diastolic blood pressure (mmHg)|OR, Operation details|
|11: :12|11/11/2017:test|Site, Ear;Site, Face;Site, Toe|Dr. Medya Rasheed|23|100|test|
* Save the consultation
* Validate that filled form has below observation values with hide label and addMore "LLA, Pain Severity"
|obs|values|
|LLA, Pain Severity|11:12|
|FSTG, Date received|2017-11-11|
|PPN, Site of wound|Site, Face;Site, Ear;Site, Toe|
|MH, Name of MLO|Dr. Medya Rasheed|
|VS, Systolic blood pressure (mmHg)|23|
|VS, Diastolic blood pressure (mmHg)|100|
|OR, Operation details|test|


Fill a form with table control
--------------------------------------------------------------------------------
tags: regression, sanity , InTest

* Login and create the "Observation test form" form by form builder
* Save "Observation test form" form using "table" by API
* Navigate to form list
* Enter version "1" of "Observation test form" form details
* Click on publish
* Navigate to dashboard
* Create patient "Nasim" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* Click on programs app
* Search and select patient "Nasim" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Add the "Observation test form" existing form
* Enter "Observation test form" template with all observation details with hide label
|HI, Chloramphenicol|POW, Site of pain|Does the patient have a passport?|SMH, Pain severity|
|Resistant|Site, Ear|Yes|23|
* Validate that filled form has below observation values with hide label
|obs|values|
|HI, Chloramphenicol|Resistant|
|POW, Site of pain|Site, Ear|
|Does the patient have a passport?|Yes|
|SMH, Pain severity|23|