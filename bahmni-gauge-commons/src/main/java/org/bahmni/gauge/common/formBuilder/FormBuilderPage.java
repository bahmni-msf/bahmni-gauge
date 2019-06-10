package org.bahmni.gauge.common.formBuilder;

import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;
import com.thoughtworks.gauge.Gauge;
import org.bahmni.gauge.common.BahmniPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

import java.io.FileReader;
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

	public void clickOnDownload(String versionNumber, String formName) {
		try {
            WebElement icon = findDownloadIcon(formName, versionNumber);
            icon.click();
            Thread.sleep(1000);
        }
        catch (Exception e){
		    e.printStackTrace();
        }
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

	public WebElement findDownloadIcon(String formName, String versionNumber) {
		List<WebElement> formList = formTableBody.findElements(By.cssSelector("tr"));
		for(int i = 0; i < formList.size(); i++) {
			if(formList.get(i).findElements(By.cssSelector("td")).get(0).getText().equals(formName) &&
					formList.get(i).findElements(By.cssSelector("td")).get(1).getText().equals(versionNumber)){

			    WebElement element= formList.get(i).findElement(By.cssSelector(".fa-download"));
				return element;
			}
		}
		return null;
	}


	public String getLastFormDetails() {
        try {
            FileReader filereader = new FileReader("/Users/bsantosh/projects/bahmni/bahmni-gauge/bahmni-gauge-amman/src/main/resources/forms.csv");
            CSVReader csvReader = new CSVReaderBuilder(filereader)
                    .withSkipLines(1)
                    .build();
            List<String[]> allData = csvReader.readAll();
            String [] formdetails=allData.get(allData.size() -1);
            System.out.println(formdetails[0] + "_" + formdetails[1]);
            Gauge.writeMessage(formdetails[0] + "_" + formdetails[1]);
            return formdetails[0] + "_" + formdetails[1];

        } catch (Exception e) {

            e.printStackTrace();

        }

        return null;
    }

}
