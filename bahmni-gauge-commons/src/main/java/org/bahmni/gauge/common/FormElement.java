package org.bahmni.gauge.common;

import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;

import java.lang.reflect.Field;
import java.util.*;

public enum FormElement {
    INPUT("input") {
        public void fillUp(WebElement observationNode, String value) {
            List<WebElement> elementList = observationNode.findElements(getSelector());
            //WebElement element = observationNode.findElement(getSelector());
            for (WebElement element : elementList) {
                if( element.getAttribute("value").equals("")) {
                    if (!Objects.equals(element.getAttribute("type"), "date"))
                        element.clear();
                    element.sendKeys(value);
                    if (element.getAttribute("role") != null) {
                        element.sendKeys(Keys.ENTER);
                    }
                    break;
                }
            }
        }

        public HashMap<String,String> getValue(WebElement parent){

            List<WebElement> elements= parent.findElements(getSelector());
            HashMap<String,String> obs = new LinkedHashMap<>();
            String value="";
            int i=0;

            if(elements.size()>1){

                for (WebElement element:elements
                     ) {
                    value=value+ element.getAttribute("value");
                    i++;
                    if(i != elements.size())
                       value=value + ":";

                }
                obs.put(parent.findElement(By.cssSelector("label")).getText(),value);
            }
            else {
                obs.put(parent.findElement(By.cssSelector("label")).getText(),elements.get(0).getAttribute("value"));
            }

            return obs;
        }
    },
    TEXT_AREA("textarea") {
        public void fillUp(WebElement observationNode, String value) {
            List<WebElement> elementList = observationNode.findElements(getSelector());

            for (WebElement element : elementList) {
                if(element.getText().isEmpty()){
                    element.clear();
                    element.sendKeys(value);
                    break;
                }
            }
        }
        public  HashMap<String,String> getValue(WebElement parent){

            HashMap<String,String> obs = new LinkedHashMap<>();
            obs.put(parent.findElement(By.cssSelector("label")).getText(),parent.findElement(getSelector()).getAttribute("value"));
            return obs;
        }
    },
    SELECT("select") {
        public void fillUp(WebElement observationNode, String value) {
            new Select(observationNode.findElement(getSelector())).selectByVisibleText(value);
        }

        public HashMap<String,String> getValue(WebElement parent){

            HashMap<String,String> obs = new LinkedHashMap<>();
            String value=  new Select(parent.findElement(getSelector())).getFirstSelectedOption().getAttribute("value");
            obs.put(parent.findElement(By.cssSelector("label")).getText(),value);

          return obs;
        }
    },
    BUTTON("button") {
        public void fillUp(WebElement observationNode, String value) {
            for (WebElement button : observationNode.findElements(getSelector())) {
                if (value.contains(";")) {
                    String values[] = value.split(";");
                    for (String val: values) {

                        if (button.getText().contains(val)) {
                            try {
                                button.click();
                                break;
                            } catch (WebDriverException e) {
                                JavascriptExecutor js = ((JavascriptExecutor) getCurrentDriver(button));
                                js.executeScript("scrollBy(0,2500)");
                                Actions actions = new Actions(getCurrentDriver(button));
                                actions.moveToElement(button).click().build().perform();
                                break;
                            }
                        }
                    }
            }
            else {
                    if (button.getText().contains(value)) {
                        try {
                            button.click();
                            break;
                        } catch (WebDriverException e) {
                            JavascriptExecutor js = ((JavascriptExecutor) getCurrentDriver(button));
                            js.executeScript("scrollBy(0,2500)");
                            Actions actions = new Actions(getCurrentDriver(button));
                            actions.moveToElement(button).click().build().perform();
                            break;
                        }
                    }
                }

                }
        }

        public HashMap<String,String> getValue(WebElement parent){
            HashMap<String,String> obs = new LinkedHashMap<>();
            String values="";
            List<WebElement> buttons=parent.findElements(getSelector());

            for (WebElement button : buttons ) {
                if (button.getAttribute("class").contains("active")) {
                    values=values+button.getText();
                    values=values+";";
                }
                }
            if ( values.length() > 0 && values.charAt(values.length() - 1) == ';') {
                values = values.substring(0, values.length() - 1);
            }
            obs.put(parent.findElement(By.cssSelector("label")).getText(), values);
                if(obs.isEmpty())
                    obs.put(parent.findElement(By.cssSelector("label")).getText(),"");
                return obs;
            }
    },
    DIV_SELECT_SINGLE(".Select--single") {
        public void fillUp(WebElement observationNode, String value) {
            WebElement selector = observationNode.findElement(getSelector());
            selector.click();
            List<WebElement> selections = selector.findElement(By.cssSelector(".Select-menu-outer")).findElements(By.cssSelector("div"));
            for(WebElement selection : selections) {
                if (selection.getText().equals(value)) {
                    selection.click();
                    break;
                }
            }
        }
        public HashMap<String,String> getValue(WebElement parent){
            HashMap<String,String> obs = new LinkedHashMap<>();
            WebElement selector = parent.findElement(getSelector());
            obs.put(parent.findElement(By.cssSelector("label")).getText(),selector.findElement(By.cssSelector(".Select--single span")).getText());
            return obs ;
        }
    },
    UNKNOWN("") {
        public void fillUp(WebElement observationNode, String value) {
            System.out.println("Value :" + value + " not entered.");
        }
        public HashMap<String,String> getValue(WebElement parent){
            HashMap<String,String> obs = new LinkedHashMap<>();
            System.out.println("No Value found for the obs");
            obs.put("","");
            return  obs;
        }

    };

    public static final FormElement[] allTypes = {INPUT, TEXT_AREA, SELECT, DIV_SELECT_SINGLE, BUTTON};

    private final String cssSelector;
    FormElement(String cssSelector) {
        this.cssSelector = cssSelector;
    }

    abstract public void fillUp(WebElement observationNode, String value);
    abstract public Map<String,String> getValue(WebElement element);


    public By getSelector() {
        return By.cssSelector(cssSelector);
    }

    public WebDriver getCurrentDriver(WebElement element) {
        WebDriver driver = null;
        try {
            Field f = element.getClass().getDeclaredField("parent");
            f.setAccessible(true);
            Object obj = f.get(element);
            if (obj instanceof WebDriver) {
                driver = (WebDriver) obj;
            }
        } catch (NoSuchFieldException | IllegalAccessException e) {
            e.printStackTrace();
        }
        return driver;
    }
}
