# Personal Homepage Design

## Goal

Build a static personal homepage for the Algorithm Foundations coursework. The site presents Gao Sichen / Teng Shang De Si Gua as a student interested in 3D vision, computer graphics, Gaussian Splatting, and AI-assisted development. It also hosts the first technical blog post required by the assignment.

## Audience

The primary audience is the course grader. The secondary audience is someone who wants to understand the student's current technical interests from a public link.

## Public Information Boundary

The public website may show:

- Name: Gao Sichen / 高司晨
- Nickname: 藤上的丝瓜
- GitHub username and profile link: only-1-luffa
- Learning and research interests

The public website will not show:

- Student ID
- Phone number
- Email address
- Personal photo
- Specific class information

## Site Structure

- `site/index.html`: personal homepage and blog entry point.
- `site/blog/gps-gaussian-plus-camera-views.html`: first technical blog post.
- `site/styles/main.css`: shared responsive styling.
- `site/AGENTS.md`: project instructions and AI collaboration notes.
- `report/homework-report.md`: coursework report draft.
- `tests/site_checks.py`: local acceptance checks.

## Homepage Content

The homepage has these sections:

- Hero: name, nickname, concise identity line, GitHub link, and blog link.
- About: current interests in 3D vision, Gaussian Splatting, fixed-camera real-time 3D streaming, algorithms, and AI-assisted development.
- Focus areas: compact cards for 3D Vision, Gaussian Splatting, camera constraints, real-time 3D streaming, and AI-assisted development.
- Learning notes: GPS-Gaussian+ reading, Algorithm Foundations coursework, and AI Agent workflow.
- Blog preview: title and summary of the first post, linking to the blog page.

## Blog Post

Title: `GPS-Gaussian+ 学习笔记：固定机位如何影响实时三维直播`

The post is written as a learning note rather than a formal paper review. It connects the student's motivation, existing fixed-camera devices for real-time 3D streaming, to technical issues in sparse-view Gaussian Splatting:

- Why this direction matters.
- What Gaussian Splatting contributes to real-time 3D representation.
- Why fixed camera positions are restrictive.
- What GPS-Gaussian+ suggests about sparse views and generalizable rendering.
- Possible future optimizations: camera layout, view weighting, pose correction, local incremental update, and multi-source input.

External references should be limited to reliable public sources:

- GPS-Gaussian+ arXiv paper.
- GPS-Gaussian+ project page.
- GPS-Gaussian+ official GitHub repository.
- Original 3D Gaussian Splatting paper or project page if needed.

## Visual Style

The style should be quiet and technical, with a light background, clear typography, and restrained green/teal accents. It should be readable on desktop and mobile without depending on external fonts or build tooling.

## Error Handling And Deployment

The site is static, so failure modes are mainly broken links, missing files, and poor responsive layout. Local checks verify required files, internal links, GitHub link, and report placeholders. Deployment target is GitHub Pages, preferably the `only-1-luffa.github.io` repository.

## Testing

Use `tests/site_checks.py` to verify:

- Required files exist.
- Homepage links to the blog.
- Blog links back to homepage.
- GitHub profile link is present.
- Report draft exists.
- No obvious unresolved placeholders remain in public pages.

