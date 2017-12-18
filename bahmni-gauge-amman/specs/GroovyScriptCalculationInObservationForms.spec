Groovy Script Calculations in Observation Forms
===============================================
Created by jaseenam on 18/12/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Groovy Script Calculations in Lower Limb Physiotherapy Assessment form
----------------------------------------------------------------------
* Create patient "Physio Patient" using API with "Hospital" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_OPD_USER" and password "BAHMNI_GAUGE_OPD_PASSWORD" with location "BAHMNI_GAUGE_OPD_LOCATION"
* Click on "Programs" app
* Select patient "Physio Patient" in tab "All"
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date recorded       |01/12/2017|
   |Type of assessment *|Initial   |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details 

   |FIELD                                        |VALUE                                                        |
   |---------------------------------------------|-------------------------------------------------------------|
   |Sitting Balance                              |1 = Steady, safe                                             |
   |Rises from chair                             |0 = Unable to without help                                   |
   |Attempts to rise                             |1 = Able, requires >1 attempt                                |
   |Immediate standing, balance (first 5 seconds)|2 = Steady without walker or other support                   |
   |Standing balance                             |2 = Narrow stance without support                            |
   |Nudged                                       |1 = Staggers, grabs, catches self                            |
   |Eyes closed                                  |1 = Steady                                                   |
   |Turning 360 degrees_1                        |0 = Discontinuous steps                                      |
   |Turning 360 degrees_2                        |1 = Steady                                                   |
   |Sitting down                                 |1 = Uses arms or not a smooth motion                         |
   |Indication of gait                           |1 = No hesitancy                                             |
   |Step length and height                       |1 = Steps through L;1 = Steps through R;0 = Steps to         |
   |Foot clearance                               |0 = Foot drop;1 = L foot clears floor;1 = R foot clears floor|
   |Step symmetry                                |1 = Right and left step length appear equal                  |
   |Step continuity                              |1 = Steps appear Continuous                                  |
   |Path                                         |1 = Mild/moderate deviation or uses w. Aid                   |
   |Trunk                                        |2 = No sway, flex., use of arms or w. Aid                    |

* Save the consultation
* Verify these forms are saved and disabled to add 

   |FORM                               |
   |-----------------------------------|
   |Lower Limb Physiotherapy Assessment|

