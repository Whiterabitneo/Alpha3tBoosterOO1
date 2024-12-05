from flask import Flask, render_template, request
import time
from selenium import webdriver
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

app = Flask(__name__)

# Initialize Redis for rate limiting
redis = Redis.from_url("redis://localhost:6379")  # Replace with your Redis URL in production

# Set up Flask-Limiter with Redis as the storage backend
limiter = Limiter(get_remote_address, storage_uri="redis://localhost:6379")
limiter.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# Apply rate limiting to the /boost endpoint
@limiter.limit("5 per minute")  # Limit to 5 requests per minute from the same IP address
@app.route('/boost', methods=['POST'])
def boost_account():
    target_url = request.form['target_url']
    num_followers = int(request.form['num_followers'])
    boost_method = request.form['boost_method']

    # Call the appropriate boosting function based on the selected method
    if boost_method == 'facebook_followers':
        boost_facebook_followers(target_url, num_followers)
    elif boost_method == 'facebook_likes':
        boost_facebook_likes(target_url, num_followers)
    elif boost_method == 'facebook_comments':
        boost_facebook_comments(target_url, num_followers)
    elif boost_method == 'instagram_followers':
        boost_instagram_followers(target_url, num_followers)
    elif boost_method == 'instagram_likes':
        boost_instagram_likes(target_url, num_followers)
    elif boost_method == 'instagram_comments':
        boost_instagram_comments(target_url, num_followers)
    elif boost_method == 'twitter_followers':
        boost_twitter_followers(target_url, num_followers)
    elif boost_method == 'twitter_likes':
        boost_twitter_likes(target_url, num_followers)
    elif boost_method == 'twitter_comments':
        boost_twitter_comments(target_url, num_followers)
    elif boost_method == 'telegram_followers':
        boost_telegram_followers(target_url, num_followers)
    elif boost_method == 'telegram_likes':
        boost_telegram_likes(target_url, num_followers)
    elif boost_method == 'telegram_comments':
        boost_telegram_comments(target_url, num_followers)
    elif boost_method == 'tiktok_followers':
        boost_tiktok_followers(target_url, num_followers)
    elif boost_method == 'tiktok_likes':
        boost_tiktok_likes(target_url, num_followers)
    elif boost_method == 'tiktok_comments':
        boost_tiktok_comments(target_url, num_followers)

    return f"Boosting to {target_url} completed!"

# Generalized Boosting Logic for Platforms
def boost_followers(driver, target_url, num_followers, follow_button_xpath):
    driver.get(target_url)
    time.sleep(5)
    
    for _ in range(num_followers):
        try:
            follow_button = driver.find_element_by_xpath(follow_button_xpath)
            follow_button.click()
            time.sleep(2)  # Wait a little before clicking again
        except Exception as e:
            print(f"Error while following: {e}")
            break
    
    # Refresh and check follower count
    driver.refresh()
    time.sleep(5)
    try:
        followers_count = driver.find_element_by_xpath("//a[contains(@href, '/followers/')]")
        current_followers = int(followers_count.text.replace(",", ""))  # Clean up the number
        if current_followers >= num_followers:
            print(f"Target account {target_url} has been boosted to {current_followers} followers.")
        else:
            print(f"Failed to boost {target_url}. Current followers: {current_followers}")
    except Exception as e:
        print(f"Error while retrieving followers count: {e}")

# Boost Instagram Followers Logic
def boost_instagram_followers(target_url, num_followers):
    driver = webdriver.Chrome()
    try:
        boost_followers(driver, target_url, num_followers, "//button[contains(text(), 'Follow')]")
    finally:
        driver.quit()

# Boost Facebook Followers Logic
def boost_facebook_followers(target_url, num_followers):
    driver = webdriver.Chrome()
    try:
        boost_followers(driver, target_url, num_followers, "//button[contains(text(), 'Follow')]")
    finally:
        driver.quit()

# Boost Facebook Likes Logic (Similar Logic as Followers)
def boost_facebook_likes(target_url, num_likes):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_likes):
            like_button = driver.find_element_by_xpath("//button[contains(text(), 'Like')]")
            like_button.click()
            time.sleep(2)  # Wait a little before liking again

        print(f"Liked {num_likes} posts on {target_url}")
    except Exception as e:
        print(f"Error while liking posts: {e}")
    finally:
        driver.quit()

# Boost Facebook Comments Logic (Similar Logic as Likes)
def boost_facebook_comments(target_url, num_comments):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_comments):
            comment_button = driver.find_element_by_xpath("//button[contains(text(), 'Comment')]")
            comment_button.click()
            time.sleep(2)  # Wait a little before commenting again
        
        print(f"Commented {num_comments} times on {target_url}")
    except Exception as e:
        print(f"Error while commenting on posts: {e}")
    finally:
        driver.quit()

