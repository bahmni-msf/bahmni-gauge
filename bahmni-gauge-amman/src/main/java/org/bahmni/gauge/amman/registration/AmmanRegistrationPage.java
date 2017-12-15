package org.bahmni.gauge.amman.registration;

import org.bahmni.gauge.amman.registration.domain.AmmanPatient;
import org.bahmni.gauge.amman.registration.domain.Fields;
import org.bahmni.gauge.amman.registration.domain.PatientAttribute;
import org.bahmni.gauge.common.registration.RegistrationFirstPage;
import org.bahmni.gauge.rest.BahmniRestClient;
import org.json.JSONObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.Select;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Objects;

public class AmmanRegistrationPage extends RegistrationFirstPage {

    @FindBy(how = How.CSS, using = ".back-btn")
    public WebElement backButton;

    @FindBy(how = How.CSS, using = ".submit-btn")
    public WebElement save;

    @FindBy(how = How.CSS, using = "#givenNameLocal")
    public WebElement givenNameLocal;

    @FindBy(how = How.CSS, using = "#familyNameLocal")
    public WebElement familyNameLocal;

    @FindBy(how = How.CSS, using = "#familyName")
    public WebElement familyName;

    @FindBy(how = How.CSS, using = "#gender")
    public WebElement gender;

    @FindBy(how = How.CSS, using = "#address3")
    public WebElement country;

    public void fillAttributes(List<PatientAttribute> patientAttributes) {
        for (PatientAttribute patientAttribute : patientAttributes) {
            WebElement element = driver.findElement(By.cssSelector(patientAttribute.getIdentifier()));
            if (patientAttribute.getAttributeType().equals("dropdown")) {
                new Select(element).selectByVisibleText(patientAttribute.getValue());
            } else if (patientAttribute.getAttributeType().equals("checkbox") && patientAttribute.getValue().equals("True")) {
                element.click();
            } else {
                element.clear();
                element.sendKeys(patientAttribute.getValue());
            }
        }
    }

    public void verifyLegalRepValues() {
        scrollToBottom();
        compareFields(Fields.caretakerNameEnglish, Fields.legalRepFullNameEnglish);
        compareFields(Fields.caretakerNameArabic, Fields.legalRepFullNameArabic);
        compareFields(Fields.caretakerGender, Fields.legalRepGender);
        compareFields(Fields.caretakerNationality, Fields.legalRepNationality);
    }

    private void compareFields(Fields expected, Fields actual) {
        String expectedValue = expected.getPatientAttribute().getValue();

        PatientAttribute patientAttribute = actual.getPatientAttribute();
        String identifier = patientAttribute.getIdentifier();
        WebElement element = driver.findElement(By.cssSelector(identifier));
        String actualValue = element.getAttribute("value");
        if (patientAttribute.getAttributeType().equals("dropdown")) {
            actualValue = new Select(element).getFirstSelectedOption().getText();
        }
        if (patientAttribute.getAttributeType().equals("date")) {
            SimpleDateFormat simpleDateFormat1 = new SimpleDateFormat("yyyy-mm-dd");
            SimpleDateFormat simpleDateFormat2 = new SimpleDateFormat("dd-mm-yyyy");
            try {
                Date expectedDate = simpleDateFormat1.parse(expectedValue);
                Date actualDate = simpleDateFormat2.parse(actualValue);
                Assert.assertEquals(expectedDate, actualDate);
            } catch (ParseException e) {
                e.printStackTrace();
            }
        } else {
            Assert.assertEquals(expectedValue, actualValue);
        }
    }

    public void createPatientUsingApi(AmmanPatient ammanPatient) {
        BahmniRestClient.get().createPatient(ammanPatient, "patient_create.ftl");
    }

    public AmmanPatient clickSave(AmmanPatient patient) {
        save.click();
        waitForSpinner();

        String path = driver.getCurrentUrl();
        String uuid = path.substring(path.lastIndexOf('/') + 1);
        if (!Objects.equals(uuid, "new")) {
            Fields.getPatientAttribute("patientIdentifier").setValue(patientIdentifierValue.getText());
            patient.setUuid(uuid);
        }
        return patient;
    }

