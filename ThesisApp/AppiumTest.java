package it.polito.thesisapp;

import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.PointerInput;
import org.openqa.selenium.interactions.Sequence;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;
import java.time.Duration;
import java.util.Collections;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;

public class AppiumTest {

    private AndroidDriver driver;

    // Utility function to swipe horizontally (the finger goes from right to left)
    public void swipeLeft(String containerXPath) {
        WebElement container = driver.findElement(AppiumBy.xpath(containerXPath));

        int startY = container.getLocation().getY() + (container.getSize().getHeight() / 2);
        int startX = container.getLocation().getX() + (int) (container.getSize().getWidth() * 0.8);
        int endX = container.getLocation().getX() + (int) (container.getSize().getWidth() * 0.2);

        PointerInput finger = new PointerInput(PointerInput.Kind.TOUCH, "finger1");
        Sequence swipe = new Sequence(finger, 1);

        swipe.addAction(finger.createPointerMove(Duration.ZERO, PointerInput.Origin.viewport(), startX, startY)); // Start
        swipe.addAction(finger.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        swipe.addAction(finger.createPointerMove(Duration.ofMillis(1000), PointerInput.Origin.viewport(), endX, startY)); // Move
        swipe.addAction(finger.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));

        driver.perform(Collections.singletonList(swipe));
    }

    // Utility function to swipe horizontally (the finger goes from left to right)
    public void swipeRight(String containerXPath) {
        WebElement container = driver.findElement(AppiumBy.xpath(containerXPath));

        int startY = container.getLocation().getY() + (container.getSize().getHeight() / 2);
        int startX = container.getLocation().getX() + (int) (container.getSize().getWidth() * 0.2);
        int endX = container.getLocation().getX() + (int) (container.getSize().getWidth() * 0.8);

        PointerInput finger = new PointerInput(PointerInput.Kind.TOUCH, "finger1");
        Sequence swipe = new Sequence(finger, 1);

        swipe.addAction(finger.createPointerMove(Duration.ZERO, PointerInput.Origin.viewport(), startX, startY)); // Start
        swipe.addAction(finger.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        swipe.addAction(finger.createPointerMove(Duration.ofMillis(1000), PointerInput.Origin.viewport(), endX, startY)); // Move
        swipe.addAction(finger.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));

        driver.perform(Collections.singletonList(swipe));
    }

    @BeforeClass
    public void setup() throws URISyntaxException, MalformedURLException {
        UiAutomator2Options options = new UiAutomator2Options()
                .setDeviceName("emulator-5554")
                .setApp("C:/Users/pole9/Desktop/Poli/Tesi/App/ThesisApp/app/build/intermediates/apk/debug/app-debug.apk")
                .setAutomationName("UiAutomator2");

        driver = new AndroidDriver(new URI("http://127.0.0.1:4723").toURL(), options);

        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
    }

