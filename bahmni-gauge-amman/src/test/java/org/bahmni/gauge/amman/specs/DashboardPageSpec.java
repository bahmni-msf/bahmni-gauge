package org.bahmni.gauge.amman.specs;

import com.thoughtworks.gauge.BeforeClassSteps;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.bahmni.gauge.common.BahmniPage;
import org.bahmni.gauge.common.DriverFactory;
import org.bahmni.gauge.common.PageFactory;
import org.bahmni.gauge.common.clinical.DashboardPage;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebElement;

import java.util.List;

/**
 * Created by swarup on 1/2/17.
 */
public class DashboardPageSpec {
    @BeforeClassSteps
    public void waitForAppReady() {
        BahmniPage.waitForSpinner(DriverFactory.getDriver());
    }

    @Step("Verify the following display controls are visible <table>")
    public void implementation1(Table displayControlList) {
        List<TableRow> rows = displayControlList.getTableRows();
        for (TableRow row : rows) {
            String titleID = row.getCell("Display Control Title");
            Assert.assertTrue(String.format("The display control %s was not found in dashboard", titleID), isElementPresent(titleID));
        }
    }


    @Step("Verify the following display controls are hidden <table>")
    public void implementation2(Table displayControlList) {
        List<TableRow> rows = displayControlList.getTableRows();
        for (TableRow row : rows) {
            String titleID = row.getCell("Display Control Title");
            Assert.assertFalse(String.format("The display control %s was not hidden in dashboard", titleID), isElementPresent(titleID));
        }
    }

    private Boolean isElementPresent(String titleID) {
        DashboardPage dashboardPage = PageFactory.get(DashboardPage.class);
        List<WebElement> displayControlList = dashboardPage.displayControls;
        for (WebElement displayControl : displayControlList) {
            String displayControlText = "";
            try {
                displayControlText = displayControl.findElement(By.tagName("h2")).getText();
            } catch (Exception e) {
            }

            if (displayControlText.contains(titleID)) {
                return true;
            }
        }
        return false;
    }

    @Step("Verify following details of <Medical History> in Patient Dashboard <Table>")
    public void implementation3(String displayControlName , Table table) {
        DashboardPage dashboardPage = PageFactory.get(DashboardPage.class);
        WebElement displayControlElement = dashboardPage.findElementById(displayControlName.replace(" ", "-"));
        List<WebElement> actualObservationList = displayControlElement.findElements(By.tagName("show-observation"));
        List<TableRow> expectedObservationList = table.getTableRows();
        Assert.assertEquals(expectedObservationList.size(),actualObservationList.size());

        for (int i = 0 ; i < actualObservationList.size();i ++){
            String fieldName = expectedObservationList.get(i).getCell("FIELD");
            String value = expectedObservationList.get(i).getCell("VALUE");
            Assert.assertTrue(String.format("Field Name %s did not match in display control",fieldName),actualObservationList.get(i).getText().contains(fieldName));
            Assert.assertTrue(String.format("Value %s did not match in display control",value),actualObservationList.get(i).getText().contains(value));
        }
    }
}
