package org.bahmni.gauge.amman.IDDoc;

import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.bahmni.gauge.common.BahmniPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class IDDocUploadPage extends BahmniPage {

    public void uploadImage(int visitNumber, Table table) {
        WebElement root;
        WebElement imagename;
        for (TableRow row : table.getTableRows()) {
            uploadFile(visitNumber, row.getCell("image"));
            root = findElement(By.cssSelector(".doc-upload-accordion>li:nth-of-type(" + (visitNumber + 1) + ")"));
            imagename = root.findElements(By.cssSelector(".concept-name.ng-pristine.ng-untouched.ng-valid.ui-autocomplete-input.ng-valid-required.ng-valid-selection")).get(0);
            imagename.clear();
            imagename.sendKeys(row.getCell("name"));
            waitForElementOnPage(By.cssSelector(".ui-menu[style*=\"display: block\"] .ui-menu-item>a"));
            driver.findElement(By.cssSelector(".ui-menu[style*=\"display: block\"] .ui-menu-item>a")).click();
        }
    }

    public void save(){
        findElement(By.cssSelector("button.btn.btn-primary:not([disabled])")).click();
    }
}
