{
  "form": {
    "name": "${name}",
    "uuid": "${uuid}"
  },
"value":"{\"name\":\"${name}\",\"uuid\":\"${uuid}\",\"controls\":[{\"type\":\"section\",\"label\":{\"type\":\"label\",\"value\":\"Outer Section\"},\"properties\":{\"location\":{\"column\":0,\"row\":0}},\"id\":\"1\",\"controls\":[{\"type\":\"obsControl\",\"label\":{\"type\":\"label\",\"value\":\"Death Note, Hospital Course\"},\"properties\":{\"mandatory\":false,\"notes\":false,\"addMore\":false,\"hideLabel\":false,\"location\":{\"column\":0,\"row\":0}},\"id\":\"2\",\"concept\":{\"name\":\"Death Note, Hospital Course\",\"uuid\":\"f5b27cae-a937-43c0-a116-8db144554d6f\",\"description\":[],\"datatype\":\"Text\",\"answers\":[],\"properties\":{\"allowDecimal\":null}},\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null},{\"type\":\"section\",\"label\":{\"type\":\"label\",\"value\":\"Inner Section\"},\"properties\":{\"location\":{\"column\":0,\"row\":1}},\"id\":\"3\",\"controls\":[{\"type\":\"obsGroupControl\",\"label\":{\"type\":\"label\",\"value\":\"Systolic Data\"},\"properties\":{\"abnormal\":false,\"location\":{\"column\":0,\"row\":0}},\"id\":\"4\",\"concept\":{\"name\":\"Systolic Data\",\"uuid\":\"c36ddb6d-3f10-11e4-adec-0800271c1b75\",\"datatype\":\"N/A\",\"set\":true,\"setMembers\":[{\"name\":\"Systolic(mm Hg)\",\"uuid\":\"c36e9c8b-3f10-11e4-adec-0800271c1b75\",\"datatype\":\"Numeric\",\"description\":[],\"units\":\"mm Hg\",\"hiNormal\":140,\"lowNormal\":110,\"hiAbsolute\":null,\"lowAbsolute\":null,\"answers\":[],\"properties\":{\"allowDecimal\":true}},{\"name\":\"Systolic Abnormal\",\"uuid\":\"c36f5a8b-3f10-11e4-adec-0800271c1b75\",\"datatype\":\"Boolean\",\"description\":[],\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null,\"answers\":[],\"properties\":{\"allowDecimal\":null}}]},\"controls\":[{\"type\":\"obsControl\",\"label\":{\"type\":\"label\",\"value\":\"Systolic(mm Hg)\"},\"properties\":{\"mandatory\":false,\"notes\":true,\"addMore\":false,\"hideLabel\":false,\"location\":{\"row\":0,\"column\":0}},\"id\":\"5\",\"concept\":{\"name\":\"Systolic(mm Hg)\",\"uuid\":\"c36e9c8b-3f10-11e4-adec-0800271c1b75\",\"datatype\":\"Numeric\",\"description\":[],\"units\":\"mm Hg\",\"hiNormal\":140,\"lowNormal\":110,\"hiAbsolute\":null,\"lowAbsolute\":null,\"answers\":[],\"properties\":{\"allowDecimal\":true}},\"units\":\"mm Hg\",\"hiNormal\":140,\"lowNormal\":110,\"hiAbsolute\":null,\"lowAbsolute\":null},{\"options\":[{\"name\":\"Yes\",\"value\":true},{\"name\":\"No\",\"value\":false}],\"type\":\"obsControl\",\"label\":{\"type\":\"label\",\"value\":\"Systolic Abnormal\"},\"properties\":{\"mandatory\":true,\"notes\":true,\"addMore\":false,\"hideLabel\":false,\"location\":{\"row\":1,\"column\":0}},\"id\":\"6\",\"concept\":{\"name\":\"Systolic Abnormal\",\"uuid\":\"c36f5a8b-3f10-11e4-adec-0800271c1b75\",\"datatype\":\"Boolean\",\"description\":[],\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null,\"answers\":[],\"properties\":{\"allowDecimal\":null}},\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null}]},{\"type\":\"obsGroupControl\",\"label\":{\"type\":\"label\",\"value\":\"BMI Status Data\"},\"properties\":{\"abnormal\":false,\"location\":{\"column\":0,\"row\":1}},\"id\":\"7\",\"concept\":{\"name\":\"BMI Status Data\",\"uuid\":\"80ef57a5-0d0c-48de-acdd-19e026c890b5\",\"datatype\":\"N/A\",\"set\":true,\"setMembers\":[{\"name\":\"BMI STATUS\",\"uuid\":\"c368694c-3f10-11e4-adec-0800271c1b75\",\"datatype\":\"Text\",\"description\":[],\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null,\"answers\":[],\"properties\":{\"allowDecimal\":null}},{\"name\":\"BMI STATUS ABNORMAL\",\"uuid\":\"afd34a0d-ca7c-4f31-bd5a-4f1fa98100e1\",\"datatype\":\"Boolean\",\"description\":[],\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null,\"answers\":[],\"properties\":{\"allowDecimal\":null}}]},\"controls\":[{\"type\":\"obsControl\",\"label\":{\"type\":\"label\",\"value\":\"BMI STATUS\"},\"properties\":{\"mandatory\":false,\"notes\":true,\"addMore\":false,\"hideLabel\":false,\"location\":{\"row\":0,\"column\":0}},\"id\":\"8\",\"concept\":{\"name\":\"BMI STATUS\",\"uuid\":\"c368694c-3f10-11e4-adec-0800271c1b75\",\"datatype\":\"Text\",\"description\":[],\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null,\"answers\":[],\"properties\":{\"allowDecimal\":null}},\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null},{\"options\":[{\"name\":\"Yes\",\"value\":true},{\"name\":\"No\",\"value\":false}],\"type\":\"obsControl\",\"label\":{\"type\":\"label\",\"value\":\"BMI STATUS ABNORMAL\"},\"properties\":{\"mandatory\":true,\"notes\":true,\"addMore\":false,\"hideLabel\":false,\"location\":{\"row\":1,\"column\":0}},\"id\":\"9\",\"concept\":{\"name\":\"BMI STATUS ABNORMAL\",\"uuid\":\"afd34a0d-ca7c-4f31-bd5a-4f1fa98100e1\",\"datatype\":\"Boolean\",\"description\":[],\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null,\"answers\":[],\"properties\":{\"allowDecimal\":null}},\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null}]}]},{\"type\":\"obsControl\",\"label\":{\"type\":\"label\",\"value\":\"P/A Presenting Part\"},\"properties\":{\"mandatory\":false,\"notes\":true,\"addMore\":false,\"hideLabel\":false,\"location\":{\"column\":0,\"row\":2},\"dropDown\":true,\"multiSelect\":false},\"id\":\"14\",\"concept\":{\"name\":\"P/A Presenting Part\",\"uuid\":\"c4517f49-3f10-11e4-adec-0800271c1b75\",\"description\":[],\"datatype\":\"Coded\",\"answers\":[{\"uuid\":\"c4526510-3f10-11e4-adec-0800271c1b75\",\"name\":{\"display\":\"Cephalic\",\"uuid\":\"c4526bb2-3f10-11e4-adec-0800271c1b75\",\"name\":\"Cephalic\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c4526510-3f10-11e4-adec-0800271c1b75/name/c4526bb2-3f10-11e4-adec-0800271c1b75\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c4526510-3f10-11e4-adec-0800271c1b75/name/c4526bb2-3f10-11e4-adec-0800271c1b75?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Cephalic\",\"uuid\":\"c4526bb2-3f10-11e4-adec-0800271c1b75\",\"name\":\"Cephalic\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c4526510-3f10-11e4-adec-0800271c1b75/name/c4526bb2-3f10-11e4-adec-0800271c1b75\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c4526510-3f10-11e4-adec-0800271c1b75/name/c4526bb2-3f10-11e4-adec-0800271c1b75?v=full\"}],\"resourceVersion\":\"1.9\"},{\"display\":\"Cephalic\",\"uuid\":\"57626fe7-a25e-404f-8c5e-427b407f97aa\",\"name\":\"Cephalic\",\"locale\":\"en\",\"localePreferred\":false,\"conceptNameType\":\"SHORT\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c4526510-3f10-11e4-adec-0800271c1b75/name/57626fe7-a25e-404f-8c5e-427b407f97aa\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c4526510-3f10-11e4-adec-0800271c1b75/name/57626fe7-a25e-404f-8c5e-427b407f97aa?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Cephalic\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"c45329de-3f10-11e4-adec-0800271c1b75\",\"name\":{\"display\":\"Breech\",\"uuid\":\"c45330f0-3f10-11e4-adec-0800271c1b75\",\"name\":\"Breech\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c45329de-3f10-11e4-adec-0800271c1b75/name/c45330f0-3f10-11e4-adec-0800271c1b75\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c45329de-3f10-11e4-adec-0800271c1b75/name/c45330f0-3f10-11e4-adec-0800271c1b75?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Breech\",\"uuid\":\"c45330f0-3f10-11e4-adec-0800271c1b75\",\"name\":\"Breech\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c45329de-3f10-11e4-adec-0800271c1b75/name/c45330f0-3f10-11e4-adec-0800271c1b75\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c45329de-3f10-11e4-adec-0800271c1b75/name/c45330f0-3f10-11e4-adec-0800271c1b75?v=full\"}],\"resourceVersion\":\"1.9\"},{\"display\":\"Breech\",\"uuid\":\"0ab2ccd3-40e9-43ef-99c2-b6b745a49135\",\"name\":\"Breech\",\"locale\":\"en\",\"localePreferred\":false,\"conceptNameType\":\"SHORT\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c45329de-3f10-11e4-adec-0800271c1b75/name/0ab2ccd3-40e9-43ef-99c2-b6b745a49135\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c45329de-3f10-11e4-adec-0800271c1b75/name/0ab2ccd3-40e9-43ef-99c2-b6b745a49135?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Breech\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"c453caa3-3f10-11e4-adec-0800271c1b75\",\"name\":{\"display\":\"Transverse\",\"uuid\":\"c453d148-3f10-11e4-adec-0800271c1b75\",\"name\":\"Transverse\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c453caa3-3f10-11e4-adec-0800271c1b75/name/c453d148-3f10-11e4-adec-0800271c1b75\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c453caa3-3f10-11e4-adec-0800271c1b75/name/c453d148-3f10-11e4-adec-0800271c1b75?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Transverse\",\"uuid\":\"c453ce42-3f10-11e4-adec-0800271c1b75\",\"name\":\"Transverse\",\"locale\":\"en\",\"localePreferred\":false,\"conceptNameType\":\"SHORT\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c453caa3-3f10-11e4-adec-0800271c1b75/name/c453ce42-3f10-11e4-adec-0800271c1b75\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c453caa3-3f10-11e4-adec-0800271c1b75/name/c453ce42-3f10-11e4-adec-0800271c1b75?v=full\"}],\"resourceVersion\":\"1.9\"},{\"display\":\"Transverse\",\"uuid\":\"c453d148-3f10-11e4-adec-0800271c1b75\",\"name\":\"Transverse\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c453caa3-3f10-11e4-adec-0800271c1b75/name/c453d148-3f10-11e4-adec-0800271c1b75\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c453caa3-3f10-11e4-adec-0800271c1b75/name/c453d148-3f10-11e4-adec-0800271c1b75?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Transverse\",\"resourceVersion\":\"1.9\"}],\"properties\":{\"allowDecimal\":null}},\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null},{\"type\":\"obsControl\",\"label\":{\"type\":\"label\",\"value\":\"Diabetes, Cormorbidities\"},\"properties\":{\"mandatory\":false,\"notes\":false,\"addMore\":false,\"hideLabel\":false,\"location\":{\"column\":0,\"row\":3},\"dropDown\":false,\"autoComplete\":true,\"multiSelect\":true},\"id\":\"15\",\"concept\":{\"name\":\"Diabetes, Cormorbidities\",\"uuid\":\"eeca97c4-c3e2-4430-85a5-a6ee9f577292\",\"description\":[],\"datatype\":\"Coded\",\"answers\":[{\"uuid\":\"8961717d-b30d-46b1-b917-ff5a463fcb51\",\"name\":{\"display\":\"Hypertension\",\"uuid\":\"4f940bcd-53dc-4fbc-82a5-c16d046cf112\",\"name\":\"Hypertension\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/8961717d-b30d-46b1-b917-ff5a463fcb51/name/4f940bcd-53dc-4fbc-82a5-c16d046cf112\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/8961717d-b30d-46b1-b917-ff5a463fcb51/name/4f940bcd-53dc-4fbc-82a5-c16d046cf112?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Hypertension\",\"uuid\":\"4f940bcd-53dc-4fbc-82a5-c16d046cf112\",\"name\":\"Hypertension\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/8961717d-b30d-46b1-b917-ff5a463fcb51/name/4f940bcd-53dc-4fbc-82a5-c16d046cf112\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/8961717d-b30d-46b1-b917-ff5a463fcb51/name/4f940bcd-53dc-4fbc-82a5-c16d046cf112?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Hypertension\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"46efad8c-dbed-4ba5-bf4f-53fc8c1a2a10\",\"name\":{\"display\":\"Hyperlipidemia\",\"uuid\":\"062997e1-2d51-4797-8002-e681a9e11483\",\"name\":\"Hyperlipidemia\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/46efad8c-dbed-4ba5-bf4f-53fc8c1a2a10/name/062997e1-2d51-4797-8002-e681a9e11483\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/46efad8c-dbed-4ba5-bf4f-53fc8c1a2a10/name/062997e1-2d51-4797-8002-e681a9e11483?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Hyperlipidemia\",\"uuid\":\"062997e1-2d51-4797-8002-e681a9e11483\",\"name\":\"Hyperlipidemia\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/46efad8c-dbed-4ba5-bf4f-53fc8c1a2a10/name/062997e1-2d51-4797-8002-e681a9e11483\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/46efad8c-dbed-4ba5-bf4f-53fc8c1a2a10/name/062997e1-2d51-4797-8002-e681a9e11483?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Hyperlipidemia\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"825e7c2e-304e-43bc-b138-e1c4bfe70b54\",\"name\":{\"display\":\"Coronary DZ\",\"uuid\":\"a31f7438-9b63-4ddb-952a-e15efcf64846\",\"name\":\"Coronary DZ\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/825e7c2e-304e-43bc-b138-e1c4bfe70b54/name/a31f7438-9b63-4ddb-952a-e15efcf64846\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/825e7c2e-304e-43bc-b138-e1c4bfe70b54/name/a31f7438-9b63-4ddb-952a-e15efcf64846?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Coronary DZ\",\"uuid\":\"a31f7438-9b63-4ddb-952a-e15efcf64846\",\"name\":\"Coronary DZ\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/825e7c2e-304e-43bc-b138-e1c4bfe70b54/name/a31f7438-9b63-4ddb-952a-e15efcf64846\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/825e7c2e-304e-43bc-b138-e1c4bfe70b54/name/a31f7438-9b63-4ddb-952a-e15efcf64846?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Coronary DZ\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"ce668b6d-3141-487e-bd0f-090b4484eba4\",\"name\":{\"display\":\"Obesity\",\"uuid\":\"ca195937-c5de-4c29-91e7-b5b31a40ac87\",\"name\":\"Obesity\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/ce668b6d-3141-487e-bd0f-090b4484eba4/name/ca195937-c5de-4c29-91e7-b5b31a40ac87\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/ce668b6d-3141-487e-bd0f-090b4484eba4/name/ca195937-c5de-4c29-91e7-b5b31a40ac87?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Obesity\",\"uuid\":\"ca195937-c5de-4c29-91e7-b5b31a40ac87\",\"name\":\"Obesity\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/ce668b6d-3141-487e-bd0f-090b4484eba4/name/ca195937-c5de-4c29-91e7-b5b31a40ac87\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/ce668b6d-3141-487e-bd0f-090b4484eba4/name/ca195937-c5de-4c29-91e7-b5b31a40ac87?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Obesity\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"c1935955-b2a5-47c2-8e78-1c9a44aeed54\",\"name\":{\"display\":\"Heart failure\",\"uuid\":\"c2e18f0d-617d-4186-9714-5a7fb0790caf\",\"name\":\"Heart failure\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c1935955-b2a5-47c2-8e78-1c9a44aeed54/name/c2e18f0d-617d-4186-9714-5a7fb0790caf\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c1935955-b2a5-47c2-8e78-1c9a44aeed54/name/c2e18f0d-617d-4186-9714-5a7fb0790caf?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Heart failure\",\"uuid\":\"c2e18f0d-617d-4186-9714-5a7fb0790caf\",\"name\":\"Heart failure\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c1935955-b2a5-47c2-8e78-1c9a44aeed54/name/c2e18f0d-617d-4186-9714-5a7fb0790caf\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/c1935955-b2a5-47c2-8e78-1c9a44aeed54/name/c2e18f0d-617d-4186-9714-5a7fb0790caf?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Heart failure\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"5e515737-3d71-45b4-b217-383eee067ee3\",\"name\":{\"display\":\"CKD\",\"uuid\":\"da2056c2-eb83-4411-9fac-fabf3801b8f6\",\"name\":\"CKD\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/5e515737-3d71-45b4-b217-383eee067ee3/name/da2056c2-eb83-4411-9fac-fabf3801b8f6\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/5e515737-3d71-45b4-b217-383eee067ee3/name/da2056c2-eb83-4411-9fac-fabf3801b8f6?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"CKD\",\"uuid\":\"da2056c2-eb83-4411-9fac-fabf3801b8f6\",\"name\":\"CKD\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/5e515737-3d71-45b4-b217-383eee067ee3/name/da2056c2-eb83-4411-9fac-fabf3801b8f6\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/5e515737-3d71-45b4-b217-383eee067ee3/name/da2056c2-eb83-4411-9fac-fabf3801b8f6?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"CKD\",\"resourceVersion\":\"1.9\"}],\"properties\":{\"allowDecimal\":null}},\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null},{\"type\":\"obsControl\",\"label\":{\"type\":\"label\",\"value\":\"Diabetes, Exercise\"},\"properties\":{\"mandatory\":false,\"notes\":false,\"addMore\":false,\"hideLabel\":false,\"location\":{\"column\":0,\"row\":4},\"dropDown\":false},\"id\":\"17\",\"concept\":{\"name\":\"Diabetes, Exercise\",\"uuid\":\"1bd46505-819d-48be-859c-79a8ba45c410\",\"description\":[],\"datatype\":\"Coded\",\"answers\":[{\"uuid\":\"a08c40a1-afc1-4a09-b162-654166d43ee3\",\"name\":{\"display\":\"None / Sedentary\",\"uuid\":\"f43cd56a-366f-4f60-9628-6076e35d4057\",\"name\":\"None / Sedentary\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/a08c40a1-afc1-4a09-b162-654166d43ee3/name/f43cd56a-366f-4f60-9628-6076e35d4057\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/a08c40a1-afc1-4a09-b162-654166d43ee3/name/f43cd56a-366f-4f60-9628-6076e35d4057?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"None / Sedentary\",\"uuid\":\"f43cd56a-366f-4f60-9628-6076e35d4057\",\"name\":\"None / Sedentary\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/a08c40a1-afc1-4a09-b162-654166d43ee3/name/f43cd56a-366f-4f60-9628-6076e35d4057\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/a08c40a1-afc1-4a09-b162-654166d43ee3/name/f43cd56a-366f-4f60-9628-6076e35d4057?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"None / Sedentary\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"f9507238-0a22-4e77-8570-1be88266d1f2\",\"name\":{\"display\":\"Standing at work\",\"uuid\":\"ba766f8e-c4d5-407b-9236-ee7e15c17cc9\",\"name\":\"Standing at work\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/f9507238-0a22-4e77-8570-1be88266d1f2/name/ba766f8e-c4d5-407b-9236-ee7e15c17cc9\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/f9507238-0a22-4e77-8570-1be88266d1f2/name/ba766f8e-c4d5-407b-9236-ee7e15c17cc9?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Standing at work\",\"uuid\":\"ba766f8e-c4d5-407b-9236-ee7e15c17cc9\",\"name\":\"Standing at work\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/f9507238-0a22-4e77-8570-1be88266d1f2/name/ba766f8e-c4d5-407b-9236-ee7e15c17cc9\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/f9507238-0a22-4e77-8570-1be88266d1f2/name/ba766f8e-c4d5-407b-9236-ee7e15c17cc9?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Standing at work\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"7d7236ef-54fd-43cd-a286-6db4f81b844c\",\"name\":{\"display\":\"Labor for work\",\"uuid\":\"7f7509aa-b1bf-4af0-8b28-6694f52051ab\",\"name\":\"Labor for work\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/7d7236ef-54fd-43cd-a286-6db4f81b844c/name/7f7509aa-b1bf-4af0-8b28-6694f52051ab\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/7d7236ef-54fd-43cd-a286-6db4f81b844c/name/7f7509aa-b1bf-4af0-8b28-6694f52051ab?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Labor for work\",\"uuid\":\"7f7509aa-b1bf-4af0-8b28-6694f52051ab\",\"name\":\"Labor for work\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/7d7236ef-54fd-43cd-a286-6db4f81b844c/name/7f7509aa-b1bf-4af0-8b28-6694f52051ab\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/7d7236ef-54fd-43cd-a286-6db4f81b844c/name/7f7509aa-b1bf-4af0-8b28-6694f52051ab?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Labor for work\",\"resourceVersion\":\"1.9\"},{\"uuid\":\"1ab6bb8f-9153-4a62-ac9d-dfcc56131bf2\",\"name\":{\"display\":\"Cardio exercise\",\"uuid\":\"23c4aee4-6bcb-4198-8f69-d5655b167448\",\"name\":\"Cardio exercise\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/1ab6bb8f-9153-4a62-ac9d-dfcc56131bf2/name/23c4aee4-6bcb-4198-8f69-d5655b167448\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/1ab6bb8f-9153-4a62-ac9d-dfcc56131bf2/name/23c4aee4-6bcb-4198-8f69-d5655b167448?v=full\"}],\"resourceVersion\":\"1.9\"},\"names\":[{\"display\":\"Cardio exercise\",\"uuid\":\"23c4aee4-6bcb-4198-8f69-d5655b167448\",\"name\":\"Cardio exercise\",\"locale\":\"en\",\"localePreferred\":true,\"conceptNameType\":\"FULLY_SPECIFIED\",\"links\":[{\"rel\":\"self\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/1ab6bb8f-9153-4a62-ac9d-dfcc56131bf2/name/23c4aee4-6bcb-4198-8f69-d5655b167448\"},{\"rel\":\"full\",\"uri\":\"http://local.mybahmni.org/openmrs/ws/rest/v1/concept/1ab6bb8f-9153-4a62-ac9d-dfcc56131bf2/name/23c4aee4-6bcb-4198-8f69-d5655b167448?v=full\"}],\"resourceVersion\":\"1.9\"}],\"displayString\":\"Cardio exercise\",\"resourceVersion\":\"1.9\"}],\"properties\":{\"allowDecimal\":null}},\"units\":null,\"hiNormal\":null,\"lowNormal\":null,\"hiAbsolute\":null,\"lowAbsolute\":null}]}]}",
  "uuid": ""
}