* Select template "Lower Limb Physiotherapy Assessment" from observation page and verify details 

   |FIELD                                        |VALUE                                                        |
   |---------------------------------------------|-------------------------------------------------------------|
   |Date recorded                                |2017-12-01                                                   |
   |Type of assessment *                         |Initial                                                      |
   |Sitting Balance                              |1 = Steady, safe                                             |
   |Rises from chair                             |0 = Unable to without help                                   |
   |Attempts to rise                             |1 = Able, requires >1 attempt                                |
   |Immediate standing, balance (first 5 seconds)|2 = Steady without walker or other support                   |
   |Standing balance                             |2 = Narrow stance without support                            |
   |Nudged                                       |1 = Staggers, grabs, catches self                            |
   |Eyes closed                                  |1 = Steady                                                   |
   |Turning 360 degrees_1                        |0 = Discontinuous steps                                      |
   |Turning 360 degrees_2                        |1 = Steady                                                   |
   |Sitting down                                 |1 = Uses arms or not a smooth motion                         |
   |Balance Score                                |10                                                           |
   |Indication of gait                           |1 = No hesitancy                                             |
   |Step length and height                       |1 = Steps through L;1 = Steps through R;0 = Steps to         |
   |Foot clearance                               |0 = Foot drop;1 = L foot clears floor;1 = R foot clears floor|
   |Step symmetry                                |1 = Right and left step length appear equal                  |
   |Step continuity                              |1 = Steps appear Continuous                                  |
   |Path                                         |1 = Mild/moderate deviation or uses w. Aid                   |
   |Trunk                                        |2 = No sway, flex., use of arms or w. Aid                    |
   |Walking time                                 |0 = Heels apart                                              |
   |Gait Score                                   |10                                                           |
   |Total Score                                  |20                                                           |
   |Risk of Falls                                |Moderate                                                     |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details 

   |FIELD                                                                         |VALUE                    |
   |------------------------------------------------------------------------------|-------------------------|
   |Walking time                                                                  |0 = Heels apart          |
   |How old is the patient                                                        |\< 18 years              |
   |I could get down on my knees without holding on to something                  |4 = With no trouble      |
   |I could keep up when I played with other kids                                 |3 = With a little trouble|
   |I could walk for 15 minutes                                                   |3 = With a little trouble|
   |I could walk between rooms                                                    |3 = With a little trouble|
   |I could get on and off the toilet without using my arms                       |4 = With no trouble      |
   |I could get on and off a low chair                                            |4 = With no trouble      |
   |I could get up from the floor by myself                                       |4 = With no trouble      |
   |I could sit on a bench without support for 15 minutes?                        |4 = With no trouble      |
   |I could stand on my tiptoes to reach for something                            |4 = With no trouble      |
   |I could stand on my tiptoes to put something (e.g. a pack of sugar) on a shelf|3 = With a little trouble|
   |I could walk on slightly uneven surfaces (such as cracked pavement)           |4 = With no trouble      |
   |I could walk on rough, uneven surfaces (such as lawns/ fields)                |3 = With a little trouble|
   |I could walk up and down ramps and hills                                      |4 = With no trouble      |
   |I could walk up and down curbs (steps)                                        |3 = With a little trouble|
   |I could get in and out of a bus                                               |3 = With a little trouble|
   |I could get in and out of a car                                               |4 = With no trouble      |
   |I could walk across the room                                                  |3 = With a little trouble|
   |I could walk while wearing a backpack full of books                           |4 = With no trouble      |
   |I could bend over to pick something up                                        |3 = With a little trouble|
   |I could exercise that others my age can do                                    |3 = With a little trouble|

* Save the consultation
* Verify these forms are saved and disabled to add 

   |FORM                               |
   |-----------------------------------|
   |Lower Limb Physiotherapy Assessment|

* Select template "Lower Limb Physiotherapy Assessment" from observation page and verify details 

   |FIELD                                                                         |VALUE                    |
   |------------------------------------------------------------------------------|-------------------------|
   |How old is the patient                                                        |\< 18 years              |
   |I could get down on my knees without holding on to something                  |4 = With no trouble      |
   |I could keep up when I played with other kids                                 |3 = With a little trouble|
   |I could walk for 15 minutes                                                   |3 = With a little trouble|
   |I could walk between rooms                                                    |3 = With a little trouble|
   |I could get on and off the toilet without using my arms                       |4 = With no trouble      |
   |I could get on and off a low chair                                            |4 = With no trouble      |
   |I could get up from the floor by myself                                       |4 = With no trouble      |
   |I could sit on a bench without support for 15 minutes?                        |4 = With no trouble      |
   |I could stand on my tiptoes to reach for something                            |4 = With no trouble      |
   |I could stand on my tiptoes to put something (e.g. a pack of sugar) on a shelf|3 = With a little trouble|
   |I could walk on slightly uneven surfaces (such as cracked pavement)           |4 = With no trouble      |
   |I could walk on rough, uneven surfaces (such as lawns/ fields)                |3 = With a little trouble|
   |I could walk up and down ramps and hills                                      |4 = With no trouble      |
   |I could walk up and down curbs (steps)                                        |3 = With a little trouble|
   |I could get in and out of a bus                                               |3 = With a little trouble|
   |I could get in and out of a car                                               |4 = With no trouble      |
   |I could walk across the room                                                  |3 = With a little trouble|
   |I could walk while wearing a backpack full of books                           |4 = With no trouble      |
   |I could bend over to pick something up                                        |3 = With a little trouble|
   |I could exercise that others my age can do                                    |3 = With a little trouble|
   |Total Score                                                                   |87.5                     |

