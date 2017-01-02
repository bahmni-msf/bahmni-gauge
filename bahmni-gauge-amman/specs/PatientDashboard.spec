Patient Dashboard Spec
=====================
Created by swarup on 1/2/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Verify the display controls visibility
--------------------------------------
* Create patient "Nasmul" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_DATA_ADMIN_USER" and password "BAHMNI_GAUGE_DATA_ADMIN_PASSWORD" with location "BAHMNI_GAUGE_DATA_ADMIN_LOCATION"
* Click on programs app
* Search and select patient "Nasmul" from "Programs" queue
* Navigate to "Reconstructive Surgery" program dashboard
* Verify the following display controls are visible
| Display Control Title       |
| Programs                    |
| Edit forms                  |
| Visits                      |
| Patient Medical Documents   |
| Patient Encounter Locations |
* Verify the following display controls are hidden
| Display Control Title  |
| Medical History        |
| First Stage Validation |
| Followup Validation    |
| Final Validation       |
