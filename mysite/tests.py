from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from mysite import views
from .models import Post
from django.contrib.auth import get_user_model

# Create your tests here.
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/hello/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("hello"))
        self.assertTemplateUsed(response, "hello.html")
    
    def test_template_content(self):
        response=self.client.get(reverse("hello"))
        self.assertContains(response, "測試網頁")


#class AboutpageTests(SimpleTestCase):
#    def test_url_exists_at_correct_location(self):
#        response = self.client.get("")
#        self.assertEqual(response.status_code, 200)
 
#class PostTests(TestCase):
    
#    @classmethod
#    def setUpTestData(cls):
#        cls.post = Post.objects.create(text="this is a test!")

#    def test_model_content(self):
#        self.assertEqual(self.post.text, "this is a test!")

#    def test_url_exists_at_correct_location(self):  # new
#        response = self.client.get("/")
#        self.assertEqual(response.status_code, 200)

#    def test_homepage(self):  # 把本來三個分開的測試結合了。
#        response = self.client.get(reverse("practice"))
#        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response, "basic.html")
#        self.assertContains(response, "this is a test!")

#class BlogTests(TestCase):
#    @classmethod
#    def setUpTestData(cls):
#        cls.user = get_user_model().objects.create_user(
#            username="testuser", email="test@email.com", password="secret"
#        )

#       cls.post = Post.objects.create(
#            title="A good title",
#            body="Nice body content",
#            author=cls.user,
#        )


   # def test_post_model(self):
    #    self.assertEqual(self.post.title, "A good title")
     #   self.assertEqual(self.post.body, "Nice body content")
      #  self.assertEqual(self.post.author.username, "testuser")
       # self.assertEqual(str(self.post), "A good title")
        #self.assertEqual(self.post.get_absolute_url(), "/post/1/")



#    def test_post_createview(self):  # new
 #   response = self.client.post(
  #      reverse("post_new"),
   #     {
    #        "title": "New title",
     #       "body": "New text",
      #      "author": self.user.id,
       # },
    #)
    #self.assertEqual(response.status_code, 302)
    #self.assertEqual(Post.objects.last().title, "New title")
    #self.assertEqual(Post.objects.last().body, "New text")

#def test_post_deleteview(self):  # new
#        response = self.client.post(reverse("post_delete", args="1"))
#        self.assertEqual(response.status_code, 302)

#def test_post_updateview(self):  # new
#    response = self.client.post(
#        reverse("post_edit", args="1"),
#        {
#            "title": "Updated title",
#            "body": "Updated text",
#        },
#   )
#    self.assertEqual(response.status_code, 302)
#    self.assertEqual(Post.objects.last().title, "Updated title")
#    self.assertEqual(Post.objects.last().body, "Updated text")

#def test_post_createview(self):  # new
#    response = self.client.post(
#        reverse("post_new"),
#        {
#            "title": "New title",
#            "body": "New text",
#            "author": self.user.id,
#        },
#    )
#    self.assertEqual(response.status_code, 302)
#    self.assertEqual(Post.objects.last().title, "New title")
#    self.assertEqual(Post.objects.last().body, "New text")