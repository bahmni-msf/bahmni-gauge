Groovy Script Calculations in Observation Forms
===============================================
Created by jaseenam on 18/12/17

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

Tinetti Balance Assessment Tool section in Lower Limb Physiotherapy Assessment form - Verify Risk of falls is high when total score is <=18
-------------------------------------------------------------------------------------------------------------------------------------------
* Create patient "Patient High" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Select patient "Patient High" in tab "All"
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date recorded       |12/12/2017|
   |Type of assessment *|Initial   |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details in "Tinetti Balance Assessment Tool" section 

   |FIELD                                        |VALUE                                                        |
   |---------------------------------------------|-------------------------------------------------------------|
   |Sitting Balance                              |0 = Leans or slides in chair                                 |
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

* Save the consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and verify details in "Tinetti Balance Assessment Tool" section 

   |FIELD                                        |VALUE                                                        |
   |---------------------------------------------|-------------------------------------------------------------|
   |Sitting Balance                              |0 = Leans or slides in chair                                 |
   |Immediate standing, balance (first 5 seconds)|2 = Steady without walker or other support                   |
   |Standing balance                             |2 = Narrow stance without support                            |
   |Nudged                                       |1 = Staggers, grabs, catches self                            |
   |Eyes closed                                  |1 = Steady                                                   |
   |Turning 360 degrees_1                        |0 = Discontinuous steps                                      |
   |Turning 360 degrees_2                        |1 = Steady                                                   |
   |Sitting down                                 |1 = Uses arms or not a smooth motion                         |
   |Balance Score                                |8                                                            |
   |Indication of gait                           |1 = No hesitancy                                             |
   |Step length and height                       |1 = Steps through L;1 = Steps through R;0 = Steps to         |
   |Foot clearance                               |0 = Foot drop;1 = L foot clears floor;1 = R foot clears floor|
   |Step symmetry                                |1 = Right and left step length appear equal                  |
   |Step continuity                              |1 = Steps appear Continuous                                  |
   |Path                                         |1 = Mild/moderate deviation or uses w. Aid                   |
   |Gait Score                                   |8                                                            |
   |Total Score                                  |16                                                           |
   |Risk of Falls                                |High                                                         |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and edit details in "Tinetti Balance Assessment Tool" section 

   |FIELD           |VALUE                                          |
   |----------------|-----------------------------------------------|
   |Sitting Balance |1 = Steady, safe                               |
   |Rises from chair|0 = Unable to without help                     |
   |Attempts to rise|1 = Able, requires >1 attempt                  |
   |Sitting down    |2 = Safe, smooth motion                        |
   |Trunk           |0 = Marked sway or uses w. Aid                 |
   |Walking time    |1 = Heels almost touching while walking        |
   |Foot clearance  |1 = L foot clears floor;1 = R foot clears floor|
   |Path            |2 = Straight without w. aid                    |

* Save the consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and verify details in "Tinetti Balance Assessment Tool" section 

   |FIELD                                        |VALUE                                               |
   |---------------------------------------------|----------------------------------------------------|
   |Sitting Balance                              |1 = Steady, safe                                    |
   |Rises from chair                             |0 = Unable to without help                          |
   |Attempts to rise                             |1 = Able, requires >1 attempt                       |
   |Immediate standing, balance (first 5 seconds)|2 = Steady without walker or other support          |
   |Standing balance                             |2 = Narrow stance without support                   |
   |Nudged                                       |1 = Staggers, grabs, catches self                   |
   |Eyes closed                                  |1 = Steady                                          |
   |Turning 360 degrees_1                        |0 = Discontinuous steps                             |
   |Turning 360 degrees_2                        |1 = Steady                                          |
   |Sitting down                                 |2 = Safe, smooth motion                             |
   |Balance Score                                |11                                                  |
   |Indication of gait                           |1 = No hesitancy                                    |
   |Step length and height                       |1 = Steps through L;1 = Steps through R;0 = Steps to|
   |Foot clearance                               |0 = Foot drop                                       |
   |Step symmetry                                |1 = Right and left step length appear equal         |
   |Step continuity                              |1 = Steps appear Continuous                         |
   |Path                                         |2 = Straight without w. aid                         |
   |Trunk                                        |0 = Marked sway or uses w. Aid                      |
   |Walking time                                 |1 = Heels almost touching while walking             |
   |Gait Score                                   |8                                                   |
   |Total Score                                  |18                                                  |
   |Risk of Falls                                |High                                                |


