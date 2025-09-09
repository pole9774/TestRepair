package com.google.samples.apps.nowinandroid.ui;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.PointerInput;
import org.openqa.selenium.interactions.Sequence;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;
import java.time.Duration;
import java.util.Collections;
import java.util.List;

public class AppiumTest {

    private AndroidDriver driver;

    // Utility function to swipe vertically (the finger goes from bottom to top)
    public void swipeUp(String containerXPath) {
        WebElement container = driver.findElement(AppiumBy.xpath(containerXPath));

        int startX = container.getLocation().getX() + (container.getSize().getWidth() / 2);
        int startY = container.getLocation().getY() + (int) (container.getSize().getHeight() * 0.8);
        int endY = container.getLocation().getY() + (int) (container.getSize().getHeight() * 0.2);

        PointerInput finger = new PointerInput(PointerInput.Kind.TOUCH, "finger1");
        Sequence swipe = new Sequence(finger, 1);

        swipe.addAction(finger.createPointerMove(Duration.ZERO, PointerInput.Origin.viewport(), startX, startY)); // Start
        swipe.addAction(finger.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        swipe.addAction(finger.createPointerMove(Duration.ofMillis(1000), PointerInput.Origin.viewport(), startX, endY)); // Move
        swipe.addAction(finger.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));

        driver.perform(Collections.singletonList(swipe));
    }

    // Utility function to swipe vertically (the finger goes top to bottom)
    public void swipeDown(String containerXPath) {
        WebElement container = driver.findElement(AppiumBy.xpath(containerXPath));

        int startX = container.getLocation().getX() + (container.getSize().getWidth() / 2);
        int startY = container.getLocation().getY() + (int) (container.getSize().getHeight() * 0.2);
        int endY = container.getLocation().getY() + (int) (container.getSize().getHeight() * 0.8);

        PointerInput finger = new PointerInput(PointerInput.Kind.TOUCH, "finger1");
        Sequence swipe = new Sequence(finger, 1);

        swipe.addAction(finger.createPointerMove(Duration.ZERO, PointerInput.Origin.viewport(), startX, startY)); // Start
        swipe.addAction(finger.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        swipe.addAction(finger.createPointerMove(Duration.ofMillis(1000), PointerInput.Origin.viewport(), startX, endY)); // Move
        swipe.addAction(finger.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));

        driver.perform(Collections.singletonList(swipe));
    }

    @BeforeClass
    public void setup() throws URISyntaxException, MalformedURLException {
        UiAutomator2Options options = new UiAutomator2Options()
                .setDeviceName("emulator-5554")
                .setApp("C:\\Users\\pole9\\Desktop\\Poli\\Tesi\\App\\nowinandroid\\app\\build\\intermediates\\apk\\demo\\release\\app-demo-release.apk")
                .setAutomationName("UiAutomator2");

        driver = new AndroidDriver(new URI("http://127.0.0.1:4723").toURL(), options);

        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
    }

    @Test
    public void firstScreen_isForYou() {
        try {
            // Search for the 'For you' tab using the text instead of resource-id
            // This approach is more stable across app versions
            WebElement for_you_tab = driver.findElement(AppiumBy.xpath("//android.view.View[@selected='true' and .//android.widget.TextView[@text='For you']]"));
            Assert.assertTrue(for_you_tab.isDisplayed(), "'For you' tab is not visible!");

            // Verify that 'For you' is selected
            Assert.assertTrue(for_you_tab.isSelected(), "'For you' tab is not selected!");

            // Additional verification that the For You text is present
            WebElement for_you_text = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text='For you']"));
            Assert.assertTrue(for_you_text.isDisplayed(), "'For you' text is not visible!");
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @Test
    public void feed_whenNoInterestsSelectionAndLoaded_showsFeed() {
        int maxSwipes = 10;
        int swipes = 0;

        try {
            // Follow the 'Headlines' topic (from the 'For you' screen)
            // The topic elements now have text rather than xpath position identifiers
            WebElement sample_topic = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Headlines\"]"));
            sample_topic.click();

            // Click 'Done' button - needs updated selector
            WebElement done_button = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Done\"]"));
            done_button.click();

            // Verify that you can see the first news
            // News items now have resource IDs in v2, and text may be slightly different
            WebElement first_news = driver.findElement(AppiumBy.xpath("//android.view.View[@resource-id=\"newsResourceCard:2\"]//android.widget.TextView[contains(@text, \"Google Pixel Watch\")]"));
            Assert.assertTrue(first_news.isDisplayed(), "First news is not displayed!");

            // Swipe to the second news - updated container selector for v2
            String containerXPath_forYou = "//android.view.View[@resource-id=\"forYou:feed\"]";
            while (driver.findElements(AppiumBy.xpath("//android.widget.TextView[contains(@text, \"Android Dev Summit\")]")).isEmpty() && swipes < maxSwipes) {
                swipeUp(containerXPath_forYou);
                swipes++;
            }

            // Verify that you can see the second news - updated selector
            WebElement second_news = driver.findElement(AppiumBy.xpath("//android.widget.TextView[contains(@text, \"Android Dev Summit\")]"));
            Assert.assertTrue(second_news.isDisplayed(), "Second news is not displayed!");

            // Go to the 'Interests' tab - updated to use text attribute
            WebElement interests = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Interests\"]"));
            interests.click();

            // Swipe to 'Headlines' topic and unfollow it - updated selectors for v2
            String containerXPath_interests = "//android.view.View[@resource-id='interests:topics']";
            swipes = 0;
            while ((driver.findElements(AppiumBy.xpath("//android.widget.TextView[@text=\"Headlines\"]")).isEmpty() || 
                    driver.findElements(AppiumBy.xpath("//android.view.View[@content-desc=\"Unfollow interest\"]")).isEmpty()) && 
                    swipes < maxSwipes) {
                swipeUp(containerXPath_interests);
                swipes++;
            }

            // Updated unfollow button selector for v2
            WebElement unfollow = driver.findElement(AppiumBy.xpath("//android.view.View[@content-desc=\"Unfollow interest\"]"));
            unfollow.click();

            // Go to the 'For you' tab - updated selector
            WebElement for_you = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"For you\"]"));
            for_you.click();
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