# Boost Instagram Likes Logic
def boost_instagram_likes(target_url, num_likes):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_likes):
            like_button = driver.find_element_by_xpath("//button[contains(text(), 'Like')]")
            like_button.click()
            time.sleep(2)
        
        print(f"Liked {num_likes} posts on {target_url}")
    except Exception as e:
        print(f"Error while liking posts: {e}")
    finally:
        driver.quit()

# Boost Instagram Comments Logic
def boost_instagram_comments(target_url, num_comments):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_comments):
            comment_button = driver.find_element_by_xpath("//button[contains(text(), 'Comment')]")
            comment_button.click()
            time.sleep(2)
        
        print(f"Commented {num_comments} times on {target_url}")
    except Exception as e:
        print(f"Error while commenting on posts: {e}")
    finally:
        driver.quit()

# Boost Twitter Followers Logic (Similar to Instagram)
def boost_twitter_followers(target_url, num_followers):
    driver = webdriver.Chrome()
    try:
        boost_followers(driver, target_url, num_followers, "//button[contains(text(), 'Follow')]")
    finally:
        driver.quit()

# Boost Twitter Likes Logic (Similar to Instagram)
def boost_twitter_likes(target_url, num_likes):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_likes):
            like_button = driver.find_element_by_xpath("//button[contains(text(), 'Like')]")
            like_button.click()
            time.sleep(2)
        
        print(f"Liked {num_likes} tweets on {target_url}")
    except Exception as e:
        print(f"Error while liking tweets: {e}")
    finally:
        driver.quit()

# Boost Twitter Comments Logic (Similar to Instagram)
def boost_twitter_comments(target_url, num_comments):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_comments):
            comment_button = driver.find_element_by_xpath("//button[contains(text(), 'Comment')]")
            comment_button.click()
            time.sleep(2)
        
        print(f"Commented {num_comments} times on {target_url}")
    except Exception as e:
        print(f"Error while commenting on tweets: {e}")
    finally:
        driver.quit()

# Boost Telegram Followers Logic (Similar to Instagram)
def boost_telegram_followers(target_url, num_followers):
    driver = webdriver.Chrome()
    try:
        boost_followers(driver, target_url, num_followers, "//button[contains(text(), 'Join')]")
    finally:
        driver.quit()

# Boost Telegram Likes Logic (Similar to Instagram)
def boost_telegram_likes(target_url, num_likes):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_likes):
            like_button = driver.find_element_by_xpath("//button[contains(text(), 'Like')]")
            like_button.click()
            time.sleep(2)
        
        print(f"Liked {num_likes} posts on {target_url}")
    except Exception as e:
        print(f"Error while liking posts: {e}")
    finally:
        driver.quit()

# Boost Telegram Comments Logic (Similar to Instagram)
def boost_telegram_comments(target_url, num_comments):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_comments):
            comment_button = driver.find_element_by_xpath("//button[contains(text(), 'Comment')]")
            comment_button.click()
            time.sleep(2)
        
        print(f"Commented {num_comments} times on {target_url}")
    except Exception as e:
        print(f"Error while commenting on posts: {e}")
    finally:
        driver.quit()

# Boost TikTok Followers Logic (Similar to Instagram)
def boost_tiktok_followers(target_url, num_followers):
    driver = webdriver.Chrome()
    try:
        boost_followers(driver, target_url, num_followers, "//button[contains(text(), 'Follow')]")
    finally:
        driver.quit()

# Boost TikTok Likes Logic (Similar to Instagram)
def boost_tiktok_likes(target_url, num_likes):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_likes):
            like_button = driver.find_element_by_xpath("//button[contains(text(), 'Like')]")
            like_button.click()
            time.sleep(2)
        
        print(f"Liked {num_likes} posts on {target_url}")
    except Exception as e:
        print(f"Error while liking posts: {e}")
    finally:
        driver.quit()

# Boost TikTok Comments Logic (Similar to Instagram)
def boost_tiktok_comments(target_url, num_comments):
    driver = webdriver.Chrome()
    try:
        driver.get(target_url)
        time.sleep(5)
        
        for _ in range(num_comments):
            comment_button = driver.find_element_by_xpath("//button[contains(text(), 'Comment')]")
            comment_button.click()
            time.sleep(2)
        
        print(f"Commented {num_comments} times on {target_url}")
    except Exception as e:
        print(f"Error while commenting on posts: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
