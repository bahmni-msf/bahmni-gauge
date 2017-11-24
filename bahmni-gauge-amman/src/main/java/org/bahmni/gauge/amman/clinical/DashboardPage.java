package org.bahmni.gauge.amman.clinical;


import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;

import java.util.List;

/**
 * Created by jaseenam on 4/25/17.
 */
public class DashboardPage extends org.bahmni.gauge.common.clinical.DashboardPage {

    public boolean dashboardName(String dashboardname) {
        boolean val = false;
        String dashboardNameonUI = selectedTab.getText();
        if (dashboardNameonUI.equalsIgnoreCase(dashboardname)) {
            val = true;
        }
        return val;
    }
}
