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
* Create a new patient through API
* Open visit of type "OPD" in "BAHMNI_GAUGE_APP_LOCATION" location for previous patient using api
