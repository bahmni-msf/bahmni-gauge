package org.bahmni.gauge.common.printforms;

import com.thoughtworks.gauge.Gauge;
import org.bahmni.gauge.common.BahmniPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

import java.util.LinkedList;
import java.util.List;

public class PrintFormsPage extends BahmniPage {

    @FindBy(xpath = "//li//a[@class=\"conceptName\"]")
    private List<WebElement> listofFormsAvaiable;

    @FindBy(xpath = "//div[@class=\"formName\"]")
    private WebElement selectedForm;

    @FindBy(xpath = "//button[text()=\"Form\"]")
    private WebElement formTab;

    @FindBy(xpath = "//button[text()=\"Code Sheet\"]")
    private WebElement codeSheetTab;

    @FindBy(xpath = "//button[@class=\"print-button\"]")
    private WebElement printButton;

    @FindBy(xpath = "//div[@class=\"code-sheet-name\"]")
    private WebElement codeSheetTitle;


    public List<String> getListofFormsDisplayed() {

        List<String> actualForms = new LinkedList<>();

        Gauge.writeMessage("Actual Forms Available :");

        for (WebElement form : listofFormsAvaiable) {

            actualForms.add(form.getText());
        //    Gauge.writeMessage(form.getText());
        }

        return actualForms;
    }


    public boolean validateSkeleton(String formName) {

        selectFormFromTheList(formName);
        waitForElementOnPagewithTimeout(By.xpath("//div[@class=\"formName\"]"), 10);

        return selectedForm.getText().equals(formName) && formTab.isDisplayed() && codeSheetTab.isDisplayed() && printButton.isDisplayed();
    }

    private void selectFormFromTheList(String formName) {

        for (WebElement element : listofFormsAvaiable) {

            if (element.getText().equals(formName))
                element.click();
            break;
        }

    }

    public boolean validateActiveTab(String tabName) {

        if(tabName.equals("form" ))
            return formTab.getAttribute("class").contains("active");
        else
            return codeSheetTab.getAttribute("class").contains("active");

    }

    public void clickOnCodeSheet() {
        codeSheetTab.click();
    }

    public boolean checkTitleOfCodeSheet(String formName) {
        return codeSheetTitle.getText().equals("Code Sheet: " + formName);
    }
}
