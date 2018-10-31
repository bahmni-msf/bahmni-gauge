package org.bahmni.gauge.common.formBuilder;

import org.bahmni.gauge.common.BahmniPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

import java.util.List;

public class FormBuilderPage extends BahmniPage {

	public static final String URL = BASE_URL.concat("/implementer-interface#/form-builder");

	@FindBy(how = How.CSS, using = ".btn--highlight")
	public WebElement createForm;

	@FindBy(how= How.CSS, using = ".form-name")
	public WebElement formNameInput;

	@FindBy(how= How.CSS, using = "tbody")
	public WebElement formTableBody;

	@FindBy(how= How.CSS, using = ".button")
	public WebElement btnCreateForm;

	@FindBy(className = "control-list")
	private List<WebElement> controlList;

	@FindBy(className = "cell")
	private List<WebElement> controlHolderList;

	@FindBy(xpath = "//div[@class='grid']//div[@class='grid']//div[@class=\"cell\"]")
	private List<WebElement> sectionControlHoldersList;





	public void clickCreateForm() {
		createForm.click();
	}

	public void enterName(String formName) {
		formNameInput.sendKeys(formName);
		btnCreateForm.click();
		waitForSpinner();
	}

    public void clickOnAction(String versionNumber, String formName) {
		WebElement icon = findFormIcon(formName, versionNumber);
		icon.click();
    }

    public WebElement findFormByNameAndVersion(String versionNum, String formName) {
		List<WebElement> formList = formTableBody.findElements(By.cssSelector("tr"));
		for (int i = 0; i < formList.size(); i++) {
			if (formList.get(i).findElements(By.cssSelector("td")).get(0).getText().equals(formName) &&
					formList.get(i).findElements(By.cssSelector("td")).get(1).getText().equals(versionNum)) {


				return formList.get(i);
			}
		}
		return null;
	}




	public WebElement findFormIcon(String formName, String versionNumber) {
		List<WebElement> formList = formTableBody.findElements(By.cssSelector("tr"));
		for(int i = 0; i < formList.size(); i++) {
			if(formList.get(i).findElements(By.cssSelector("td")).get(0).getText().equals(formName) &&
					formList.get(i).findElements(By.cssSelector("td")).get(1).getText().equals(versionNumber)){
				return formList.get(i).findElement(By.cssSelector("a"));
			}
		}
		return null;
	}

	public void DragandDropControl(String controlName) {



		WebElement control= findControlByName(controlName);
		WebElement controlHolder=findEmptyControlHolderInGrid();
		DragAndDropInHTML5(control,controlHolder);
	}

	private WebElement findEmptyControlHolderInGrid() {

		for (WebElement element:controlHolderList
			 ) {

			if(!checkIfCellBelongsToSection(element))
				return element;

		}
		return null;

	}

	private boolean checkIfCellBelongsToSection(WebElement element){

		if (sectionControlHoldersList.contains(element))
			return true;
		else
			return false;

	}

	private WebElement findControlByName(String controlName) {
		for (WebElement control : controlList) {

			if(control.getText().equalsIgnoreCase(controlName))
			   return control;
		}
		return null;

	}
}
