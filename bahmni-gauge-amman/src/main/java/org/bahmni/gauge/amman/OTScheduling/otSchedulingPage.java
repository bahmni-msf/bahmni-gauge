package org.bahmni.gauge.amman.OTScheduling;

import org.bahmni.gauge.amman.home.HomePage;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

import java.util.Date;

/**
 * Created by jaseenam on 20/07/17.
 */
public class otSchedulingPage extends otHomePage{
    @FindBy (how = How.CSS, using = ".back-btn.dashboard-link.ot-surgical-button")
    WebElement newSurgicalBlockBtn;

    public void gotoCreateSurgicalBlock() {
        newSurgicalBlockBtn.click();
    }

    public void goToSurgeryBlockDate(Date date) {

    }

    public void clickEditService(String surgicalBlock, String ot) {
    }
}
