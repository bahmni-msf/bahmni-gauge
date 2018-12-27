Patient Obs in Forms 2.0
=====================


Created by bsantosh on 14/11/18

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Validate forms display control for forms 2.0
-----------------------
Tags: InTest

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
