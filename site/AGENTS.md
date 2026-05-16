# Project Instructions

This is a static coursework website for Algorithm Foundations assignment 1.

## Structure

- `index.html`: personal homepage.
- `blog/gps-gaussian-plus-camera-views.html`: first technical blog post.
- `styles/main.css`: shared layout and typography.
- `assets/images/gaussian-field.png`: local visual asset used by the homepage and blog.

## Editing Rules

- Keep the site static. Do not add a framework or package manager unless the assignment scope changes.
- Keep all public links relative except the GitHub profile and external references in the blog post.
- Do not publish student ID, phone number, email address, personal photo, or class details on the public website.
- Keep Chinese copy natural and personal. AI may polish wording, but the viewpoint should remain tied to the student's stated motivation: fixed-camera real-time 3D streaming.

## Verification

From the assignment root, run:

```powershell
python tests/site_checks.py
```

The script checks required files, internal links, public identity content, and basic responsive CSS.

