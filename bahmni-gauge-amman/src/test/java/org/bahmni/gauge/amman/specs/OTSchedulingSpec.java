package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import org.bahmni.gauge.amman.OTScheduling.otHomePage;
import org.bahmni.gauge.amman.OTScheduling.otSchedulingPage;
import org.bahmni.gauge.amman.OTScheduling.otSurgicalBlockPage;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;

/**
 * Created by jaseenam on 20/07/17.
 */
public class OTSchedulingSpec {
    private otSchedulingPage OTSchedulingPage;
    private otHomePage OTHomePage;
    private otSurgicalBlockPage OTSurgicalBlockPage;

    public OTSchedulingSpec() {
        OTSchedulingPage = PageFactory.get(otSchedulingPage.class);
        OTHomePage = PageFactory.get(otHomePage.class);
        OTSurgicalBlockPage = PageFactory.get(otSurgicalBlockPage.class);
    }

    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Navigate to OT Scheduling tab")
    public void gotoOTScheduling() {
        OTHomePage.goToOTScheduling();
        waitForAppReady();
    }

    @Step("Create a new surgical block for <Ashraf Bustanji> in <OT 2> from date <08/08/2017> time <08:00 AM> to date <08/08/2017> time <11:00 AM>")
    public void createNewSurgicalBlock(String surgeon, String OT, String startdate, String starttime, String enddate, String endtime) {
        OTSchedulingPage.gotoCreateSurgicalBlock();
        waitForAppReady();
        OTSurgicalBlockPage.selectSurgeon(surgeon);
        OTSurgicalBlockPage.selectLocation(OT);
        OTSurgicalBlockPage.selectDateTime(startdate, starttime, enddate, endtime);
        OTSurgicalBlockPage.clickSave();
        waitForAppReady();
    }

    @Step("Add surgery with below details <table>")
    public void addSurgeriesInBlock(Table table) {
        OTSurgicalBlockPage.addSugery(table);
        OTSurgicalBlockPage.clickSave();
        waitForAppReady();
    }
}
