package org.bahmni.gauge.amman.specs;

import com.gargoylesoftware.htmlunit.ElementNotFoundException;
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

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

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
    public void implementation3(String displayControlName, Table table) {
        DashboardPage dashboardPage = PageFactory.get(DashboardPage.class);
        WebElement displayControlElement = dashboardPage.findElementById(displayControlName.replace(" ", "-"));
        List<WebElement> actualObservationList = getChildObsTags(displayControlElement);
        List<TableRow> expectedObservationList = table.getTableRows();
        Assert.assertEquals(expectedObservationList.size(), actualObservationList.size());

        for (int i = 0; i < actualObservationList.size(); i++) {
            String fieldName = expectedObservationList.get(i).getCell("FIELD").trim();
            String value = expectedObservationList.get(i).getCell("VALUE").trim();
            String actualField = actualObservationList.get(i).findElement(By.cssSelector("span")).getText().trim();
            String actualValue = actualObservationList.get(i).findElement(By.cssSelector(".value-text-only")).getText().replace("\n", "").trim();
            Assert.assertTrue(String.format("Field Name %s did not match in display control in text %s ", fieldName, actualField), actualField.contains(fieldName));
            for (String val : value.split(","))
                Assert.assertTrue(String.format("value %s did not match in display control in text %s ", val, actualValue), actualValue.contains(val.trim()));
        }
    }

    private List<WebElement> getChildObsTags(WebElement displayControlElement) {
        List<WebElement> op = new ArrayList<>();
        List<WebElement> tmp = displayControlElement.findElements(By.tagName("show-observation"));
        for (WebElement element : tmp) {
            try {
                element.findElement(By.tagName("show-observation"));
            } catch (NoSuchElementException e) {
                op.add(element);
            }
        }
        return op;
    }

    @Step("Wait for the scheduler to run and close the visit")
    public void waitForScheduler() {
        try {
            TimeUnit.MINUTES.sleep(1);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Step("Verify visit is closed")
    public void verifyConsultationIsNotPresent() {
        org.bahmni.gauge.amman.clinical.DashboardPage dashboardPage;
        dashboardPage = PageFactory.get(org.bahmni.gauge.amman.clinical.DashboardPage.class);
        Assert.assertFalse("Consultation button is present", dashboardPage.isEnterDataPresent());
    }

}