    public void startVisitUsingApi(AmmanPatient ammanPatient) {
        JSONObject reponse = BahmniRestClient.get().create(ammanPatient, "visit");
        Object activeVisitUuid = reponse.get("uuid");
        ammanPatient.setActiveVisitUuid(activeVisitUuid.toString());
    }

    public void closeVisitUsingApi(AmmanPatient ammanPatient) {
        String requestJson = "{\"withCredentials\":true}";
        BahmniRestClient.post("/openmrs/ws/rest/v1/bahmnicore/visit/endVisit?visitUuid=" + ammanPatient.getActiveVisitUuid(), requestJson);
        ammanPatient.setActiveVisitUuid(null);
    }

    public void verifyLegalRepAfterSave() {
        scrollToBottom();
        compareFields(Fields.legalRepFullNameEnglish, Fields.legalRepFullNameEnglish);
        compareFields(Fields.legalRepFullNameArabic, Fields.legalRepFullNameArabic);
        compareFields(Fields.legalRepGender, Fields.legalRepGender);
        compareFields(Fields.legalRepNationality, Fields.legalRepNationality);
    }

    public void verifyCaretakerAfterSave() {
        scrollToBottom();
        compareFields(Fields.caretakerNameEnglish, Fields.caretakerNameEnglish);
        compareFields(Fields.caretakerNameArabic, Fields.caretakerNameArabic);
        compareFields(Fields.caretakerGender, Fields.caretakerGender);
        compareFields(Fields.caretakerNationality, Fields.caretakerNationality);
    }

    public void verifyIDDocumentsAfterSave() {
        scrollToBottom();
        compareFields(Fields.id1DocNumber, Fields.id1DocNumber);
        compareFields(Fields.id1DocumentType, Fields.id1DocumentType);
        compareFields(Fields.id1FullNameEnglish, Fields.id1FullNameEnglish);
    }

    public void clickBackButton() {
        backButton.click();
    }

    public void verifyPatientDetails() {
        String patientID = Fields.patientIdentifier.getPatientAttribute().getValue();
        String patientFirstName = Fields.firstName.getPatientAttribute().getValue();
        String patientLastName = Fields.lastName.getPatientAttribute().getValue();
        String patientGivenNameLocal = Fields.givenNameArabic.getPatientAttribute().getValue();
        String patientFamilyNameLocal = Fields.familyNameArabic.getPatientAttribute().getValue();
        String patientGender = Fields.gender.getPatientAttribute().getValue();
        String patientAge = Fields.age.getPatientAttribute().getValue();
        String patientCountry = Fields.country.getPatientAttribute().getValue();

        try {
            if (patientIdentifierValue.getText() != null) {
                Assert.assertEquals("Identifier dont match", patientID, patientIdentifierValue.getText());
            }
        } catch (NoSuchElementException ex) {

        }

        Assert.assertEquals("First Name dont match", patientFirstName, txtPatientName.getAttribute("value"));
        Assert.assertEquals("Last Name dont match", patientLastName, familyName.getAttribute("value"));
        Assert.assertEquals("Gender dont match", patientGender, new Select(gender).getFirstSelectedOption().getText());
        Assert.assertEquals("Age dont match", patientAge, ageYears.getAttribute("value"));

        if (givenNameLocal.getAttribute("value") != null) {
            Assert.assertEquals("Given Name Local dont match", patientGivenNameLocal, givenNameLocal.getAttribute("value"));
        }
        if (familyNameLocal.getAttribute("value") != null) {
            Assert.assertEquals("Family Name Local dont match", patientFamilyNameLocal, familyNameLocal.getAttribute("value"));
        }
        Assert.assertEquals("Country dont match", patientCountry, country.getAttribute("value"));
    }
}
