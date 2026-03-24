from requests import Session

class Campfire:
    def __init__(self) -> None:
        self.api = "https://campfire.moe/api"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Android; U; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/33.0",
            "Accept": "application/json"
        }
        self.user_id = None
        self.nickname = None
        self.access_token = None
        self.login_token = None

    def _post(self, endpoint: str, data: dict = None) -> dict:
        return self.session.post(
            f"{self.api}{endpoint}", data=data).json()

    def _get(self, endpoint: str) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}").json()

    def login(self, email: str, password: str) -> dict:
        data = {
            "email": email,
            "password": password,
            "redir": False
        }
        response = self.session.post(
            f"{self.api}/auth/login", data=data)
        response_json = response.json()
        response_cookies = response.cookies
        if "account" in response_json:
            self.user_id = response_json["account"]["J_ID"]
            self.nickname = response_json["account"]["J_NAME"]
            self.access_token = response_cookies["token"]
            self.login_token = response_cookies["loginToken"]
            self.session.headers["J_API_ACCESS_TOKEN"] = self.access_token
            self.session.headers["J_API_LOGIN_TOKEN"] = self.login_token
        return response_json

    def comment(
            self,
            pub_id: int,
            content: str,
            reply_id: int = 0) -> dict:
        data = {
            "content": content,
            "reply_id": reply_id
        }
        return self._post(f"/pub/{pub_id}/comment?redir=false", data)

    def get_draft_content(self, draft_id: int) -> dict:
        return self._get(f"/drafts/{draft_id}")

    def publish_post(self, draft_id: int) -> dict:
        return self._post(f"/draft/{draft_id}/publish")

    def get_my_profile(self) -> dict:
        return self._get("/user")

    def get_my_quest(self) -> dict:
        return self._get("/user/quest")

    def send_karma(self, pub_id: int, is_positive: bool) -> dict:
        return self._get(f"/pub/{pub_id}/karma?positive={is_positive}")

    def reject_activity(self, activity_id: int) -> dict:
        return self._get(f"/activity/{activity_id}/reject")

    def sub_fandom(
            self,
            fandom_id: int,
            sub_type: str = "all",
            important: bool = True) -> dict:
        return self._get(
            f"/fandom/{fandom_id}/sub?type={sub_type}&important={important}")

    def member_activity(
            self,
            activity_id: int,
            is_member: bool) -> dict:
        return self._get(
            f"/activity/{activity_id}/member?member={is_member}")

    def get_my_drafts(self, offset: int = 0) -> dict:
        return self._get(f"/drafts?offset={offset}")

    def get_feed(
            self,
            feed_type: str = "all",
            offset: int = 0) -> dict:
        """
        FEED-TYPES:
             1 - ALL,
             2 - SUBSCRIBED,
             3 - GOOD,
             4 - BEST,
             5 - ALL_SUBS,
             6 - ABYSS
        """
        return self._get(f"/feed?type={feed_type}&offset={offset}")

    def get_account_info(self, nickname: str) -> dict:
        return self._get(f"/account/{nickname}")

    def get_account_posts(
            self,
            account_id: int,
            offset: int = 0) -> dict:
        return self._get(
            f"/account/{account_id}/publications?offset={offset}")

    def get_activity_info(self, activity_id: int) -> dict:
        return self._get(f"/activity/{activity_id}")

    def get_activity_posts(
            self,
            activity_id: int,
            offset: int = 0) -> dict:
        return self._get(
            f"/activity/{activity_id}/posts?offset={offset}")

    def get_fandom_info(self, fandom_id: int) -> dict:
        return self._get(f"/fandom/{fandom_id}")

    def get_fandom_posts(
            self,
            fandom_id: int,
            offset: int = 0) -> dict:
        return self._get(f"/fandom/{fandom_id}/posts?offset={offset}")

    def get_fandom_wiki(
            self,
            fandom_id: int,
            offset: int = 0) -> dict:
        return self._get(f"/fandom/{fandom_id}/wiki?offset={offset}")

    def get_fandom_wiki_section(
            self,
            fandom_id: int,
            section_id: int,
            offset: int = 0) -> dict:
        return self._get(
            f"/fandom/{fandom_id}/wiki/{section_id}?offset={offset}")

    def get_wiki_articles(self, article_id: int) -> dict:
        return self._get(f"/fandom/wiki/{article_id}")

    def get_popular_fandoms(
            self,
            card: bool = False,
            offset: int = 0) -> dict:
        return self._get(f"/fandom?card={card}&offset={offset}")

    def get_image(self, image_id: int) -> dict:
        return self._get(f"/image/{image_id}")

    def search_posts(self, query: str) -> dict:
        return self._get(f"/post/search?q={query}")

    def get_post_content(self, post_id: int) -> dict:
        return self._get(f"/post/{post_id}")

    def get_comments(
            self,
            pub_id: int,
            offset: int = 0) -> dict:
        return self._get(f"/post/{pub_id}/comments?offset={offset}")

    def get_project_donates(self) -> dict:
        return self._get("/project/donates")

    def get_rubric_info(
            self,
            rubric_id: int,
            offset: int = 0) -> dict:
        return self._get(f"/rubric/{rubric_id}?offset={offset}")

    def get_rubric_posts(
            self,
            rubric_id: int,
            offset: int = 0) -> dict:
        return self._get(f"/rubric/{rubric_id}?offset={offset}")
