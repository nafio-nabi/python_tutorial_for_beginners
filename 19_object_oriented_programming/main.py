from user import User
from post import Post

# an object. An object is an instance of a class.
app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

print()

app_user_one.change_job_title("DevOps trainer")
app_user_one.get_user_info()

print()

# an object. An object is an instance of a class.
app_user_two = User("john.doe@example.com", "John Doe", "pwd2", "Frontend Engineer")
app_user_two.get_user_info()

print()

# an object. An object is an instance of a class.
new_post = Post("Hello World", app_user_two.name)
new_post.get_post_info()