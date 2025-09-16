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
            // Search for the 'For you' tab
            WebElement for_you = driver.findElement(AppiumBy.xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/O0.r0/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]"));
            Assert.assertTrue(for_you.isDisplayed(), "'For you' is not visible!");

            // Verify that 'For you' is selected
            Assert.assertTrue(for_you.isSelected(), "'For you' is not selected!");
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
            WebElement sample_topic = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Headlines\"]"));
            sample_topic.click();

            // Click 'Done' button
            WebElement done_button = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Done\"]"));
            done_button.click();

            // Verify that you can see the first news
            WebElement first_news = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"The new Google Pixel Watch is here  — start building for Wear OS! ⌚\"]"));
            Assert.assertTrue(first_news.isDisplayed(), "First news is not displayed!");

            // Swipe to the second news
            String containerXPath_forYou = "//android.view.View[@resource-id=\"forYou:feed\"]";
            while (driver.findElements(AppiumBy.xpath("//android.widget.TextView[@text=\"Android Dev Summit ’22: Coming to you, online and around the world! ⛰\uFE0F\"]")).isEmpty() && swipes < maxSwipes) {
                swipeUp(containerXPath_forYou);
                swipes++;
            }

            // Verify that you can see the second news
            WebElement second_news = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Android Dev Summit ’22: Coming to you, online and around the world! ⛰\uFE0F\"]"));
            Assert.assertTrue(second_news.isDisplayed(), "Second news is not displayed!");

            // Go to the 'Interests' tab
            WebElement interests = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Interests\"]"));
            interests.click();

            // Swipe to 'Headlines' topic and unfollow it
            String containerXPath_interests = "//android.view.View[@resource-id='interests:topics']";
            swipes = 0;
            while ((driver.findElements(AppiumBy.xpath("//android.widget.TextView[@text=\"Headlines\"]")).isEmpty() || driver.findElements(AppiumBy.xpath("//android.view.View[@content-desc=\"Unfollow interest button\"]")).isEmpty()) && swipes < maxSwipes) {
                swipeUp(containerXPath_interests);
                swipes++;
            }

            WebElement unfollow = driver.findElement(AppiumBy.xpath("//android.view.View[@content-desc=\"Unfollow interest button\"]"));
            unfollow.click();

            // Go to the 'For you' tab
            WebElement for_you = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"For you\"]"));
            for_you.click();
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @Test
    public void interestsWithTopics_whenTopicsFollowed_showFollowedAndUnfollowedTopicsWithInfo() {
        try {
            // Go to the 'Interests' tab
            WebElement interests = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Interests\"]"));
            interests.click();

            // Follow the second topic
            WebElement follow_button = driver.findElement(AppiumBy.xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/O0.r0/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View"));
            follow_button.click();

            // Verify the first 3 topics are displayed
            WebElement first_topic = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Accessibility\"]"));
            Assert.assertTrue(first_topic.isDisplayed(), "First topic is not displayed!");

            WebElement second_topic = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Android Auto\"]"));
            Assert.assertTrue(second_topic.isDisplayed(), "Second topic is not displayed!");

            WebElement third_topic = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Android Studio & Tools\"]"));
            Assert.assertTrue(third_topic.isDisplayed(), "Third topic is not displayed!");

            // Unfollow the second topic
            WebElement unfollow_button = driver.findElement(AppiumBy.xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/O0.r0/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View"));
            unfollow_button.click();

            // Go to the 'For you' tab
            WebElement for_you = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"For you\"]"));
            for_you.click();
        } catch (NoSuchElementException e) {
            Assert.fail("Element not found: " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("Unexpected error: " + e.getMessage());
        }
    }

    @Test
    public void news_whenSuccessAndTopicIsSuccess_isShown() {
        int maxSwipes = 10;
        int swipes = 0;

        try {
            // Go to 'Interests' tab
            WebElement interests_tab = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Interests\"]"));
            interests_tab.click();

            // Click topic 'Accessibility'
            WebElement topic = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Accessibility\"]"));
            topic.click();

            // Swipe vertically until the first news title is found
            String containerXPath = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/O0.r0/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View";
            while (driver.findElements(AppiumBy.xpath("//android.widget.TextView[@text=\"Listen to our major Text to Speech upgrades for 64 bit devices \uD83D\uDCAC\"]")).isEmpty() && swipes < maxSwipes) {
                swipeUp(containerXPath);
                swipes++;
            }

            WebElement news_title = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Listen to our major Text to Speech upgrades for 64 bit devices \uD83D\uDCAC\"]"));
            Assert.assertTrue(news_title.isDisplayed(), "Title is not displayed!");

            // Swipe to the back button and click it
            swipes = 0;
            while (driver.findElements(AppiumBy.xpath("//android.view.View[@content-desc=\"Back\"]")).isEmpty() && swipes < maxSwipes) {
                swipeDown(containerXPath);
                swipes++;
            }
            WebElement back_button = driver.findElement(AppiumBy.xpath("//android.view.View[@content-desc=\"Back\"]"));
            back_button.click();

            // Go to 'For you' tab
            WebElement for_you_tab = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"For you\"]"));
            for_you_tab.click();
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