* Navigate to patient dashboard
* Verify the dashboard name is "Physiotherapy Summary"
* Verify following details of "Physiotherapy Assessments" in Patient Dashboard 

   |FIELD                                                                         |VALUE                                                          |
   |------------------------------------------------------------------------------|---------------------------------------------------------------|
   |Date recorded                                                                 |01 Dec 17                                                      |
   |Type of assessment                                                            |Initial                                                        |
   |Sitting Balance                                                               |1 = Steady, safe                                               |
   |Rises from chair                                                              |0 = Unable to without help                                     |
   |Attempts to rise                                                              |1 = Able, requires >1 attempt                                  |
   |Immediate standing, balance (first 5 seconds)                                 |2 = Steady without walker or other support                     |
   |Standing balance                                                              |2 = Narrow stance without support                              |
   |Nudged                                                                        |1 = Staggers, grabs, catches self                              |
   |Eyes closed                                                                   |1 = Steady                                                     |
   |Turning 360 degrees_1                                                         |0 = Discontinuous steps                                        |
   |Turning 360 degrees_2                                                         |1 = Steady                                                     |
   |Sitting down                                                                  |1 = Uses arms or not a smooth motion                           |
   |Balance Score                                                                 |10                                                             |
   |Indication of gait                                                            |1 = No hesitancy                                               |
   |Step length and height                                                        |1 = Steps through L, 1 = Steps through R, 0 = Steps to         |
   |Foot clearance                                                                |0 = Foot drop, 1 = L foot clears floor, 1 = R foot clears floor|
   |Step symmetry                                                                 |1 = Right and left step length appear equal                    |
   |Step continuity                                                               |1 = Steps appear Continuous                                    |
   |Path                                                                          |1 = Mild/moderate deviation or uses w. Aid                     |
   |Trunk                                                                         |2 = No sway, flex., use of arms or w. Aid                      |
   |Walking time                                                                  |0 = Heels apart                                                |
   |Gait Score                                                                    |10                                                             |
   |Total Score                                                                   |20                                                             |
   |Risk of Falls                                                                 |Moderate                                                       |
   |How old is the patient                                                        |\< 18 years                                                    |
   |I could get down on my knees without holding on to something                  |4 = With no trouble                                            |
   |I could keep up when I played with other kids                                 |3 = With a little trouble                                      |
   |I could walk for 15 minutes                                                   |3 = With a little trouble                                      |
   |I could walk between rooms                                                    |3 = With a little trouble                                      |
   |I could get on and off the toilet without using my arms                       |4 = With no trouble                                            |
   |I could get on and off a low chair                                            |4 = With no trouble                                            |
   |I could get up from the floor by myself                                       |4 = With no trouble                                            |
   |I could sit on a bench without support for 15 minutes?                        |4 = With no trouble                                            |
   |I could stand on my tiptoes to reach for something                            |4 = With no trouble                                            |
   |I could stand on my tiptoes to put something (e.g. a pack of sugar) on a shelf|3 = With a little trouble                                      |
   |I could walk on slightly uneven surfaces (such as cracked pavement)           |4 = With no trouble                                            |
   |I could walk on rough, uneven surfaces (such as lawns/ fields)                |3 = With a little trouble                                      |
   |I could walk up and down ramps and hills                                      |4 = With no trouble                                            |
   |I could walk up and down curbs (steps)                                        |3 = With a little trouble                                      |
   |I could get in and out of a bus                                               |3 = With a little trouble                                      |
   |I could get in and out of a car                                               |4 = With no trouble                                            |
   |I could walk across the room                                                  |3 = With a little trouble                                      |
   |I could walk while wearing a backpack full of books                           |4 = With no trouble                                            |
   |I could bend over to pick something up                                        |3 = With a little trouble                                      |
   |I could exercise that others my age can do                                    |3 = With a little trouble                                      |
   |Total Score                                                                   |87.5                                                           |
