package org.bahmni.gauge.amman.registration;

import com.thoughtworks.gauge.TableRow;
import org.bahmni.gauge.amman.registration.domain.AmmanPatient;
import org.bahmni.gauge.amman.registration.domain.Fields;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.registration.RegistrationSearch;
import org.bahmni.gauge.common.registration.domain.Patient;
import org.bahmni.gauge.data.BahmniTable;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.Select;

import java.util.List;

public class AmmanRegistrationSearch extends AmmanRegistrationPage{

	@FindBy(how= How.CSS, using = ".fa-home")
    public WebElement iconHome;
	
	@FindBy(how= How.CSS, using = ".fa-search")
    public WebElement iconSearch;
	
	@FindBy(how= How.CSS, using = "i.fa-plus")
    public WebElement iconCreateNew;
	
	@FindBy(how= How.CSS, using = "#registrationNumber")
    public WebElement txtRegistration;
	
	@FindBy(how= How.CSS, using = "#name")
    public WebElement txtName;

	@FindBy(how= How.CSS, using = "#addressFieldValue")
	public WebElement txtCountry;
	
	@FindBy(how= How.CSS, using = "#identifierPrefix")
    public List<WebElement> txtIdentifier;
	
	@FindBy(how= How.CSS, using = ".search-patient-id .reg-srch-btn")
    public WebElement btnIdentifierSearch;

	@FindBy(how = How.CSS, using = ".search-seperator-r .reg-srch-btn")
	public WebElement btnRegSearch;
	
	@FindBy(how= How.CSS, using = ".registraition-search-results-container > table")
    public WebElement gridSearchResults;

	@FindBy(how= How.CSS, using = "#customAttribute")
	public WebElement custom_attribute;

    public void clickSearch() {
    	iconSearch.click();
    }

    public void clickHome() {
    	iconHome.click();
    }

    public void clickCreateNew() {
    	iconCreateNew.click();
    }

    public void verifyCreateNewIconIsDisplayed(){
    		Assert.assertTrue(driver.findElements(By.cssSelector("i.fa-plus")).size() != 0);
	}

    public void enterName(String name) {
    	txtName.sendKeys(name,Keys.ENTER);
    }

    public void searchByExactIdentifier(String prefix, String id){
	    selectPrefix(prefix);

	    txtRegistration.sendKeys(id);
	    btnIdentifierSearch.click();
    }

	private void selectPrefix(String prefix) {
		if(txtIdentifier.size()>0){
			new Select(txtIdentifier.get(0)).selectByVisibleText(prefix);
		}
	}

	public void searchByIdentifier(String id){
		txtRegistration.sendKeys(id);
		btnIdentifierSearch.click();
    }

	public void searchByName(String name){
		txtName.sendKeys(name);
		btnRegSearch.click();
	}

	public void searchByCountry(String country) {
		txtCountry.sendKeys(country);
		btnRegSearch.click();
	}

	public void searchByCustomAttribute(String attribute){
		custom_attribute.sendKeys(attribute);
		btnRegSearch.click();
	}

	public void getFirstResult() {
		waitForElementOnPage(gridSearchResults);
		gridSearchResults.findElements(By.tagName("a")).get(0).click();
	}

	public void verifySearchResults(){
		BahmniTable dataOnUI=extractTableDataFrom(By.className("table"));
		String patientID = Fields.getPatientAttribute("patientIdentifier").getValue();
		String patientName = Fields.getPatientAttribute("firstName").getValue() + " " + Fields.getPatientAttribute("lastName").getValue();
		String givenNameLocal = Fields.getPatientAttribute("givenNameArabic").getValue();
		String familyNameLocal = Fields.getPatientAttribute("familyNameArabic").getValue();
		String patientGender = Fields.getPatientAttribute("gender").getValue();
		String patientAge = Fields.getPatientAttribute("age").getValue();
		String patientCountry = Fields.getPatientAttribute("country").getValue();

		for(TableRow row : dataOnUI.getTableRows()){
			if(row.getCell("ID").equals(patientID))
			{

				Assert.assertEquals("Name dont match",patientName,row.getCell("Name"));
				Assert.assertEquals("Gender dont match",patientGender.equals("Male")?"M":patientGender.equals("Female")?"F":"O",row.getCell("Gender"));
				Assert.assertEquals("Age dont match",patientAge,row.getCell("Age"));
				if(row.getCell("Given Name Local")!=null) {
					Assert.assertEquals("Given Name Local dont match", givenNameLocal, row.getCell("Given Name Local"));
				}
				if(row.getCell("Family Name Local")!=null) {
					Assert.assertEquals("Family Name Local dont match", familyNameLocal, row.getCell("Family Name Local"));
				}
				Assert.assertEquals("Country dont match",patientCountry,row.getCell("Country"));
			}
		}
	}
	public void verifySearchResults(String text, String column) {
		BahmniTable dataOnUI=extractTableDataFrom(By.className("table"));
		Assert.assertTrue("Column values dont match",dataOnUI.doesColumnOfEachRowContainsValue(text,column));
	}

}
