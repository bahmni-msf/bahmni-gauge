package org.bahmni.gauge.amman.OTScheduling;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.bahmni.gauge.amman.registration.domain.PatientAttribute;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;

import java.util.List;

/**
 * Created by jaseenam on 21/07/17.
 */
public class otSurgicalBlockPage extends otSchedulingPage{

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

    @FindBy(how = How.CSS, using = ".create-surgical-title>button")
    WebElement addSurgeryBtn;

    @FindBy(how = How.ID, using = "patientID")
    WebElement patientIDorName;

    @FindBy(how = How.XPATH, using = ".//*[@id='ngdialog2']/div[2]/form/div/p[5]/select")
    WebElement otherSurgeon;

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

    @FindBy(how = How.CSS, using = "input.add")
    WebElement addSurgery;

    public void selectSurgeon(String surgeon) {
        Select surgeonDrpdwn = new Select(surgeonDropdown);
        surgeonDrpdwn.selectByVisibleText(surgeon);
    }

    public void selectLocation(String ot) {
        int noOfLocations = otLocations.size();
        for (WebElement otLocation:otLocations) {
            if (otLocation.getText().equalsIgnoreCase(ot)){
                otLocation.click();
                break;
            }
        }
    }

    public void selectDateTime(String startdate, String stime, String enddate, String etime) {
        startdate = startdate.replace("/", "");
        stime = stime.replace(":", "");
        stime = stime.replace(" ", "");

        enddate = enddate.replace("/", "");
        etime = etime.replace(":", "");
        etime = etime.replace(" ", "");
        //System.out.println(startdate+stime+enddate+etime);
        otStartDateTime.sendKeys(startdate);
        otStartDateTime.sendKeys(Keys.TAB);
        otStartDateTime.sendKeys(stime);

        otEndDateTime.sendKeys(enddate);
        otEndDateTime.sendKeys(Keys.TAB);
        otEndDateTime.sendKeys(etime);
    }

    public void clickSave() {
        saveOTSurgicalBlock.click();
    }

    public void clickAddSurgery() {
        addSurgeryBtn.click();
    }

    public void addSugery(Table table) {
        List<TableRow> surgeries = table.getTableRows();
        for (TableRow surgery: surgeries) {
            clickAddSurgery();
            waitForElement(driver, ExpectedConditions.visibilityOfAllElementsLocatedBy(By.cssSelector(".ngdialog-content")));
            fillAutocomplete(patientIDorName, surgery.getCell("Patient ID or Name"));
            new Select(otherSurgeon).selectByVisibleText(surgery.getCell("Other Surgeon"));
            surgicalAssistant.sendKeys(surgery.getCell("Surgical Assistant"));
            anaesthetist.sendKeys(surgery.getCell("Anaesthetist"));
            scrubNurse.sendKeys(surgery.getCell("Scrub Nurse"));
            circulatingNurse.sendKeys(surgery.getCell("Circulating Nurse"));
            notes.sendKeys(surgery.getCell("Notes"));
            addSurgery.click();
        }
    }

    public void fillAutocomplete(WebElement autoComplete, String value){
        autoComplete.sendKeys(value);
        waitForElementOnPage(By.id("ui-id-45"));
        autoComplete.sendKeys(Keys.DOWN);
        findElement(By.id("ui-id-45")).click();
    }

}
