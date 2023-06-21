import string
import random
import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.custom_mapping = {}

    def shorten_url(self, original_url, custom_alias=None):
        if custom_alias:
            if custom_alias in self.custom_mapping:
                raise ValueError("Custom alias already exists.")

            self.custom_mapping[custom_alias] = original_url
            return custom_alias

        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choice(characters) for _ in range(6))
            if short_url not in self.url_mapping:
                break

        self.url_mapping[short_url] = original_url

        return short_url

    def get_original_url(self, short_url):
        if short_url in self.custom_mapping:
            return self.custom_mapping[short_url]
        else:
            return self.url_mapping.get(short_url)

    def generate_custom_alias(self, original_url):
        md5_hash = hashlib.md5(original_url.encode()).hexdigest()
        return md5_hash[:8]

# Usage example:
shortener = URLShortener()
original_url = "https://ca.indeed.com/career-advice/career-development/python-projects-for-resume"
short_url = shortener.shorten_url(original_url)
print("Short URL:", short_url)

retrieved_url = shortener.get_original_url(short_url)
print("Retrieved URL:", retrieved_url)

custom_alias = shortener.generate_custom_alias(original_url)
custom_short_url = shortener.shorten_url(original_url, custom_alias)
print("Custom Short URL:", custom_short_url)

retrieved_custom_url = shortener.get_original_url(custom_short_url)
print("Retrieved Custom URL:", retrieved_custom_url)
