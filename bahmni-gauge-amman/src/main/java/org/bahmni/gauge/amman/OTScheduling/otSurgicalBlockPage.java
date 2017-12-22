package org.bahmni.gauge.amman.OTScheduling;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.WebElement;
import org.junit.Assert;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

/**
 * Created by jaseenam on 21/07/17.
 */
public class otSurgicalBlockPage extends otSchedulingPage {

    @FindBy(how = How.CSS, using = ".ng-pristine.ng-untouched.ng-invalid.ng-invalid-required")
    WebElement surgeonDropdown;

    @FindBy(how = How.CSS, using = ".location-buttons")
    public List<WebElement> otLocations;

    @FindBy(how = How.CSS, using = "input[type='datetime-local']")
    WebElement otStartDateTime;

    @FindBy(how = How.XPATH, using = "(//input[@type='datetime-local'])[2]")
    WebElement otEndDateTime;

    @FindBy(how = How.CSS, using = ".ot-nav-save")
    WebElement saveOTSurgicalBlock;

    @FindBy(how = How.CSS, using = ".ngdialog-content")
    WebElement addEditSurgeryForm;

    @FindBy(how = How.ID, using = "patientID")
    WebElement patientIDorName;

    @FindBy(how = How.ID, using = "surgicalAssistant")
    WebElement surgicalAssistant;

    @FindBy(how = How.ID, using = "anaesthetistID")
    WebElement anaesthetist;

    @FindBy(how = How.ID, using = "scrubNurseID")
    WebElement scrubNurse;

    @FindBy(how = How.ID, using = "circulatingNurseID")
    WebElement circulatingNurse;

    @FindBy(how = How.ID, using = "notesID")
    WebElement notes;

    @FindBy(how = How.ID, using = "edit-appointment")
    WebElement editAppointment;

    @FindBy(how = How.ID, using = "procedureID")
    WebElement procedure;

    @FindBy(how = How.ID, using = "estTimeHoursID")
    WebElement estHours;

    @FindBy(how = How.ID, using = "estTimeMinutesID")
    WebElement estMinutes;

    @FindBy(how = How.CSS, using = ".add")
    WebElement addSurgery;

    @FindBy(how = How.CSS, using = "input.cancel")
    WebElement cancel;

    public void selectSurgeon(String surgeon) {
        Select surgeonDrpdwn = new Select(surgeonDropdown);
        surgeonDrpdwn.selectByVisibleText(surgeon);
    }

    public void selectLocation(String ot) {
        for (WebElement otLocation : otLocations) {
            if (otLocation.getText().equalsIgnoreCase(ot)) {
                waitForSpinner(driver);
                otLocation.click();
                break;
            }
        }
    }

    public void selectDateTime(String startdate, String stime, String enddate, String etime) {
        if (startdate.contains("NOW")) {
            startdate = todayDateAsString();
        }
        if (enddate.contains("NOW")) {
            enddate = todayDateAsString();
        }
        startdate = startdate.replace("/", "");
        stime = stime.replace(":", "");
        stime = stime.replace(" ", "");

        enddate = enddate.replace("/", "");
        etime = etime.replace(":", "");
        etime = etime.replace(" ", "");

        otStartDateTime.sendKeys(startdate);
        otStartDateTime.sendKeys(Keys.TAB);
        otStartDateTime.sendKeys(stime);

        otEndDateTime.sendKeys(enddate);
        otEndDateTime.sendKeys(Keys.TAB);
        otEndDateTime.sendKeys(etime);
    }

    public String DateTimeToString(String startdate, String stime) {
        if (startdate.contains("NOW")) {
            startdate = todayDateAsString();
        }

        startdate = startdate + ", " + stime;
        return startdate;
    }

    public void clickSave() {
        click(saveOTSurgicalBlock);
    }

    public void clickAddSurgery() {
        click(findButtonByText("Add Surgery"));
        waitForVisibilityOfElementOnPage(addEditSurgeryForm);
    }

    public void addSurgery(Table table) {
        List<TableRow> surgeries = table.getTableRows();
        for (TableRow surgery : surgeries) {
            clickAddSurgery();
            fillAutocomplete(patientIDorName, surgery.getCell("Patient ID or Name"));
            WebElement otherSurgeon = driver.findElement(By.xpath(".//*[@id='ngdialog1']/div[2]/form/div/p[5]/select"));
            new Select(otherSurgeon).selectByVisibleText(surgery.getCell("Other Surgeon"));
            surgicalAssistant.sendKeys(surgery.getCell("Surgical Assistant"));
            anaesthetist.sendKeys(surgery.getCell("Anaesthetist"));
            scrubNurse.sendKeys(surgery.getCell("Scrub Nurse"));
            circulatingNurse.sendKeys(surgery.getCell("Circulating Nurse"));
            notes.sendKeys(surgery.getCell("Notes"));
            waitForSpinner(driver);
            addSurgery.click();
            waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".ngdialog-content")));
        }
    }

    public void fillAutocomplete(WebElement autoComplete, String value) {
        waitForVisibilityOfElementOnPage(autoComplete);
        autoComplete.sendKeys(value);
        List<WebElement> patientSearchResults = driver.findElements(By.className("ui-corner-all"));
        waitForElement(driver, ExpectedConditions.visibilityOfAllElements(patientSearchResults));
        autoComplete.sendKeys(Keys.DOWN, Keys.RETURN);
    }

    public static void editSurgicalBlock(Table table, List<String> columnNames) {
    }

    public void editSurgery(Table table) {
        editAppointment.click();
        TableRow requiredRow = null;
        for (TableRow row : table.getTableRows()) {
            if (row.getCell("Name").contains(patientIDorName.getText())) {
                requiredRow = row;
                break;
            }
        }
        Assert.assertEquals(requiredRow.getCell("Procedure(s)"), procedure.getAttribute("value"));
        Assert.assertEquals(requiredRow.getCell("Est Time Hours"), estHours.getAttribute("value"));
        Assert.assertEquals(requiredRow.getCell("Est Time Minutes"), estMinutes.getAttribute("value"));
        waitForSpinner(driver);
        cancel.click();
    }

    private String todayDateAsString() {
        DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
        Date today = new Date();
        return dateFormat.format(today);
    }

    public int verifyBlockdata(String surgeon, String ot, String startdate, String starttime, String enddate, String endtime) {
        if (surgeonDropdown.getText().equalsIgnoreCase(surgeon)) {
            for (WebElement otloc : otLocations) {
                if (otloc.isSelected()) {
                    if (otloc.getText().equalsIgnoreCase(ot)) {
                        if (otStartDateTime.getText().equalsIgnoreCase(DateTimeToString(startdate, starttime))) {
                            if (otEndDateTime.getText().equalsIgnoreCase(DateTimeToString(enddate, endtime))) {
                                return 1;
                            } else {
                                Assert.fail("End Time is different");
                            }
                        } else {
                            Assert.fail("Start Time is different");
                        }


                    } else {
                        Assert.fail("OT location is different");
                    }
                }
            }
        } else {
            Assert.fail("Surgeon name is different");
        }
        return 0;
    }
}
