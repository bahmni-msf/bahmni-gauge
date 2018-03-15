package org.bahmni.gauge.amman.clinical;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import java.util.List;

public class ObservationsPage extends org.bahmni.gauge.common.clinical.ObservationsPage {

    @FindBy(how = How.CSS, using = ".leaf-observation-node")
    public List<WebElement> observationNodes;

    @FindBy(how = How.CSS, using = ".hasLegend .collapsible-set")
    public List<WebElement> sections;

    @FindBy(how = How.ID, using = "modal-revise-button3")
    public WebElement saveBtn;

    @Override
    public void selectTemplate(String templateName) {
        int formSelected = 0;
        List<WebElement> templateList = driver.findElements(By.cssSelector("section.concept-set-panel-left  li .concept-set-name"));
        if (templateList.size() > 0) {
            for (WebElement form : templateList) {
                if (form.getText().startsWith(templateName)) {
                    if (!(templateName.equals("Vital Signs") && form.getText().equals("Baseline Vital Signs"))) {
                        form.click();
                        formSelected = 1;
                        break;
                    }
                }
            }
        }
        if (formSelected == 0) {
            clickTemplateButton();
            List<WebElement> allForms = templatePanel.findElements(By.tagName("button"));

            for (WebElement form : allForms) {
                if (form.getText().contains(templateName)) {
                    if (!(templateName.equals("Vital Signs") && form.getText().equals("Baseline Vital Signs"))) {
                        form.click();
                        formSelected = 1;
                        break;
                    }
                }
            }
        }
        if (formSelected == 0) {
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
                        if (autoComplete.getAttribute("class").contains("ui-autocomplete-input")) {
                            fillAutocomplete(autoComplete, value);
                            break;
                        } else if (autoComplete.getAttribute("class").contains("input ng-pristine ng-untouched ng-valid")) {
                            fillAutocomplete(autoComplete, value);
                            break;
                        } else {
                            WebElement inputField = observationNode.findElement(By.tagName("input"));
                            if (inputField.getText().isEmpty()) {
                                inputField.sendKeys(value, Keys.TAB);
                                break;
                            }
                        }
                    } else if (hasTag(observationNode, "textarea")) {
                        WebElement textField = observationNode.findElement(By.tagName("textarea"));
                        if (textField.getText().isEmpty()) {
                            textField.sendKeys(value);
                            break;
                        }
                    } else if (hasTag(observationNode, "select")) {
                        new Select(observationNode.findElement(By.tagName("select"))).selectByVisibleText(value);
                        break;
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

    public void verifyTemplateData(Table table) {
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
                        Assert.assertTrue(String.format("%s Data does not match", fieldName), autoComplete.getAttribute("value").equalsIgnoreCase(value));
                        break;
                    }
                } else if (hasTag(observationNode, "textarea")) {
                    WebElement textField = observationNode.findElement(By.tagName("textarea"));
                    Assert.assertTrue(String.format("%s Data does not match", fieldName), textField.getAttribute("value").equalsIgnoreCase(value));
                    break;

                } else if (hasTag(observationNode, "select")) {
                    Assert.assertTrue("Data does not match", new Select(observationNode.findElement(By.tagName("select"))).getFirstSelectedOption().getText().equalsIgnoreCase(value));
                    break;
                } else if (hasTag(observationNode, "button")) {
                    List<WebElement> buttons = observationNode.findElements(By.tagName("button"));
                    String[] multiSelect = value.split(";");
                    for (String val : multiSelect) {
                        for (WebElement button : buttons) {
                            if (button.getText().contains(val)) {
                                Assert.assertTrue("Button is not selected", button.isSelected());
                            }
                        }
                    }
                    break;
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

    private boolean hasClass(WebElement answer) {
        boolean val = true;
        try {
            answer.findElement(By.cssSelector(".compuptedValue"));
        } catch (NoSuchElementException e) {
            val = false;
        }
        return val;
    }

    private boolean hasElement(WebElement parentElement) {
        boolean val = true;
        try {
            parentElement.findElement(By.cssSelector(".mylegend"));
        } catch (NoSuchElementException e) {
            val = false;
        }
        return val;
    }

    public void fillAutocomplete(WebElement autoComplete, String value) {
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

    public void verifyFormIsAddMore(String templateName) {
        clickTemplateButton();
        List<WebElement> allForms = templatePanel.findElements(By.tagName("button"));
        for (WebElement form : allForms) {
            if (form.getText().contains(templateName)) {
                Boolean isAddMore = isAttribtuePresent(form, "disabled");
                Assert.assertFalse(isAddMore);
                break;
            }
        }
        clickTemplateButton();
    }

    private boolean isAttribtuePresent(WebElement element, String attribute) {
        Boolean result = false;
        try {
            String value = element.getAttribute(attribute);
            if (value != null) {
                result = true;
            }
        } catch (Exception e) {
        }
        return result;
    }


    public void fillTemplateData(Table table, String section) {
        List<TableRow> rows = table.getTableRows();
        WebElement selectedSection = null;
        for (WebElement eachSection : sections) {
            if (hasElement(eachSection)) {
                String sectionTitle = eachSection.findElement(By.cssSelector(".mylegend")).getText();
                if (sectionTitle.equalsIgnoreCase(section)) {
                    selectedSection = eachSection;
                    break;
                }
            }
        }
        if (selectedSection != null) {
            List<WebElement> obsNode = selectedSection.findElements(By.cssSelector(".leaf-observation-node"));
            for (TableRow row : rows) {
                boolean fieldFound = false;
                String fieldName = row.getCell("FIELD").trim();
                String value = row.getCell("VALUE");
                for (WebElement observationNode : obsNode) {
                    String observLabel = observationNode.findElement(By.tagName("label")).getText().trim();
                    if (observLabel.equals(fieldName)) {
                        fieldFound = true;
                        if (hasTag(observationNode, "input")) {
                            WebElement autoComplete = observationNode.findElement(By.tagName("input"));
                            if (autoComplete.getAttribute("class").contains("ui-autocomplete-input")) {
                                fillAutocomplete(autoComplete, value);
                                break;
                            } else if (autoComplete.getAttribute("class").contains("input ng-pristine ng-untouched ng-valid")) {
                                fillAutocomplete(autoComplete, value);
                                break;
                            } else {
                                WebElement inputField = observationNode.findElement(By.tagName("input"));
                                if (inputField.getText().isEmpty()) {
                                    inputField.sendKeys(value, Keys.TAB);
                                    break;
                                }
                            }
                        } else if (hasTag(observationNode, "textarea")) {
                            WebElement textField = observationNode.findElement(By.tagName("textarea"));
                            if (textField.getText().isEmpty()) {
                                textField.sendKeys(value);
                                break;
                            }
                        } else if (hasTag(observationNode, "select")) {
                            new Select(observationNode.findElement(By.tagName("select"))).selectByVisibleText(value);
                            break;
                        } else if (hasTag(observationNode, "button")) {
                            List<WebElement> buttons = observationNode.findElements(By.tagName("button"));
                            String[] multiSelect = value.split(";");
                            for (String val : multiSelect) {
                                for (WebElement button : buttons) {
                                    if (button.getText().contains(val)) {
                                        try {
                                            button.click();
                                            break;
                                        } catch (WebDriverException ee) {
                                            JavascriptExecutor js = ((JavascriptExecutor) driver);
                                            js.executeScript("scrollBy(0,1000)");
                                            Actions actions = new Actions(driver);
                                            actions.moveToElement(button).click().build().perform();
                                            break;
                                        }
                                    }
                                }
                            }
                            break;
                        }
                    }
                }
                if (!fieldFound) {
                    Assert.fail("Field " + fieldName + " not found or disabled");
                }
            }
        } else if (selectedSection == null) {
            Assert.fail("Section " + section + " not found or disabled");
        }
    }

    public void verifyTemplateData(Table table, String section) {
        List<TableRow> rows = table.getTableRows();
        WebElement selectedSection = null;
        for (WebElement eachSection : sections) {
            String sectionTitle = eachSection.findElement(By.cssSelector(".mylegend")).getText();
            if (sectionTitle.equalsIgnoreCase(section)) {
                selectedSection = eachSection;
                break;
            }
        }
        if (selectedSection != null) {
            List<WebElement> obsNode = selectedSection.findElements(By.cssSelector(".leaf-observation-node"));
            List<WebElement> obsNodeCalculated = selectedSection.findElements(By.cssSelector(".hasLegend .collapsible-set"));
            for (WebElement element : obsNodeCalculated) {
                obsNode.add(element);
            }
            for (TableRow row : rows) {
                boolean fieldFound = false;
                String fieldName = row.getCell("FIELD").trim();
                String value = row.getCell("VALUE");
                for (WebElement observationNode : obsNode) {
                    String observLabel = observationNode.findElement(By.tagName("label")).getText().trim();
                    if (observLabel.equals(fieldName)) {
                        fieldFound = true;
                        if (hasClass(observationNode)) {
                            Assert.assertTrue(String.format("%s Data does not match", fieldName), observationNode.findElement(By.cssSelector(".compuptedValue")).getText().equalsIgnoreCase(value));
                            break;
                        }
                        if (hasTag(observationNode, "input")) {
                            WebElement autoComplete = observationNode.findElement(By.tagName("input"));
                            Assert.assertTrue(String.format("%s Data does not match", fieldName), autoComplete.getAttribute("value").equalsIgnoreCase(value));
                            break;
                        } else if (hasTag(observationNode, "textarea")) {
                            WebElement textField = observationNode.findElement(By.tagName("textarea"));
                            Assert.assertTrue(String.format("%s Data does not match", fieldName), textField.getAttribute("value").equalsIgnoreCase(value));
                            break;

                        } else if (hasTag(observationNode, "select")) {
                            Assert.assertTrue("Data does not match", new Select(observationNode.findElement(By.tagName("select"))).getFirstSelectedOption().getText().equalsIgnoreCase(value));
                            break;
                        } else if (hasTag(observationNode, "button")) {
                            List<WebElement> buttons = observationNode.findElements(By.tagName("button"));
                            String[] multiSelect = value.split(";");
                            for (String val : multiSelect) {
                                for (WebElement button : buttons) {
                                    if (button.getText().contains(val)) {
                                        Assert.assertTrue(String.format("%s Button is not selected", val), button.getAttribute("class").contains("active"));
                                        break;
                                    }
                                }
                            }
                            break;
                        }
                    }
                }
                if (!fieldFound) {
                    Assert.fail("Field " + fieldName + " not found or disabled");
                }
            }
        } else if (selectedSection == null) {
            Assert.fail("Section " + section + " not found or disabled");
        }
    }
        public void clickSaveConfirmPopup() {
            boolean foundAlert = false;
            try {
                waitForElement(driver, ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
                saveBtn.click();
                waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
                foundAlert = true;
            } catch (TimeoutException eT0) {
                foundAlert = false;
            }
        }
    }


