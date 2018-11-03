Form Builder UI related tests
=====================
Tags: FormBuilder


Created by bsantosh on 22/10/18

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Create a form by dragging controls
----------------

* Login and create the "formBuilderUITest" form by form builder
* Drag a "label" control to form
* Change the "Label" label name to "Iron Man"
* Drag a "Section" control to form
* Change the "Section" label name to "Captain America"
* Drag a "Obs" control to form
* Associate "HI, Penicillin" concept to "obs"
* Drag a "ObsGroup" control to form
* Associate "History and Examination" concept to "obsGroup"
* Click on save
* Verify "Form Saved Successfully" showed up
* Navigate to form list
* Enter version "1" of "formBuilderUITest" form details
* Verify whether all the controls are placed properly

Edit a form using UI
----------------
* Navigate to form list
* Enter version "1" of "formBuilderUITest" form details
* Validate that concept associated with a obs control is not editable
* Select "AddMore" property for "Captain America"
* Drag a "label" control to form
* Delete "label" control from form
* Move label "Iron Man" to bottom
* Click on save
* Verify "Form Saved Successfully" showed up

Validate Control Properties associated with different concept types
------------------------------------
* Navigate to form list
* Enter version "1" of "formBuilderUITest" form details
* Drag an "Obs" control to form
