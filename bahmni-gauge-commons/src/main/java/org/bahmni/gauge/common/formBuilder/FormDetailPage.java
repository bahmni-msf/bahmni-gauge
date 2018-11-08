package org.bahmni.gauge.common.formBuilder;

import org.bahmni.gauge.common.BahmniPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

import java.util.List;


public class FormDetailPage extends BahmniPage {
    @FindBy(how = How.CSS, using = "button")
    public WebElement editButton;

    @FindBy(how = How.CSS, using = ".button")
    public WebElement okButton;

    @FindBy(how = How.CSS, using = ".breadcrumbs")
    public WebElement breadCrumbsGuider;

    @FindBy(how = How.CSS, using = ".publish-button")
    public WebElement publishButton;

    @FindBy(how = How.CSS, using = ".header-title")
    public WebElement formHeader;

    @FindBy(how = How.CSS, using = ".grid")
    public WebElement canvas;

    @FindBy(how = How.CSS, using = ".save-button")
    public WebElement saveButton;

    @FindBy(how = How.CSS, using = ".form-properties")
    public WebElement propertiesBody;

    @FindBy(how = How.CSS, using = ".dialog--no-header")
    public WebElement editConfirmBox;

    @FindBy(className = "control-list")
    private List<WebElement> controlList;

    @FindBy(className = "cell")
    private List<WebElement> controlHolderList;

    @FindBy(xpath = "//div[@class='grid']//div[@class='grid']//div[@class=\"cell\"]")
    private List<WebElement> sectionControlHoldersList;

    @FindBy(xpath = "//div[text()=\"Select Obs Source\"]")
    private WebElement obsControl;

    @FindBy(xpath = "//div[text()=\"Select ObsGroup Source\"]")
    private WebElement obsGroupControl;

    @FindBy(xpath = "//div[@class=\"Select-input\"]/input")
    private WebElement conceptSearchBox;

    @FindBy(xpath = "//button[@type=\"submit\"]")
    private WebElement acceptDeleteControl;

    @FindBy(xpath = "//div[@class=\"table-controls\"]//div[@class=\"form-builder-row row0\"]/div/div")
    private List<WebElement> tableControlHoldersList;


    public void clickOnEdit() {
        editButton.click();
    }

    public void clickOnOK() {
        okButton.click();
    }

    public void clickOnAcceptDeleteControl(){
        acceptDeleteControl.click();
    }

    public void clickOnFormBuilder() {
        breadCrumbsGuider.findElements(By.cssSelector("a")).get(1).click();
    }

    public void clickOnPublish() {
        publishButton.click();
    }

    public String getFormInfo() {
        return formHeader.getText();
    }

    public List<WebElement> getCanvasBodyLabelList() {
        return canvas.findElements(By.cssSelector("label"));
    }

    public void clickOnSave() {
        saveButton.click();
    }

    public void clickOnControl(WebElement control) {
        control.click();
    }

    public void clickOnProperty(String propertyType) {
        List<WebElement> allPropertyType = propertiesBody.findElements(By.cssSelector("label"));
        List<WebElement> propertyCheckBox = propertiesBody.findElements(By.cssSelector("input"));

        for (int i = 0; i < allPropertyType.size(); i++) {
            if (allPropertyType.get(i).getText().equals(propertyType)) {
                propertyCheckBox.get(i).click();
            }
        }
    }


    public WebElement getEditButton() {
        return editButton;
    }

    public void changeName(String labelName, String name) {
        List<WebElement> labelList = driver.findElements(By.tagName("label"));
        for (WebElement label : labelList) {
            if (label.getText().equals(labelName)) {
                WebElement parentElement = label.findElement(By.xpath("../.."));

                doubleClickOnLabel(label);

                WebElement childElement = parentElement.findElement(By.cssSelector(".form-builder-label"));

                childElement.clear();
                childElement.sendKeys(name);

                canvas.click();
            }
        }
    }

    public void doubleClickOnLabel(WebElement label) {
        Actions action = new Actions(driver).doubleClick(label);
        action.build().perform();
    }

    public boolean isPropertyChecked(String propertyType) {
        List<WebElement> allPropertyType = propertiesBody.findElements(By.cssSelector("label"));
        List<WebElement> propertyCheckBox = propertiesBody.findElements(By.cssSelector("input"));

        for (int i = 0; i < allPropertyType.size(); i++) {
            if (allPropertyType.get(i).getText().equals(propertyType) &&
                    propertyCheckBox.get(i).isSelected()) {
                return true;
            }
        }
        return false;
    }

    public List<WebElement> getAllButton() {
        return driver.findElement(By.cssSelector(".breadcrumb-wrap")).findElements(By.cssSelector("button"));
    }

    public WebElement findCanvasTitle() {
        return driver.findElement(By.cssSelector(".canvas-title"));
    }

    public WebElement getEditConfirmBox() {
        return editConfirmBox;
    }

    public void DragandDropControl(String controlName) {


        WebElement control = findControlByName(controlName);
        WebElement controlHolder = findEmptyControlHolderInGrid();
        dragAndDropInHTML5(control, controlHolder);
    }

    private WebElement findEmptyControlHolderInGrid() {

        for (WebElement element : controlHolderList
                ) {

            if (!checkIfCellBelongsToSectionOrSection(element))
                return element;

        }
        return null;

    }

    private boolean checkIfCellBelongsToSectionOrSection(WebElement element) {

        if (sectionControlHoldersList.contains(element) || tableControlHoldersList.contains(element))
            return true;
        else
            return false;

    }

    private WebElement findControlByName(String controlName) {
        for (WebElement control : controlList) {

            if (control.getText().equalsIgnoreCase(controlName))
                return control;
        }
            return null;

    }

    public void associateConcept(String conceptName, String controlType) {

        Actions actions = new Actions(driver);

        if (controlType.equalsIgnoreCase("obs"))
            obsControl.click();
        else
            obsGroupControl.click();
         actions.moveToElement(conceptSearchBox).click().sendKeys(conceptName).build().perform();
         waitForSpinnerOnSearchConcept(driver);
         actions.moveToElement(findElement(By.className("Select-menu-outer"))).click().build().perform();
   }

    public boolean checkIfControlIsNotEditable(WebElement control) {

        control.click();
        return driver.findElement(By.xpath("//div[contains(@class,\"is-disabled\")]")).isDisplayed();
    }

    public void DragandDropObsToTable(String column) {

        WebElement control = findControlByName("obs");
        WebElement controlHolder = findEmptyControlHolderInTable(column);
        dragAndDropInHTML5(control,controlHolder);


    }

    private WebElement findEmptyControlHolderInTable(String column) {

        if (column.equalsIgnoreCase("left"))
            return tableControlHoldersList.get(0);
        else
            return tableControlHoldersList.get(1);
    }
}
