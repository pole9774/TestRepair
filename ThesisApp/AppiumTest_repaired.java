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
            // Search for message 'Hello, Alessandro' and verify it is displayed
            WebElement welcome_message = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Hello, Alessandro\"]"));
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
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            // Wait for the first task to be visible in the default (unordered) state
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]")
            ));

            // Find the sort button for activities (updated for v2)
            WebElement sort_activities_button = driver.findElement(
                    AppiumBy.xpath("//android.view.View[@content-desc=\"Sort activities\"]")
            );
            Assert.assertTrue(sort_activities_button.isDisplayed(), "Sort Activities button is not visible!");
            sort_activities_button.click();

            // Wait for the first task to be visible (now ordered a-z)
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task B\"]")
            ));

            WebElement task_name1 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task B\"]"));
            Assert.assertTrue(task_name1.isDisplayed(), "Task name (1) is not visible!");

            // Click the sort button again (now ordered z-a)
            sort_activities_button.click();

            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task D\"]")
            ));

            WebElement task_name2 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task D\"]"));
            Assert.assertTrue(task_name2.isDisplayed(), "Task name (2) is not visible!");

            // Click the sort button again (now back to default/unordered)
            sort_activities_button.click();

            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]")
            ));

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
            // Search for 'Hello, Alessandro', 'My Squads' title and 'Activities' title, and verify they are displayed
            WebElement welcome_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Hello, Alessandro\"]"));
            Assert.assertTrue(welcome_text.isDisplayed(), "Welcome title is not visible!");

            WebElement squads_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"My Squads\"]"));
            Assert.assertTrue(squads_text.isDisplayed(), "My Squads title is not visible!");

            WebElement activities_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Activities\"]"));
            Assert.assertTrue(activities_text.isDisplayed(), "Activities title is not visible!");

            // Verify they are correctly stacked one under the other
            int welcomeY = welcome_text.getLocation().getY();
            int squadsY = squads_text.getLocation().getY();
            int activitiesY = activities_text.getLocation().getY();

            Assert.assertTrue(welcomeY < squadsY, "Welcome text is not above My Squads text!");
            Assert.assertTrue(squadsY < activitiesY, "My Squads text is not above Activities text!");
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @Test
    public void taskCard_showsCorrectAssignedMembersCount() {
        try {
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            // Wait for the first task to be visible (unordered state)
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]")
            ));

            // Find and click the sort button for activities (updated for v2)
            WebElement sort_activities_button = driver.findElement(
                    AppiumBy.xpath("//android.view.View[@content-desc=\"Sort activities\"]")
            );
            Assert.assertTrue(sort_activities_button.isDisplayed(), "Sort Activities button is not visible!");
            sort_activities_button.click();

            // Wait for the first task to be visible (now ordered a-z)
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task B\"]")
            ));

            WebElement task_name1 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task B\"]"));
            Assert.assertTrue(task_name1.isDisplayed(), "Task name (1) is not visible!");

            // Check assigned members for Task B (should be 1)
            WebElement task_members1 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"1 assigned members\"]"));
            Assert.assertTrue(task_members1.isDisplayed(), "Task members (1) is not visible!");

            // Click the sort button again (now ordered z-a)
            sort_activities_button.click();

            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task D\"]")
            ));

            WebElement task_name2 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task D\"]"));
            Assert.assertTrue(task_name2.isDisplayed(), "Task name (2) is not visible!");

            // Check assigned members for Task D (should be 1)
            WebElement task_members2 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"1 assigned members\"]"));
            Assert.assertTrue(task_members2.isDisplayed(), "Task members (2) is not visible!");

            // Click the sort button again (back to default/unordered)
            sort_activities_button.click();

            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]")
            ));

            WebElement task_name3 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Task C\"]"));
            Assert.assertTrue(task_name3.isDisplayed(), "Task name (3) is not visible!");

            // Check assigned members for Task C (should be 1)
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
            // Verify 'My Squads' header is displayed
            WebElement squads_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"My Squads\"]"));
            Assert.assertTrue(squads_text.isDisplayed(), "My Squads title is not visible!");

            // Verify 'Activities' header is displayed
            WebElement activities_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Activities\"]"));
            Assert.assertTrue(activities_text.isDisplayed(), "Activities title is not visible!");
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
