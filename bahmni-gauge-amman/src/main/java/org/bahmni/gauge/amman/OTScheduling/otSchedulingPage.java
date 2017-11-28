package org.bahmni.gauge.amman.OTScheduling;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

/**
 * Created by jaseenam on 20/07/17.
 */
public class otSchedulingPage extends otHomePage {
    @FindBy(how = How.CSS, using = ".back-btn.dashboard-link.ot-surgical-button")
    WebElement newSurgicalBlockBtn;

    @FindBy(how = How.CSS, using = ".heading-cell")
    WebElement OT;

    @FindBy(how = How.CSS, using = ".calendar-current-day")
    WebElement calendarCurrentDay;

    @FindBy(how = How.LINK_TEXT, using = "Edit")
    WebElement editButton;

    public void gotoCreateSurgicalBlock() {
        newSurgicalBlockBtn.click();
    }

    public void goToSurgeryBlockDate(String date) {

    }

    public void clickEditService(String surgicalBlock, String ot) {
    }


    public void verifySurgicalBlockIsCreated(String surgeon, String ot, String startdate, String enddate) {
        if (startdate.contains("NOW")) {
            startdate = todayDateAsString();
        }
        if (enddate.contains("NOW")) {
            enddate = todayDateAsString();
        }
        if (calendarCurrentDay.getText().contains(startdate)) {
            if (calendarCurrentDay.getText().contains(enddate)) {
                List<WebElement> SurgicalBlocks = driver.findElements(By.className("surgicalBlock-surgenName"));
                for (WebElement SurgicalBlock : SurgicalBlocks) {
                    String surgeonName = driver.findElement(By.className("surgicalBlock-surgenName")).getText();
                    if (surgeonName.equalsIgnoreCase("Surgeon - "+surgeon)) {
                        waitForSpinner();
                        driver.findElement(By.className("surgical-block")).click();
                        //waitForElement(driver, ExpectedCondition <editButton.isEnabled());
                        editButton.click();
                        waitForSpinner();
                    }
                }

            }
        }


    }

    private String todayDateAsString() {
        DateFormat dateFormat = new SimpleDateFormat("dd MMM yyyy");
        Date today = new Date();
        return dateFormat.format(today);
    }
}
