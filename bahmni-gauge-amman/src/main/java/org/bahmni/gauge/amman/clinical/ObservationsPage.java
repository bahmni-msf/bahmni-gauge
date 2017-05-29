package org.bahmni.gauge.amman.clinical;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.Select;

import java.util.List;

public class ObservationsPage extends org.bahmni.gauge.common.clinical.ObservationsPage {

    @FindBy(how = How.CSS, using = ".leaf-observation-node")
    public List<WebElement> observationNodes;

    @Override
    public void selectTemplate(String templateName) {
        int formSelected = 0;
        List <WebElement> templateList = driver.findElements(By.cssSelector("section.concept-set-panel-left  li .concept-set-name"));
        if (templateList.size()>0) {
            for (WebElement form : templateList) {
                if (form.getText().contains(templateName)) {
                    form.click();
                    formSelected = 1;
                    break;
                }
            }
        }
        if (formSelected==0){
            clickTemplateButton();
            List<WebElement> allForms = templatePanel.findElements(By.tagName("button"));

            for (WebElement form : allForms) {
                if (form.getText().contains(templateName)) {
                    form.click();
                    formSelected = 1;
                    break;
                }
            }
        }
        if(formSelected==0) {
            Assert.fail("Form " + templateName + " not found");
        }
    }


    public void fillTemplateData(Table table) {
        List<TableRow> rows = table.getTableRows();
        for (TableRow row : rows) {
            boolean fieldFound = false;
            String fieldName = row.getCell("FIELD").trim();
            String value = row.getCell("VALUE");
            for (WebElement observationNode : observationNodes) {
                String observLabel = observationNode.findElement(By.tagName("label")).getText().trim();
                if (observLabel.equals(fieldName)) {
                    fieldFound = true;
                    if (hasTag(observationNode, "input")) {
                        WebElement autoComplete = observationNode.findElement(By.tagName("input"));
                        if (autoComplete.getAttribute("class").contains("ui-autocomplete-input"))
                            fillAutocomplete(autoComplete, value);
                        else if (autoComplete.getAttribute("class").contains("input ng-pristine ng-untouched ng-valid")) {
                            fillAutocomplete(autoComplete, value);
                        }
                        else {
                            observationNode.findElement(By.tagName("input")).sendKeys(value, Keys.TAB);
                        }
                    } else if (hasTag(observationNode, "textarea")) {
                        observationNode.findElement(By.tagName("textarea")).sendKeys(value);
                    } else if (hasTag(observationNode, "select")) {
                        new Select(observationNode.findElement(By.tagName("select"))).selectByVisibleText(value);
                    } else if (hasTag(observationNode, "button")) {
                        List<WebElement> buttons = observationNode.findElements(By.tagName("button"));
                        String[] multiSelect = value.split(";");
                        for (String val : multiSelect) {
                            for (WebElement button : buttons) {
                                if (button.getText().contains(val)) {
                                    try {
                                        button.click();
                                        break;
                                    } catch (WebDriverException e) {
                                        JavascriptExecutor js = ((JavascriptExecutor) driver);
                                        js.executeScript("scrollBy(0,1000)");
                                        Actions actions = new Actions(driver);
                                        actions.moveToElement(button).click().build().perform();
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
            }
            if (!fieldFound) {
                Assert.fail("Field " + fieldName + " not found or disabled");
            }
        }
    }

    private boolean hasTag(WebElement answer, String input) {
        boolean val = true;
        try {
            answer.findElement(By.tagName(input));
        } catch (NoSuchElementException e) {
            val = false;
        }
        return val;
    }

    public void fillAutocomplete(WebElement autoComplete, String value){
            autoComplete.sendKeys(value);
            autoComplete.sendKeys(Keys.DOWN);
            waitForElementOnPage(By.xpath(".//a[text()=\"" + value + "\"]"));
            findElement(By.xpath(".//a[text()=\"" + value + "\"]")).click();
    }

    public void verifyFormSaved(Table table) {
        List<TableRow> rows = table.getTableRows();
        for (TableRow row : rows) {
            String formName = row.getCell("FORM").trim();
            Boolean isDisabled = getDisabledValue(formName);
            Assert.assertTrue(isDisabled);
        }
    }
}