Tinetti Balance Assessment Tool section in Lower Limb Physiotherapy Assessment form - Verify Risk of falls is moderate when total score is between 19-23
--------------------------------------------------------------------------------------------------------------------------------------------------------
* Create patient "Patient Moderate" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Select patient "Patient Moderate" in tab "All"
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date recorded       |12/12/2017|
   |Type of assessment *|Initial   |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details in "Tinetti Balance Assessment Tool" section 

   |FIELD                                        |VALUE                                                        |
   |---------------------------------------------|-------------------------------------------------------------|
   |Sitting Balance                              |1 = Steady, safe                                             |
   |Attempts to rise                             |1 = Able, requires >1 attempt                                |
   |Immediate standing, balance (first 5 seconds)|2 = Steady without walker or other support                   |
   |Standing balance                             |2 = Narrow stance without support                            |
   |Nudged                                       |1 = Staggers, grabs, catches self                            |
   |Eyes closed                                  |1 = Steady                                                   |
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

* Select template "Lower Limb Physiotherapy Assessment" from observation page and verify details in "Tinetti Balance Assessment Tool" section 

   |FIELD                                        |VALUE                                                        |
   |---------------------------------------------|-------------------------------------------------------------|
   |Sitting Balance                              |1 = Steady, safe                                             |
   |Attempts to rise                             |1 = Able, requires >1 attempt                                |
   |Immediate standing, balance (first 5 seconds)|2 = Steady without walker or other support                   |
   |Standing balance                             |2 = Narrow stance without support                            |
   |Nudged                                       |1 = Staggers, grabs, catches self                            |
   |Eyes closed                                  |1 = Steady                                                   |
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
   |Gait Score                                   |10                                                           |
   |Total Score                                  |20                                                           |
   |Risk of Falls                                |Moderate                                                     |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and edit details in "Tinetti Balance Assessment Tool" section 

   |FIELD                |VALUE                                  |
   |---------------------|---------------------------------------|
   |Path                 |2 = Straight without w. aid            |
   |Rises from chair     |0 = Unable to without help             |
   |Turning 360 degrees_1|0 = Discontinuous steps                |
   |Walking time         |1 = Heels almost touching while walking|

* Save the consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and verify details in "Tinetti Balance Assessment Tool" section 

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
   |Balance Score                                |10                                                           |
   |Indication of gait                           |1 = No hesitancy                                             |
   |Step length and height                       |1 = Steps through L;1 = Steps through R;0 = Steps to         |
   |Foot clearance                               |0 = Foot drop;1 = L foot clears floor;1 = R foot clears floor|
   |Step symmetry                                |1 = Right and left step length appear equal                  |
   |Step continuity                              |1 = Steps appear Continuous                                  |
   |Path                                         |2 = Straight without w. aid                                  |
   |Trunk                                        |2 = No sway, flex., use of arms or w. Aid                    |
   |Walking time                                 |1 = Heels almost touching while walking                      |
   |Gait Score                                   |12                                                           |
   |Total Score                                  |22                                                           |
   |Risk of Falls                                |Moderate                                                     |