    @Test
    public void welcomeMessage_displaysUserFirstName() {
        try {
            // Search for message 'Welcome, Alessandro' and verify it is displayed
            WebElement welcome_message = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Welcome, Alessandro\"]"));
            Assert.assertTrue(welcome_message.isDisplayed(), "Welcome message is not visible!");
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @Test
    public void sortButton_callsToggleSortMode() {
        try {
            // Wait for the first task to be visible
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]")
            ));

            // Search for the sort button, verify it is displayed and click on it (tasks now ordered a-z)
            WebElement sort_tasks_button = driver.findElement(AppiumBy.xpath("//android.view.View[@content-desc=\"Sort tasks\"]"));
            Assert.assertTrue(sort_tasks_button.isDisplayed(), "Sort Tasks button is not visible!");
            sort_tasks_button.click();

            // Wait for the first task to be visible
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task A\"]")
            ));

            // Search for the first task alphabetically
            WebElement task_name1 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task A\"]"));
            Assert.assertTrue(task_name1.isDisplayed(), "Task name (1) is not visible!");

            // Click the sort button (tasks now ordered z-a)
            sort_tasks_button.click();

            // Wait for the first task to be visible
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task F\"]")
            ));

            // Search for the last task alphabetically
            WebElement task_name2 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task F\"]"));
            Assert.assertTrue(task_name2.isDisplayed(), "Task name (2) is not visible!");

            // Click the sort button (tasks now not ordered)
            sort_tasks_button.click();

            // Wait for the first task to be visible
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]")
            ));

            // Search for the expected task
            WebElement task_name3 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]"));
            Assert.assertTrue(task_name3.isDisplayed(), "Task name (3) is not visible!");
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @Test
    public void homeScreen_hasCorrectVerticalLayoutStructure() {
        try {
            // Search for 'Welcome, Alessandro', 'My Teams' title and 'Tasks' title, and verify they are displayed
            WebElement welcome_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Welcome, Alessandro\"]"));
            Assert.assertTrue(welcome_text.isDisplayed(), "Welcome title is not visible!");

            WebElement teams_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"My Teams\"]"));
            Assert.assertTrue(teams_text.isDisplayed(), "My Teams title is not visible!");

            WebElement tasks_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Tasks\"]"));
            Assert.assertTrue(tasks_text.isDisplayed(), "Tasks title is not visible!");

            // Verify they are correctly stacked one under the other
            int welcomeY = welcome_text.getLocation().getY();
            int teamsY = teams_text.getLocation().getY();
            int tasksY = tasks_text.getLocation().getY();

            Assert.assertTrue(welcomeY < teamsY, "Welcome text is not above My Teams text!");
            Assert.assertTrue(teamsY < tasksY, "My Teams text is not above Tasks text!");
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @Test
    public void taskCard_showsCorrectAssignedMembersCount() {
        try {
            // Wait for the first task to be visible
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]")
            ));

            // Search for the sort button, verify it is displayed and click on it (tasks now ordered a-z)
            WebElement sort_tasks_button = driver.findElement(AppiumBy.xpath("//android.view.View[@content-desc=\"Sort tasks\"]"));
            Assert.assertTrue(sort_tasks_button.isDisplayed(), "Sort Tasks button is not visible!");
            sort_tasks_button.click();

            // Wait for the first task to be visible
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task A\"]")
            ));

            // Search for the first task alphabetically
            WebElement task_name1 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task A\"]"));
            Assert.assertTrue(task_name1.isDisplayed(), "Task name (1) is not visible!");

            // Search for the number of assigned members on the task and verify it is displayed and it is correct
            WebElement task_members1 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"2 assigned members\"]"));
            Assert.assertTrue(task_members1.isDisplayed(), "Task members (1) is not visible!");

            // Click the sort button (tasks now ordered z-a)
            sort_tasks_button.click();

            // Wait for the first task to be visible
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task F\"]")
            ));

            // Search for the last task alphabetically
            WebElement task_name2 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task F\"]"));
            Assert.assertTrue(task_name2.isDisplayed(), "Task name (2) is not visible!");

            // Search for the number of assigned members on the task and verify it is displayed and it is correct
            WebElement task_members2 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"0 assigned members\"]"));
            Assert.assertTrue(task_members2.isDisplayed(), "Task members (2) is not visible!");

            // Click the sort button (tasks now not ordered)
            sort_tasks_button.click();

            // Wait for the first task to be visible
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]")
            ));

            // Search for the expected task
            WebElement task_name3 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]"));
            Assert.assertTrue(task_name3.isDisplayed(), "Task name (3) is not visible!");

            // Search for the number of assigned members on the task and verify it is displayed and it is correct
            WebElement task_members3 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"1 assigned members\"]"));
            Assert.assertTrue(task_members3.isDisplayed(), "Task members (3) is not visible!");
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @Test
    public void sectionHeaders_areDisplayedCorrectly() {
        try {
            // Verify 'My Teams' header is displayed
            WebElement teams_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"My Teams\"]"));
            Assert.assertTrue(teams_text.isDisplayed(), "My Teams title is not visible!");

            //Verify 'Tasks' header is displayed
            WebElement tasks_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Tasks\"]"));
            Assert.assertTrue(tasks_text.isDisplayed(), "Tasks title is not visible!");
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @AfterClass
    public void teardown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
