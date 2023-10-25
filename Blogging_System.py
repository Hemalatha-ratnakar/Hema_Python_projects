class Blog:
    def __init__(self):
        self.posts = []

    def create_post(self, title, content):
        post = {'title': title, 'content': content}
        self.posts.append(post)
        print("New post created!")

    def display_posts(self):
        if not self.posts:
            print("No posts found.")
            return
        for index, post in enumerate(self.posts, 1):
            print(f"Post #{index}\nTitle: {post['title']}\nContent: {post['content']}\n")

    def update_post(self, post_index, title, content):
        if post_index < 1 or post_index > len(self.posts):
            print("Invalid post index.")
            return
        self.posts[post_index - 1] = {'title': title, 'content': content}
        print(f"Post #{post_index} updated!")

    def delete_post(self, post_index):
        if post_index < 1 or post_index > len(self.posts):
            print("Invalid post index.")
            return
        deleted_post = self.posts.pop(post_index - 1)
        print(f"Post #{post_index} deleted: {deleted_post['title']}")

def main():
    my_blog = Blog()
    
    while True:
        print("1. Create a new post")
        print("2. Display all posts")
        print("3. Update a post")
        print("4. Delete a post")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            my_blog.create_post(title, content)
        elif choice == "2":
            my_blog.display_posts()
        elif choice == "3":
            post_index = int(input("Enter the post index to update: "))
            title = input("Enter updated post title: ")
            content = input("Enter updated post content: ")
            my_blog.update_post(post_index, title, content)
        elif choice == "4":
            post_index = int(input("Enter the post index to delete: "))
            my_blog.delete_post(post_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
