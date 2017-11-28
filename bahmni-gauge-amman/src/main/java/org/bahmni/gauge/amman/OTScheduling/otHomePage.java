package org.bahmni.gauge.amman.OTScheduling;

import org.bahmni.gauge.amman.home.HomePage;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

/**
 * Created by jaseenam on 20/07/17.
 */
public class otHomePage extends HomePage {
    @FindBy(how = How.LINK_TEXT, using = "Surgical Queues")
    WebElement surgicalQueues;

    @FindBy(how = How.LINK_TEXT, using = "OT Scheduling")
    WebElement OTScheduling;

    public void goToSurgicalQueues() {
        surgicalQueues.click();
    }

    public void goToOTScheduling() {
        OTScheduling.click();
    }
}
