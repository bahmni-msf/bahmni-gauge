package org.bahmni.gauge.amman.inpatient;

import org.apache.commons.collections.CollectionUtils;
import org.bahmni.gauge.common.inpatient.BedAssignmentPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.util.List;

public class AdmitPage extends BedAssignmentPage {

    @FindBy(how = How.CSS, using = ".bed.AVAILABLE")
    public List<WebElement> beds;

    @FindBy(how = How.CSS, using = ".adt-admit")
    public WebElement AdmitBtn;

    @FindBy(how = How.CSS, using = ".adt-transfer")
    public WebElement MovementBtn;

    @FindBy(how = How.CSS, using = ".adt-discharge")
    public WebElement DischargeBtn;

    @FindBy(how = How.CSS, using = "#modal-revise-button1")
    public WebElement AdtAdmitBtn;

    @FindBy(how = How.CSS, using = ".room:nth-child(2)")
    public WebElement RC4thFloor;

    @FindBy(how = How.CSS, using = ".room:nth-child(3)")
    public WebElement RC5thFloor;

    @FindBy(how = How.CSS, using = ".room:nth-child(2)")
    public WebElement Ward2ndFloor;

    @FindBy(how = How.CSS, using = ".room:nth-child(3)")
    public WebElement Ward3rdFloor;

    @FindBy(how = How.CSS, using = ".room:nth-child(2)")
    public WebElement Kahramana1stFloor;

    @FindBy(how = How.CSS, using = ".room:nth-child(3)")
    public WebElement Kahramana2ndFloor;

    @FindBy(how = How.CSS, using = ".room:nth-child(4)")
    public WebElement KahramanaBufferBeds;

    public Boolean assignAnEmptyBed() {
        waitForSpinner();
        //System.out.println(beds.size());
        if (!CollectionUtils.isEmpty(beds)) {
            return assignBed(RC4thFloor, beds.get(0));
        }
        return Boolean.FALSE;
    }

    private Boolean assignBed(WebElement ward, WebElement bed) {
        bed.click();
        if (AdmitBtn.isEnabled()) {
            AdmitBtn.click();
        } else if (MovementBtn.isEnabled()) {
            MovementBtn.click();
        }
        waitForElement(driver, ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
        AdtAdmitBtn.click();
        waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
        waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.id("overlay")));
        return Boolean.TRUE;
    }

    public void goToRC4thFloor() {

        RC4thFloor.click();
    }

    public void goToRC5thFloor() {

        RC5thFloor.click();
    }

    public void goToKahramanaBufferBeds() {

        KahramanaBufferBeds.click();
    }

    public void goToKahramana2ndFloor() {

        Kahramana2ndFloor.click();
    }

    public void goToKahramana1stFloor() {

        Kahramana1stFloor.click();
    }

    public void goToWard3rdFloor() {

        Ward3rdFloor.click();
    }

    public void goToWard2ndFloor() {

        Ward2ndFloor.click();
    }

    public Boolean dischargePatient() {
        waitForSpinner();
        DischargeBtn.click();
        waitForElement(driver, ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
        AdtAdmitBtn.click();
        waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
        waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.id("overlay")));
        return Boolean.TRUE;
    }
}