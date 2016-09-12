package org.bahmni.gauge.common.specs;

import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.registration.RegistrationSearch;
import org.bahmni.gauge.common.registration.domain.Patient;
import org.bahmni.gauge.rest.BahmniRestClient;
import org.bahmni.gauge.common.PageFactory;
import org.bahmni.gauge.common.registration.RegistrationFirstPage;
import org.openqa.selenium.WebDriver;

public class RegistrationFirstPageSpec {

	private final WebDriver driver;

	public RegistrationFirstPage registrationFirstPage;

	public RegistrationFirstPageSpec() {
		this.driver = DriverFactory.getDriver();
		this.registrationFirstPage = PageFactory.getRegistrationFirstPage();
	}

	@BeforeClassSteps
	public void waitForAppReady() {
		new BahmniPage().waitForSpinner(driver);
	}

	@Step("On the new patient creation page")
	public void navigateToPatientCreatePage() {
		driver.get(RegistrationFirstPage.URL);
	}

	@Step("Create the following patient <table>")
	public void createPatients(Table table) throws Exception {
		registrationFirstPage.createPatients(table);
	}

	@Step("Create patient with manual id <table>")
	public void createPatientWithId(Table table) throws Exception {
		registrationFirstPage.createPatientWithId(table);
	}

	@Step("Create the following patient with ID as recently created Patient <table>")
	public void createPatientsWithExistingID(Table table) throws Exception {
		RegistrationSearch registrationSearch = PageFactory.getRegistrationSearchPage();
		String recentlyCreatedPatientID = registrationSearch.getPatientFromSpecStore().getIdNumber();
		table.getTableRows().get(0).addCell("idNumber", recentlyCreatedPatientID.toString());
		table.getColumnNames().add(1,"idNumber");
		registrationFirstPage.createPatientWithId(table);
	}

	@Step("Click on search patient link")
	public void navigateToPatientSearch() {
		registrationFirstPage.navigateToSearchPage();
	}

	@Step("Validate that the patient edit page is opened for previously created patient")
	public void validateThePatientPageIsOpened() {
		registrationFirstPage.verifyPatientWithIdentifierAndName();
	}

	@Step("Ensure that the patient edit page is opened for previously created patient")
	public void ensureThePatientPageIsOpened() {
		registrationFirstPage.verifyPatientWithIdentifierAndName();
	}

	@Step("Start a visit <visit>")
	public void startPatientVisit(String visit) throws InterruptedException {
		registrationFirstPage.startVisit(visit);
	}

	@Step("Select check to enter patient ID manually")
	public void selectCheckToEnterPatientID() {
		registrationFirstPage.selectEnterPatientID();
	}

	@Step("Enter Visit Details Page")
	public void enterVisitDetailsPage() {
		registrationFirstPage.enterVisitDetailsPage();
	}

	@Step("Create the following patient using api <table>")
	public void createPatientThroughAPI(Table table) throws Exception {
		registrationFirstPage.createPatientUsingApi(table);
	}

	@Step("Verify the patient creation fails")
	public void verifyPatientCreationWithSameID() {
		new BahmniPage().validateSystemException(driver);
	}

}
