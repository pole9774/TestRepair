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
            // In the second version, the bottom bar no longer has resource-id "NiaBottomBar".
            // The selected "For you" tab is the first android.view.View at the bottom with selected="true" and contains a TextView with text "For you".
            WebElement forYouTab = driver.findElement(AppiumBy.xpath(
                "//android.view.View[@selected='true' and .//android.widget.TextView[@text='For you']]"
            ));
            Assert.assertTrue(forYouTab.isDisplayed(), "'For you' tab is not visible!");

            // Optionally, verify the label is present inside the tab
            WebElement forYouLabel = forYouTab.findElement(AppiumBy.xpath(".//android.widget.TextView[@text='For you']"));
            Assert.assertTrue(forYouLabel.isDisplayed(), "'For you' label is not visible!");
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
            // 1. Follow the 'Headlines' topic (from the 'For you' screen v2)
            WebElement sample_topic = driver.findElement(AppiumBy.xpath(
                "//android.view.View[@resource-id='forYou:topicSelection']//android.widget.TextView[@text='Headlines']/.."
            ));
            sample_topic.click();

            // 2. Click 'Done' button (from the 'For you' screen v2)
            WebElement done_button = driver.findElement(AppiumBy.xpath(
                "//android.widget.TextView[@text='Done']/parent::android.view.View"
            ));
            done_button.click();

            // 3. Verify that you can see the first news (from the news feed v2)
            WebElement first_news = driver.findElement(AppiumBy.xpath(
                "//android.view.View[@resource-id='forYou:feed']//android.widget.TextView[@text=\"The new Google Pixel Watch is here  — start building for Wear OS! ⌚\"]"
            ));
            Assert.assertTrue(first_news.isDisplayed(), "First news is not displayed!");

            // 4. Swipe to the second news (from the news feed v2)
            String containerXPath_forYou = "//android.view.View[@resource-id='forYou:feed']";
            while (driver.findElements(AppiumBy.xpath(
                "//android.view.View[@resource-id='forYou:feed']//android.widget.TextView[@text=\"Android Dev Summit ’22: Coming to you, online and around the world! ⛰\uFE0F\"]"
            )).isEmpty() && swipes < maxSwipes) {
                swipeUp(containerXPath_forYou);
                swipes++;
            }

            // 5. Verify that you can see the second news (from the news feed v2)
            WebElement second_news = driver.findElement(AppiumBy.xpath(
                "//android.view.View[@resource-id='forYou:feed']//android.widget.TextView[@text=\"Android Dev Summit ’22: Coming to you, online and around the world! ⛰\uFE0F\"]"
            ));
            Assert.assertTrue(second_news.isDisplayed(), "Second news is not displayed!");

            // 6. Go to the 'Interests' tab (bottom bar, v2)
            WebElement interests = driver.findElement(AppiumBy.xpath(
                "//android.widget.TextView[@text='Interests']/ancestor::android.view.View[@clickable='true']"
            ));
            interests.click();

            // 7. Swipe to 'Headlines' topic and unfollow it (interests_v2.xml)
            String containerXPath_interests = "//android.view.View[@resource-id='interests:topics']";
            swipes = 0;
            while (
                (driver.findElements(AppiumBy.xpath(
                    "//android.view.View[@resource-id='interests:topics']//android.widget.TextView[@text='Headlines']/parent::android.view.View"
                )).isEmpty() ||
                driver.findElements(AppiumBy.xpath(
                    "//android.view.View[@resource-id='interests:topics']//android.widget.TextView[@text='Headlines']/following-sibling::android.view.View//android.view.View[@content-desc='Unfollow interest']"
                )).isEmpty()) && swipes < maxSwipes
            ) {
                swipeUp(containerXPath_interests);
                swipes++;
            }

            WebElement unfollow = driver.findElement(AppiumBy.xpath(
                "//android.view.View[@resource-id='interests:topics']//android.widget.TextView[@text='Headlines']/following-sibling::android.view.View//android.view.View[@content-desc='Unfollow interest']"
            ));
            unfollow.click();

            // 8. Go to the 'For you' tab (bottom bar, v2)
            WebElement for_you = driver.findElement(AppiumBy.xpath(
                "//android.widget.TextView[@text='For you']/ancestor::android.view.View[@clickable='true']"
            ));
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