Tinetti Balance Assessment Tool section in Lower Limb Physiotherapy Assessment form - Verify Risk of falls is low when total score is >=24
------------------------------------------------------------------------------------------------------------------------------------------
* Create patient "Patient Low" using API with "First Stage Validation" visit
* Enroll patient to reconstructive surgery program using API
* On the login page
* Login with username "BAHMNI_GAUGE_APP_USER" and password "BAHMNI_GAUGE_APP_PASSWORD" with location "BAHMNI_GAUGE_APP_LOCATION"
* Click on programs app
* Select patient "Patient Low" in tab "All"
* Navigate to "Reconstructive Surgery" program dashboard
* Navigate to consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details 

   |FIELD               |VALUE     |
   |--------------------|----------|
   |Date recorded       |12/12/2017|
   |Type of assessment *|Initial   |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and fill details in "Tinetti Balance Assessment Tool" section 

   |FIELD                                        |VALUE                                                        |
   |---------------------------------------------|-------------------------------------------------------------|
   |Sitting Balance                              |1 = Steady, safe                                             |
   |Rises from chair                             |2 = Able without use of arms                                 |
   |Attempts to rise                             |2 = Able, requires, 1 attempt                                |
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
   |Path                                         |2 = Straight without w. aid                                  |
   |Trunk                                        |2 = No sway, flex., use of arms or w. Aid                    |
   |Walking time                                 |1 = Heels almost touching while walking                      |

* Save the consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and verify details in "Tinetti Balance Assessment Tool" section 

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
   |Balance Score                                |13                                                           |
   |Indication of gait                           |1 = No hesitancy                                             |
   |Step length and height                       |1 = Steps through L;1 = Steps through R;0 = Steps to         |
   |Foot clearance                               |0 = Foot drop;1 = L foot clears floor;1 = R foot clears floor|
   |Step symmetry                                |1 = Right and left step length appear equal                  |
   |Step continuity                              |1 = Steps appear Continuous                                  |
   |Trunk                                        |2 = No sway, flex., use of arms or w. Aid                    |
   |Walking time                                 |0 = Heels apart                                              |
   |Gait Score                                   |11                                                           |
   |Total Score                                  |24                                                           |
   |Risk of Falls                                |Low                                                          |

* Select template "Lower Limb Physiotherapy Assessment" from observation page and edit details in "Tinetti Balance Assessment Tool" section 

   |FIELD       |VALUE                                     |
   |------------|------------------------------------------|
   |Nudged      |2 = Steady                                |
   |Sitting down|2 = Safe, smooth motion                   |
   |Path        |1 = Mild/moderate deviation or uses w. Aid|

* Save the consultation
* Select template "Lower Limb Physiotherapy Assessment" from observation page and verify details in "Tinetti Balance Assessment Tool" section 

   |FIELD                                        |VALUE                                                        |
   |---------------------------------------------|-------------------------------------------------------------|
   |Sitting Balance                              |1 = Steady, safe                                             |
   |Rises from chair                             |0 = Unable to without help                                   |
   |Attempts to rise                             |1 = Able, requires >1 attempt                                |
   |Immediate standing, balance (first 5 seconds)|2 = Steady without walker or other support                   |
   |Standing balance                             |2 = Narrow stance without support                            |
   |Nudged                                       |2 = Steady                                                   |
   |Eyes closed                                  |1 = Steady                                                   |
   |Turning 360 degrees_1                        |0 = Discontinuous steps                                      |
   |Turning 360 degrees_2                        |1 = Steady                                                   |
   |Sitting down                                 |2 = Safe, smooth motion                                      |
   |Balance Score                                |15                                                           |
   |Indication of gait                           |1 = No hesitancy                                             |
   |Step length and height                       |1 = Steps through L;1 = Steps through R;0 = Steps to         |
   |Foot clearance                               |0 = Foot drop;1 = L foot clears floor;1 = R foot clears floor|
   |Step symmetry                                |1 = Right and left step length appear equal                  |
   |Step continuity                              |1 = Steps appear Continuous                                  |
   |Path                                         |1 = Mild/moderate deviation or uses w. Aid                   |
   |Trunk                                        |2 = No sway, flex., use of arms or w. Aid                    |
   |Walking time                                 |0 = Heels apart                                              |
   |Gait Score                                   |12                                                           |
   |Total Score                                  |27                                                           |
   |Risk of Falls                                |Low                                                          |
