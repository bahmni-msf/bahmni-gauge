Patient Obs in Forms 2.0
=====================


Created by bsantosh on 14/11/18

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
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
* Verify form is "v1" version and "Draft" status
* Verify "Save" button is "enable" on form builder
* Verify "Publish" button is "disabled" on form builder

* Save "Observation test form" form using "threeObsInnerSectionObsGroups" by API
* Navigate to form list
* Enter version "1" of "Observation test form" form details
* Click on save
* Verify "Form Saved Successfully" showed up
* Click on publish
* Verify "Form Successfully Published" showed up
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
|11: :12|11/11/2017:test|Site, Ear|Dr. Medya Rasheed|23|100|test|

