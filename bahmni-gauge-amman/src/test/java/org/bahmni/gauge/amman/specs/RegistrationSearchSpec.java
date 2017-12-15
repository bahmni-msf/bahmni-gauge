package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Step;
import org.bahmni.gauge.amman.registration.AmmanRegistrationSearch;
import org.bahmni.gauge.amman.registration.domain.Fields;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.openqa.selenium.By;

public class RegistrationSearchSpec {

    private AmmanRegistrationSearch registrationSearch = (AmmanRegistrationSearch) PageFactory.get(AmmanRegistrationSearch.class);

    @BeforeClassSteps
    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Search previously created patient with identifier")
    public void searchPreviousCreatedPatientWithIdentifier() {
        registrationSearch.searchByIdentifier(Fields.patientIdentifier.getPatientAttribute().getValue());
    }

    @Step("Search previously created patient with patient name")
    public void searchPreviouslyCreatedPatientWithName() {
        registrationSearch.searchByName(Fields.firstName.getPatientAttribute().getValue());
    }

    @Step("Search previously created patient with Country")
    public void searchPreviouslyCreatedPatientWithCountry() {
        registrationSearch.searchByCountry(Fields.country.getPatientAttribute().getValue());
    }

    @Step("Search previously created patient with Name in Arabic")
    public void searchPreviouslyCreatedPatientWithNameInArabic() {
        registrationSearch.searchByCustomAttribute(Fields.givenNameArabic.getPatientAttribute().getValue());
    }

    @Step("Verify previous patient details is listed in search result")
    public void validatePreviousPatientSearchResults() {
        registrationSearch.verifySearchResults();
    }

    @Step("Click on previous patient id link from search results")
    public void clickOnPreviousPatientLink() {
        String patientID = Fields.patientIdentifier.getPatientAttribute().getValue();
        registrationSearch.findElement(By.xpath(".//a[contains(text(),\"" + patientID + "\")]")).click();
    }

    @Step("Verify Create New button is displayed")
    public void verifyCreateNewIsDisplayed() {
        registrationSearch.verifyCreateNewIconIsDisplayed();
    }

}
