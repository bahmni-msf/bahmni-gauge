package org.bahmni.gauge.amman.AppointmentScheduling;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.util.List;

/**
 * Created by jaseenam on 01/08/17.
 */

public class appointmentSchedulingAdminPage extends appointmentSchedulingHeader {
    @FindBy(how = How.CSS, using = ".add-service-btn")
    WebElement addServiceBtn;

    @FindBy(how = How.CSS, using = ".service-admin-content table thead tr th")
    public List<WebElement> columnNameElements;

    @FindBy(how = How.CSS, using = ".service-admin-content table tbody tr")
    public List<WebElement> rowsList;

    @FindBy(how = How.CSS, using = "#modal-revise-button1")
    WebElement serviceDeleteBtn;

    public void gotoAddNewServicePage() {
        addServiceBtn.click();
    }

    private int getColumnIndex(String columnName) {
        int i = 0;
        for (WebElement column : columnNameElements) {
            //System.out.println(column.getText());
            if (column.getText().contains(columnName)) {
                return i;
            }
            i++;
        }
        Assert.fail("Column '" + columnName + "' not found");
        return -1;
    }

    public String getColumnData(String columnName, String servicename) {
        int columnIndex = getColumnIndex(columnName);
        String actualData = "";
        WebElement row = selectGivenServiceRow(servicename);
//        System.out.println(columnName);
//        System.out.println(servicename);
//        System.out.println(actualData);
//        if (rowsList.isEmpty()) {
//            Assert.fail("Service not found");
//        }
//        else {
//            for (WebElement row : rowsList) {
//                if (row.findElements(By.tagName("td")).get(0).getText().equalsIgnoreCase(servicename)) {
                    actualData = row.findElements(By.tagName("td")).get(columnIndex).getText();
                    //System.out.println(actualData);
//                    break;
//                }
//            }
//        }
            return actualData;
    }

    public void clickEditService(String serviceName) {
        WebElement row = selectGivenServiceRow(serviceName);
        if (row != null) {
            row.findElement(By.linkText("Edit")).click();
        }
    }

    public void deleteService(String serviceName) {
        WebElement row = selectGivenServiceRow(serviceName);
        if (row == null){
            return;
        }
        click(row.findElement(By.linkText("Delete")));
        waitForElement(driver, ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
        serviceDeleteBtn.click();
        waitForElement(driver, ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".ngdialog-overlay")));
    }

    public WebElement selectGivenServiceRow(String serviceName) {
        WebElement noRow = null;
        if (rowsList.isEmpty()) {
            Assert.fail("No Service found");
            return noRow;
        }
        else {
            for (WebElement row : rowsList) {
                if (row.findElements(By.tagName("td")).get(0).getText().equalsIgnoreCase(serviceName)) {
                    return row;
                }
            }
        }
        return noRow;
    }
}
