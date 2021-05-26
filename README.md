# blog-django

Done

- Post CRUD
- post image
- top posts

<!-- TODO: Planned -->

<!--! Registration Page: -->

    ○ Username
    ○ Email
    ○ Password
    ○ Password Confirmation (two must match) (Bonus)

<!--! Login Page: -->

    ○ Form contains 2 fields. Username & PW.
    ○ Password will be shown in asterisks. when the user clicks on login, if he is blocked then redirect him back to login page with a message (sorry you are blocked contact the admin)
    ○ if he isn’t blocked then he will be authenticated. ( search for Django authentication)

<!--! pagination(Bonus):  -->

    Will have a pagination part where each page will contain only top 5 posts sorted by publish date. When click on Next it will get me the next 5 posts.

<!--! categories subscribe / unsubscribe system(Bonus): -->

    when click on subscribe to a category confirmation email would be send to the user with this message (Hello - user name you have subscribed successfully in - category name - welcome aboard )(search for sending email with Django)

<!--! single category page:  -->

    show posts with the current category

<!-- ! Post Page Content: -->

    ● Title
    ● Post Picture
    ● Content of the post
    ● The category that this post is under
    ● Comments section
    ● Tags related

<!-- ! Post Page Characteristics: -->

    ● Each comment shows the time of the comment and the username who wrote the comment.
    ● There will be a reply on comment (Bonus)
    ● Add comment Section. User must be signed in to can submit a comment (enter the text and a submit button to submit the comment)
    ● If the comment contains inappropriate words, it will show like ****** With the length of the undesired word. For example: (Bonus) [ ‘stupid’ → ****** ] [ ‘fool’ → **** ]
    ● Like and dislike counter on the posts.
    ● and if a post counted more than 10 dislikes it will be auto deleted. (Bonus)

<!-- ! Normal user characteristics: -->

    ● He can see posts and categories
    ● Search by tag, post title.
    ● If logged in he can like, dislike, comment and reply a comment on a post.
    ● If blocked, he cannot log into the system on login page (Your account is locked, please contact an admin.)

<!-- ! Admin user characteristics: -->

    ● Admin user, can make CRUD on posts.
    ● Admin user, can make CRUD on categories
    ● admin user, can block or unblock users.
    ● Admin user, can promote a normal user to an admin user so that he  will be able to log into the admin screen.
    ● Admin user can CRUN on forbidden words.

<!-- ! Admin page custommizations: -->

    ● When Admin clicks on Users Link, it would list all the users, in case The user is also an admin, his row will be colored by red. Else it will be a normal row. Or display is Admin equals to True.
    ● For the normal users there should be a button that enables the admin to either lock or unlock this user from logging to the system. And for the Admin users this button is not available So, an admin cannot lock another admin.
