package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.bahmni.gauge.amman.SpecStoreHelper;
import org.bahmni.gauge.amman.registration.AmmanRegistrationPage;
import org.bahmni.gauge.amman.registration.domain.AmmanPatient;
import org.bahmni.gauge.amman.registration.domain.Fields;
import org.bahmni.gauge.amman.registration.domain.PatientAttribute;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.bahmni.gauge.common.registration.RegistrationVisitDetailsPage;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import java.util.ArrayList;
import java.util.List;

public class RegistrationSpec {
    private AmmanPatient ammanPatient = new AmmanPatient();
    private AmmanRegistrationPage registrationPage = (AmmanRegistrationPage) PageFactory.get(AmmanRegistrationPage.class);

    @BeforeClassSteps
    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step({"Enter Patient Details <table>", "Enter Legal Rep Details <table>", "Enter Caretaker Details <table>", "Enter ID Document Details <table>", "Edit previous patient details <table>"})
    public void enterPatientDetails(Table table) throws Exception {
        List<PatientAttribute> patientAttributes = transformTableToPatientAttributes(table);
        waitForAppReady();
        registrationPage.fillAttributes(patientAttributes);
    }

    @Step("Save Patient and refresh page")
    public void savePatient() {
        AmmanPatient ammnPatient = registrationPage.clickSave(ammanPatient);
        SpecStoreHelper.store(AmmanPatient.class, ammnPatient);
        DriverFactory.getDriver().navigate().refresh();
    }

    @Step("Save Patient")
    public void clickSavePatient() {
        AmmanPatient ammnPatient = registrationPage.clickSave(ammanPatient);
        SpecStoreHelper.store(AmmanPatient.class, ammnPatient);
    }

    @Step("Go to Home Page")
    public void clickBackButton() {
        registrationPage.clickBackButton();
        waitForAppReady();
    }

    @Step("Start <visitType> visit and navigate to Programs page")
    public void startVisitNavigateProgram(String visitType) {
        registrationPage.showAllVisitTypeOptions();
        registrationPage.findVisit(visitType).click();
        waitForAppReady();
        PageFactory.get(RegistrationVisitDetailsPage.class);
    }

    @Step("Click Enter <hospital> visit Details button and navigate to Programs page")
    public void enterVisitNavigateProgram(String visitName) {
        registrationPage.clickVisitDetailsButton();
        waitForAppReady();
        PageFactory.get(RegistrationVisitDetailsPage.class);
    }

    @Step("Verify Legal Rep Values for autocomplete")
    public void verifyLegalRepValues() {
        registrationPage.verifyLegalRepValues();
    }


    private ArrayList<PatientAttribute> transformTableToPatientAttributes(Table table) throws Exception {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        ArrayList<PatientAttribute> patientAttributes = new ArrayList<PatientAttribute>();
        for (String columnName : columnNames) {
            PatientAttribute patientAttribute = Fields.getPatientAttribute(columnName);
            if (patientAttribute != null) {
                patientAttribute.setValue(rows.get(0).getCell(columnName));
                patientAttributes.add(patientAttribute);
                ammanPatient.addAttribute(patientAttribute);
            }
        }

        return patientAttributes;
    }

    @Step("Create patient <Name> using API with <visit Type> visit")
    public void implementation1(String name, String visitType) throws Exception {
        PatientAttribute patientAttribute = Fields.firstName.getPatientAttribute();
        patientAttribute.setValue(name);
        ammanPatient.addAttribute(patientAttribute);
        registrationPage.createPatientUsingApi(ammanPatient);
        SpecStoreHelper.store(AmmanPatient.class, ammanPatient);
        ammanPatient.setVisitType(visitType);
        registrationPage.startVisitUsingApi(ammanPatient);
    }

    @Step("End visit for previously created patient using API")
    public void implementation2() {
        registrationPage.closeVisitUsingApi(ammanPatient);
    }

    @Step("Start <visitType> visit using API")
    public void implementation3(String visitType) {
        ammanPatient.setVisitType(visitType);
        registrationPage.startVisitUsingApi(ammanPatient);
    }

    @Step("Verify Legal Rep Details after Save")
    public void implementation4() {
        registrationPage.verifyLegalRepAfterSave();
    }

    @Step("Verify caretaker details after save")
    public void implementation5() {
        registrationPage.verifyCaretakerAfterSave();
    }

    @Step("Verify patient id documents after save")
    public void implementation6() {
        registrationPage.verifyIDDocumentsAfterSave();
    }

    @Step("Verify the patient details")
    public void verifyPatientDetails() {
        registrationPage.verifyPatientDetails();
    }

    @Step("Verify patient identifier begins with nationality code <countryCode> and ends with gender code <genderCode>")
    public void verifyPatientIdentifier(String countryCode, String genderCode) {
        String actualCountryCode = Fields.patientIdentifier.getPatientAttribute().getValue().substring(0, 2);
        String actualGenderCode = Fields.patientIdentifier.getPatientAttribute().getValue().substring(8);
        Assert.assertTrue("Identifier country code is not as expected", actualCountryCode.equals(countryCode));
        Assert.assertTrue("Identifier gender code is not as expected", actualGenderCode.equals(genderCode));
    }

    @Step({"Verify below sections are hidden by default in Registration page <table>", "Verify below sections are hidden in Registration page <table>"})
    public void verifyElementsHidden(Table table) {
        List<TableRow> tableRows = table.getTableRows();
        for (TableRow row : tableRows) {
            String selectedRow = row.getCell("SECTION");
            Assert.assertFalse(String.format("%s is not hidden", selectedRow), isElementPresent(selectedRow));
        }
    }

    @Step({"Verify below sections are visible by default in Registration page <table>", "Verify below sections are visible in Registration page <table>"})
    public void verifyElementsVisible(Table table) {
        List<TableRow> tableRows = table.getTableRows();
        for (TableRow row : tableRows) {
            String selectedRow = row.getCell("SECTION");
            Assert.assertTrue(String.format("%s is not visible", selectedRow), isElementPresent(selectedRow));
        }
    }

    private Boolean isElementPresent(String titleID) {
        List<WebElement> sectionList = registrationPage.registrationSections;
        for (WebElement section : sectionList) {
            String sectionHeaderText = "";
            try {
                sectionHeaderText = section.findElement(By.cssSelector("strong")).getText();
            } catch (Exception e) {
            }

            if (sectionHeaderText.equalsIgnoreCase(titleID)) {
                return true;
            }
        }
        return false;
    }
}
