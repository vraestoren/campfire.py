# <img src="https://github.com/user-attachments/assets/11427115-91e5-4785-ab62-54f7ed7add48" width="28" style="vertical-align:middle;" /> campfire.py

> Web-API for [Campfire](https://campfire.moe) Russian social network for fandom communities with posts, wikis, activities, and more.

## Quick Start
```python
from campfire import Campfire

campfire = Campfire()
campfire.login(email="example@gmail.com", password="password")

# Get your profile
print(campfire.get_my_profile())

# Browse the feed
print(campfire.get_feed(feed_type="all"))
```

---

## Authentication

| Method | Description |
|--------|-------------|
| `login(email, password)` | Sign in and store session tokens |

---

## Profile

| Method | Description |
|--------|-------------|
| `get_my_profile()` | Get current user's profile |
| `get_my_quest()` | Get current user's quests |
| `get_my_drafts(offset)` | Get your draft posts |
| `get_account_info(nickname)` | Get public profile by nickname |
| `get_account_posts(account_id, offset)` | Get posts by a user |

---

## Feed

| Method | Description |
|--------|-------------|
| `get_feed(feed_type, offset)` | Get posts from the feed |

**Feed types:**

| Value | Meaning |
|-------|---------|
| `1` | All |
| `2` | Subscribed |
| `3` | Good |
| `4` | Best |
| `5` | All subscriptions |
| `6` | Abyss |

---

## Posts & Comments

| Method | Description |
|--------|-------------|
| `get_post_content(post_id)` | Get a post by ID |
| `search_posts(query)` | Search posts by keyword |
| `publish_post(draft_id)` | Publish a draft |
| `get_draft_content(draft_id)` | Get content of a draft |
| `comment(pub_id, content, reply_id)` | Post a comment |
| `get_comments(pub_id, offset)` | Get comments on a post |
| `send_karma(pub_id, is_positive)` | Upvote or downvote a post |

---

## Fandoms

| Method | Description |
|--------|-------------|
| `get_fandom_info(fandom_id)` | Get fandom details |
| `get_fandom_posts(fandom_id, offset)` | Get posts in a fandom |
| `get_fandom_wiki(fandom_id, offset)` | Get fandom wiki |
| `get_fandom_wiki_section(fandom_id, section_id, offset)` | Get a wiki section |
| `get_wiki_articles(article_id)` | Get a wiki article |
| `get_popular_fandoms(card, offset)` | Browse popular fandoms |
| `sub_fandom(fandom_id, sub_type, important)` | Subscribe to a fandom |

---

## Activities & Rubrics

| Method | Description |
|--------|-------------|
| `get_activity_info(activity_id)` | Get activity details |
| `get_activity_posts(activity_id, offset)` | Get posts in an activity |
| `reject_activity(activity_id)` | Reject an activity |
| `member_activity(activity_id, is_member)` | Join or leave an activity |
| `get_rubric_info(rubric_id, offset)` | Get rubric info |
| `get_rubric_posts(rubric_id, offset)` | Get posts in a rubric |

---

## Misc

| Method | Description |
|--------|-------------|
| `get_image(image_id)` | Get image by ID |
| `get_project_donates()` | Get project donation info |
